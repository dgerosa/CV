import gspread
import numpy as np
import json
import urllib
import skywalker
import ads
from tqdm import tqdm
import copy
import sys
import time
import os


# Set to false when testing to avoid API limit
refresh=True

#########################################
print('Read citations from CV')
#########################################

with open('CV.tex', 'r') as f:
    CV = np.array(f.readlines())
ADSbibs =np.array([line.split("{")[1].split("}")[0] for line in CV if "%ADSkey" in line])
INSPIREbibs =np.array([line.split("{")[1].split("}")[0] for line in CV if "%INSPIREkey" in line])

#########################################
print('Get citations from ADS')
#########################################

with open('/Users/dgerosa/reps/dotfiles/adstoken.txt') as f:
    ads.config.token = f.read()

@skywalker.checkpoint('get_ads',refresh=refresh,verbose=False)
def get_ads():
    first_author=[]
    ADScitation_count=[]
    title=[]
    year=[]
    pub=[]
    arxiv_class=[]
    retrievedbibcodes=[]
    for b in tqdm(ADSbibs):
        if b:
            #q = list(ads.SearchQuery(bibcode=b,fl=['first_author','citation_count','title','year','pub','arxiv_class']))[0]
            q = list(ads.SearchQuery(q=b,fl=['first_author','citation_count','title','year','pub','arxiv_class','bibcode']))
            if len(q)!=1:
                raise ValueError("ADS error in "+b)
            q=q[0]
            first_author.append(q.first_author.split(",")[0]) # Last names are enough
            ADScitation_count.append(q.citation_count)
            title.append(np.squeeze(q.title))
            year.append(q.year)
            pub.append(q.pub)
            if q.arxiv_class is None:
                arxiv_class.append("")
            else:
                arxiv_class.append(q.arxiv_class[0])
            retrievedbibcodes.append(q.bibcode)
        else:
            first_author.append("")
            ADScitation_count.append(0)
            title.append("")
            year.append("")
            pub.append("")
            arxiv_class.append("")
            retrievedbibcodes.append("")

    first_author=np.array(first_author)
    ADScitation_count=np.array(ADScitation_count)
    title=np.array(title)
    year=np.array(year)
    pub=np.array(pub)
    arxiv_class=np.array(arxiv_class)
    retrievedbibcodes=np.array(retrievedbibcodes)

    pub=np.where(pub=='Ph.D. Thesis', 'PhD thesis', pub)
    pub=np.where(pub=='arXiv e-prints', 'arxiv', pub)
    pub=np.where(pub=='Caltech Undergraduate Research Journal (CURJ) : Winter 2014', 'Caltech Undergraduate Research Journal', pub)
    pub=np.where(pub=='Gravitational Wave Astrophysics', 'Astrophysics and Space Science Proceedings', pub)

    return first_author, ADScitation_count,title,year,pub, arxiv_class,retrievedbibcodes

first_author, ADScitation_count,title,year,pub, arxiv_class,retrievedbibcodes = get_ads()

#########################################
print('Get citations from INSPIRE')
#########################################

@skywalker.checkpoint('get_inspire',refresh=refresh,verbose=False)
def get_inspire():
    INSPIREcitation_count=[]
    for b in tqdm(INSPIREbibs):
        if b:
            n_retries=0
            while n_retries<10:
                try:
                    req = urllib.request.urlopen("https://inspirehep.net/api/literature?q=texkey:"+b)
                except urllib.error.HTTPError as e:
                    if e.code == 429:
                        print('here')
                        retry_time = req.getheaders()["retry-in"]
                        print('INSPIRE API error: retry-in', retry_time)
                        sleep(retry_time)
                        n_retries = n_retries + 1
                        continue
                    else:
                        raise ValueError("INSPIRE error in "+b)
                else:

                    q = json.loads(req.read().decode("utf-8"))
                    n = len(q['hits']['hits'])
                    if n!=1:
                        raise ValueError("INSPIRE error in "+b)
                    INSPIREcitation_count.append(q['hits']['hits'][0]['metadata']['citation_count'])
                    break
        else:
            INSPIREcitation_count.append(0)


    return np.array(INSPIREcitation_count)

INSPIREcitation_count = get_inspire()

MAXcitation_count=np.maximum(ADScitation_count,INSPIREcitation_count)


#########################################
print('Write Google Spreadsheet: List')
#########################################
gc = gspread.service_account()
sh = gc.open("Citation count")

ind = np.argsort(MAXcitation_count)[::-1]

first_author=first_author[ind]
ADScitation_count=ADScitation_count[ind]
INSPIREcitation_count=INSPIREcitation_count[ind]
MAXcitation_count=MAXcitation_count[ind]
title=title[ind]
year=year[ind]
pub=pub[ind]

worksheet = sh.worksheet("List")
worksheet.update("C3",np.expand_dims(first_author,1).tolist())
worksheet.update("D3",np.expand_dims(year,1).tolist())
worksheet.update("E3",np.expand_dims(title,1).tolist())
worksheet.update("F3",np.expand_dims(ADScitation_count,1).tolist())
worksheet.update("G3",np.expand_dims(INSPIREcitation_count,1).tolist())
worksheet.update("H3",np.expand_dims(MAXcitation_count,1).tolist())

worksheet.update("F2",str(np.sum(ADScitation_count)))
worksheet.update("G2",str(np.sum(INSPIREcitation_count)))
totalnumber = np.sum(MAXcitation_count)
worksheet.update("H2",str(totalnumber))

hindex = sum(x >= i + 1 for i, x in enumerate(sorted(  list(MAXcitation_count), reverse=True)))
worksheet.update("I2",str(hindex))

#########################################
print('Write Google Spreadsheet: Year')
#########################################

singleyear=np.array(list(set(year)))
journalcount = np.array([np.sum(year==s) for s in singleyear])

ind = np.argsort(singleyear)
singleyear=singleyear[ind]
journalcount=journalcount[ind]

worksheet = sh.worksheet("Years")
worksheet.update("A2",np.expand_dims(np.array(singleyear),1).tolist())
worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())

#########################################
print('Write Google Spreadsheet: Journal')
#########################################

singlepub=np.array(list(set(pub)))
shortpub = copy.deepcopy(singlepub)
shortpub=np.where(shortpub=="The Journal of Open Source Software", "JOS", shortpub)
shortpub=np.where(shortpub=="Physical Review Letters", "PRL", shortpub)
shortpub=np.where(shortpub=="The Astrophysical Journal", "APJ", shortpub)
shortpub=np.where(shortpub=="Classical and Quantum Gravity", "CQG", shortpub)
shortpub=np.where(shortpub=="Monthly Notices of the Royal Astronomical Society", "MNRAS", shortpub)
shortpub=np.where(shortpub=="General Relativity and Gravitation", "GRG", shortpub)
shortpub=np.where(shortpub=="IAU Symposium", "IAU", shortpub)
shortpub=np.where(shortpub=="Physical Review D", "PRD", shortpub)
shortpub=np.where(shortpub=="Caltech Undergraduate Research Journal", "CURJ", shortpub)
shortpub=np.where(shortpub=="Journal of Physics Conference Series", "JPcs", shortpub)
shortpub=np.where(shortpub=="Astrophysics and Space Science Proceedings", "ASSp", shortpub)
shortpub=np.where(shortpub=="Astronomy and Astrophysics", "A&A", shortpub)
shortpub=np.where(shortpub=="Physical Review Research", "PRR", shortpub)

journalcount = np.array([np.sum(pub==s) for s in singlepub])

ind = np.argsort(journalcount)[::-1]
singlepub=singlepub[ind]
shortpub=shortpub[ind]
journalcount=journalcount[ind]

worksheet = sh.worksheet("Journals")
worksheet.update("A2",np.expand_dims(np.array(singlepub),1).tolist())
worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())
worksheet.update("D2",np.expand_dims(np.array(shortpub),1).tolist())

#########################################
print('Write Google Spreadsheet: arXiv')
#########################################

singlearxiv=np.array(list(set(arxiv_class)))
# Remove empty
singlearxiv=singlearxiv[singlearxiv!=""]
journalcount = np.array([np.sum(arxiv_class==s) for s in singlearxiv])

ind = np.argsort(journalcount)[::-1]
singlearxiv=singlearxiv[ind]
journalcount=journalcount[ind]

worksheet = sh.worksheet("arXiv")
worksheet.update("A2",np.expand_dims(np.array(singlearxiv),1).tolist())
worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())



#########################################
print("Update CV")
#########################################

print("\tTotal number of citations: ", totalnumber)
print("\th-index: ", hindex)

with open('CV.tex', 'r') as f:
    CV = f.read()

CV = "%mark_hindex".join([CV.split("%mark_hindex")[0],"\n"+str(hindex)+" ",CV.split("%mark_hindex")[2]])

CV = "%mark_totalnumber".join([CV.split("%mark_totalnumber")[0],"\n"+str(round(totalnumber,-2))+" ",CV.split("%mark_totalnumber")[2]])

for have,found in zip(ADSbibs,retrievedbibcodes):
    if have!=found:
        print("\tReplacing ADS key:", have,"-->", found)
        CV = "".join([CV.split(have)[0],found,CV.split(have)[1]])

with open('CV.tex', 'w') as f:
    f.write(CV)

with open('CV.tex', 'r') as f:
    CV = f.read()

os.system('pdflatex CV >/dev/null')

#########################################
print("Update talklist")
#########################################

with open('talklist.tex', 'r') as f:
    talklist = f.read()

talklist = "%mark_intro".join([talklist.split("%mark_intro")[0],CV.split("%mark_intro")[1],talklist.split("%mark_intro")[2]])
talklist = "%mark_talknumbers".join([talklist.split("%mark_talknumbers")[0],CV.split("%mark_talknumbers")[1],talklist.split("%mark_talknumbers")[2]])
talklist = "%mark_talklist".join([talklist.split("%mark_talklist")[0],CV.split("%mark_talklist")[1],talklist.split("%mark_talklist")[2]])

with open('talklist.tex', 'w') as f:
    f.write(talklist)

os.system('pdflatex talklist >/dev/null')

#########################################
print("Update publist")
#########################################

with open('publist.tex', 'r') as f:
    publist = f.read()

publist = "%mark_intro".join([publist.split("%mark_intro")[0],CV.split("%mark_intro")[1],publist.split("%mark_intro")[2]])
publist = "%mark_pubnumbers".join([publist.split("%mark_pubnumbers")[0],CV.split("%mark_pubnumbers")[1],publist.split("%mark_pubnumbers")[2]])
publist = "%mark_publist".join([publist.split("%mark_publist")[0],CV.split("%mark_publist")[1],publist.split("%mark_publist")[2]])

with open('publist.tex', 'w') as f:
    f.write(publist)

os.system('filltex publist >/dev/null') # Note filltex to get the bibliography right

# #########################################
# print("Bibbase bibliography")
# #########################################
#
# file= open('publist.bib', 'r')
# biblio = file.read()
#
# # Conversion from ADS to whatever I want in bibbase
# biblio = biblio.replace('\mnras', 'Monthly Notices of the Royal Astronomical Society')
# biblio = biblio.replace('\mnrasl', 'Monthly Notices of the Royal Astronomical Society Letters')
# biblio = biblio.replace('\prd', 'Physical Review D')
# biblio = biblio.replace('\prl', 'Physical Review Letters')
# biblio = biblio.replace('\cqg', 'Classical and Quantum Gravity')
# biblio = biblio.replace('\\aap', 'Astronomy and Astrophysics')
#
#
# file = open('publist.bib', 'w')
# file.write(biblio)
# file.close()

#########################################
print("Update shortCV")
#########################################

CVshort = "%mark_short".join([CV.split("%mark_short")[0],CV.split("%mark_short")[2]])

with open('CVshort.tex', 'w') as f:
    f.write(CVshort)

os.system('pdflatex CVshort >/dev/null')


#########################################
print("Update transcript")
#########################################

with open('transcript.tex', 'r') as f:
    transcript = f.read()

transcript = "%mark_intro".join([transcript.split("%mark_intro")[0],CV.split("%mark_intro")[1],transcript.split("%mark_intro")[2]])

with open('transcript.tex', 'w') as f:
    f.write(transcript)

os.system('pdflatex transcript >/dev/null')

#########################################
print("Cleaning...")
#########################################
os.system('rm -rf *aux *bbl *blg *out *log *synctex.gz')

#########################################
print("Done!")
#########################################
