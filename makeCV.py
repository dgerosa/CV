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

from database import papers, talks

# Set to true when testing to avoid API limit
testing=True

def hindex(citations):
    return sum(x >= i + 1 for i, x in enumerate(sorted(  list(citations), reverse=True)))


def ads_citations(papers):

    print('Get citations from ADS')

    with open('/Users/dgerosa/reps/dotfiles/adstoken.txt') as f:
        ads.config.token = f.read()

    for k in tqdm(papers):
        for p in tqdm(papers[k]['data']):
            if p['ads']:
                if testing:
                    p['ads_citations'] = np.random.randint(0, 100)
                    p['ads_found'] = p['ads']
                else:
                    q = list(ads.SearchQuery(q=p['ads'],fl=['citation_count','bibcode']))
                    if len(q)!=1:
                        raise ValueError("ADS error in "+b)
                    q=q[0]
                    p['ads_citations'] = q.citation_count
                    p['ads_found'] = q.bibcode
            else:
                p['ads_citations'] = 0
                p['ads_found'] = ""

    return papers


def inspire_citations(papers):

    print('Get citations from INSPIRE')

    for k in tqdm(papers):
        for p in tqdm(papers[k]['data']):
            if p['inspire']:
                if testing:
                    p['inspire_citations'] = np.random.randint(0, 100)
                else:
                    n_retries=0
                    while n_retries<10:
                        try:
                            req = urllib.request.urlopen("https://inspirehep.net/api/literature?q=texkey:"+p['inspire'])
                        except urllib.error.HTTPError as e:
                            if e.code == 429:
                                print('here')
                                retry_time = req.getheaders()["retry-in"]
                                print('INSPIRE API error: retry-in', retry_time)
                                sleep(retry_time)
                                n_retries = n_retries + 1
                                continue
                            else:
                                raise ValueError("INSPIRE error in "+p['inspire'])
                        else:

                            q = json.loads(req.read().decode("utf-8"))
                            n = len(q['hits']['hits'])
                            if n!=1:
                                raise ValueError("INSPIRE error in "+b)
                            p['inspire_citations']=q['hits']['hits'][0]['metadata']['citation_count']
                            break

            else:
                p['inspire_citations'] = 0

    return papers


def parsepapers(papers,filename="parsepapers.tex"):

    print('Parse papers from database')

    out=[]
    for k in ['submitted','published','proceedings']:
        out.append("\\textcolor{color1}{\\textbf{"+papers[k]['label']+":}}")
        out.append("\\vspace{-0.5cm}")
        out.append("")
        out.append("\cvitem{}{\small\hspace{-1cm}\\begin{longtable}{rp{0.3cm}p{15.8cm}}")
        out.append("%")

        i = len(papers[k]['data'])
        for p in papers[k]['data']:
            out.append("\\textbf{"+str(i)+".} & & \\textit{"+p['title'].strip(".")+".}")
            out.append("\\newline{}")
            out.append(p['author'].replace("D. Gerosa","\\textbf{D. Gerosa}").strip(".")+".")
            out.append("\\newline{}")
            line=""
            if p['link']:
                line +="\href{"+p['link']+"}"
            if p['journal']:
                line+="{"+p['journal'].strip(".")+"}. "
            if p['arxiv']:
                line+="\href{https://arxiv.org/abs/"+p['arxiv'].split(":")[1].split(" ")[0]+"}{"+p['arxiv'].strip(".")+".}"
            out.append(line)
            if p['more']:
                out.append("\\newline{}")
                out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
            out.append("\\vspace{0.09cm}\\\\")
            out.append("%")
            i=i-1
        out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def parsetalks(talks,filename="parsetalks.tex"):

    print('Parse talks from database')

    out=[]
    out.append("Invited talks marked with *.")
    out.append("\\vspace{0.2cm}")
    out.append("")

    for k in ['conferences','seminars','posters','outreach']:
        out.append("\\textcolor{color1}{\\textbf{"+talks[k]['label']+":}}")
        out.append("\\vspace{-0.5cm}")
        out.append("")
        out.append("\cvitem{}{\small\hspace{-1cm}\\begin{longtable}{rp{0.3cm}p{15.8cm}}")
        out.append("%")

        i = len(talks[k]['data'])
        for p in talks[k]['data']:
            if p["invited"]:
                mark="*"
            else:
                mark=""
            out.append("\\textbf{"+str(i)+".} & "+mark+" & \\textit{"+p['title'].strip(".")+".}")
            out.append("\\newline{}")
            out.append(p['where'].strip(".")+", "+p['when'].strip(".")+".")
            if p['more']:
                out.append("\\newline{}")
                out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
            out.append("\\vspace{0.05cm}\\\\")
            out.append("%")
            i=i-1
        out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def metricspapers(papers,filename="metricspapers.tex"):

    print('Compute papers metrics')

    out=[]
    out.append("\cvitem{}{\\begin{tabular}{rcl}")
    out.append("\\textcolor{mark_color}{\\textbf{Publications}}: &\hspace{0.3cm} &")
    out.append("\\textbf{"+str(len(papers['published']['data']))+"} papers published in major peer-reviewed journals,")
    out.append("\\textbf{"+str(len(papers['submitted']['data']))+"} paper in submission stage,")
    out.append("\\\\ & &")
    out.append("\\textbf{"+str(len(papers['proceedings']['data']))+"} other publications (white papers, long-authorlist reviews, proceedings, software, etc)")
    out.append("\\\\ & &")

    first_author = []
    for k in ['submitted','published','proceedings']:
        for p in papers[k]['data']:
            if "D. Gerosa" not in p['author']:
                raise ValueError("Looks like you're not an author:", p['title'])
            first_author.append( p['author'].split("D. Gerosa")[0]=="" )

    out.append("(out of which \\textbf{"+str(np.sum(first_author))+"} first-authored papers and")

    press_release = []
    for k in ['submitted','published','proceedings']:
        for p in papers[k]['data']:
            press_release.append("press release" in p['more'])

    out.append("\\textbf{"+str(np.sum(press_release))+"} papers covered by press releases).")
    out.append("\end{tabular} }")

    ads_citations = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in papers])
    inspire_citations = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in papers])
    max_citations = np.maximum(ads_citations,inspire_citations)

    out.append("\\textcolor{mark_color}{\\textbf{Total number of citations}}: >"+str(round(np.sum(max_citations),-2))+".")
    out.append("\\textcolor{mark_color}{\\textbf{h-index}}: "+str(hindex(max_citations))+" (using ADS and InSpire).")
    out.append("\\\\")
    out.append("\\textcolor{mark_color}{\\textbf{Web links to list services}}:")
    out.append("\href{https://ui.adsabs.harvard.edu/search/fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype%3A%22misc%22%20OR%20doctype%3A%22inproceedings%22%20OR%20doctype%3A%22article%22%20OR%20doctype%3A%22eprint%22)&q=%20author%3A%22Gerosa%2C%20Davide%22&sort=citation_count%20desc%2C%20bibcode%20desc&p_=0}{\\textsc{ADS}};")
    out.append("\href{http://inspirehep.net/search?ln=en&ln=en&p=exactauthor%3AD.Gerosa.1&of=hb&action_search=Search&sf=&so=d&rm=citation&rg=25&sc=0}{\\textsc{InSpire}};")
    out.append("\href{http://arxiv.org/a/gerosa_d_1.html}{\\textsc{arXiv}}.")

    with open(filename,"w") as f: f.write("\n".join(out))


def metricstalks(talks,filename="metricstalks.tex"):

    print('Compute talks metrics')


    out=[]
    out.append("\cvitem{}{\\begin{tabular}{rcl}")
    out.append("\\textcolor{mark_color}{\\textbf{Presentations}}: &\hspace{0.3cm} &")
    out.append("\\textbf{"+str(len(talks['conferences']['data']))+"} talks at conferences,")
    out.append("\\textbf{"+str(len(talks['seminars']['data']))+"} talks at department seminars,")
    out.append("\\textbf{"+str(len(talks['posters']['data']))+"} posters at conferences,")
    out.append("\\\\ & &")

    invited = []
    for k in ['conferences','seminars','posters']:
        for p in talks[k]['data']:
            invited.append(p['invited'])

    out.append("(out of which \\textbf{"+str(np.sum(invited))+"} invited presentations),")
    out.append("\\textbf{"+str(len(talks['outreach']['data']))+"} outreach talks.")

    out.append("\end{tabular} }")

    with open(filename,"w") as f: f.write("\n".join(out))


papers = ads_citations(papers)
papers = inspire_citations(papers)
parsepapers(papers)
parsetalks(talks)
metricspapers(papers)
metricstalks(talks)


def convertjournal(j):
    journalconversion={}
    journalconversion['\prd']=["Physical Review D", "PRD"]
    journalconversion['\prdrc']=["Physical Review D", "PRD"]
    journalconversion['\prl']=["Physical Review Letters","PRL"]
    journalconversion['\prr']=["Physical Review Research","PRR"]
    journalconversion['\mnras']=["Monthly Notices of the Royal Astronomical Society","MNRAS"]
    journalconversion['\mnrasl']=["Monthly Notices of the Royal Astronomical Society","MNRAS"]
    journalconversion['\cqg']=["Classical and Quantum Gravity","CQG"]
    journalconversion['\\aap']=["Astronomy & Astrophysics","A&A"]
    journalconversion['\\apj']=["Astrophysical Journal","APJ"]
    journalconversion['\\apjl']=["Astrophysical Journal","APJ"]
    journalconversion['\grg']=["General Relativity and Gravitation","GRG"]
    journalconversion['\\natastro']=["Nature Astronomy","NatAstro"]
    journalconversion['Proceedings of the International Astronomical Union']=["IAU Proceedigs","IAU"]
    journalconversion['Journal of Physics: Conference Series']=["Journal of Physics: Conference Series","JoPCS"]
    journalconversion['Journal of Open Source Software']=["Journal of Open Source Software","JOSS"]
    journalconversion['Astrophysics and Space Science Proceedings']=["Astrophysics and Space Science Proceedings","AaSSP"]
    journalconversion['Caltech Undergraduate Research Journal']=["Caltech Undergraduate Research Journal","CURJ"]
    journalconversion["Chapter in ``Handbook of Gravitational Wave Astronomy'', Springer"]=["Springer book chapter","Springer"]

    if j in journalconversion:
        return journalconversion[j]
    else:
        return [j,j]


def citationspreadsheet(papers):

    gc = gspread.service_account()
    sh = gc.open("Citation count")

    print('Write Google Spreadsheet: List')

    spreaddata={}
    spreaddata['first_author']=[]
    spreaddata['ads_citations']=[]
    spreaddata['inspire_citations']=[]
    spreaddata['max_citations']=[]
    spreaddata['title']=[]
    spreaddata['journal']=[]
    spreaddata['year']=[]
    spreaddata['arxiv']=[]

    for k in papers:
        for p in papers[k]['data']:
            spreaddata['first_author'].append(p['author'].split(",")[0].split(".")[-1].strip().replace("\`",""))
            spreaddata['ads_citations'].append(p['ads_citations'])
            spreaddata['inspire_citations'].append(p['inspire_citations'])
            spreaddata['max_citations'].append(max(p['ads_citations'],p['inspire_citations']))
            spreaddata['title'].append(p['title'])
            if p['journal']:
                spreaddata['journal'].append(p['journal'].split("(")[0].replace("in press","").rstrip(" 0123456789.,") )
            elif p['arxiv']:
                spreaddata['journal'].append('arXiv')
            else:
                spreaddata['journal'].append("")
            if p['journal'] == "PhD thesis":
                spreaddata['year'].append(2016)
            elif p['journal'] and "(" in  p['journal'] and ")" in  p['journal']:
                spreaddata['year'].append(p['journal'].split("(")[-1].split(")")[0])
            elif p['arxiv']:
                spreaddata['year'].append("20"+p['arxiv'].split(':')[1][:2])
            else:
                spreaddata['year'].append()
            if p['arxiv']:
                spreaddata['arxiv'].append(p['arxiv'].split(']')[0].split("[")[1])
            else:
                spreaddata['arxiv'].append("None")
    tot = len(spreaddata['title'])
    for x in spreaddata:
        assert(len(spreaddata[x]) == tot)

    ind = np.argsort(spreaddata['max_citations'])[::-1]
    for x in spreaddata:
        spreaddata[x]=np.array(spreaddata[x])[ind]

    worksheet = sh.worksheet("List")
    worksheet.update("A3",np.expand_dims(np.arange(tot)+1,1).tolist())
    worksheet.update("C3",np.expand_dims(spreaddata['first_author'],1).tolist())
    worksheet.update("D3",np.expand_dims(spreaddata['year'],1).tolist())
    worksheet.update("E3",np.expand_dims(spreaddata['title'],1).tolist())
    worksheet.update("F3",np.expand_dims(spreaddata['ads_citations'],1).tolist())
    worksheet.update("G3",np.expand_dims(spreaddata['inspire_citations'],1).tolist())
    worksheet.update("H3",np.expand_dims(spreaddata['max_citations'],1).tolist())
    worksheet.update("F2",str(np.sum(spreaddata['ads_citations'])))
    worksheet.update("G2",str(np.sum(spreaddata['inspire_citations'])))
    worksheet.update("H2",str(np.sum(spreaddata['max_citations'])))
    worksheet.update("I2",str(hindex(spreaddata['max_citations'])))


    print('Write Google Spreadsheet: Year')


    singleyear=np.array(list(set(spreaddata['year'])))
    journalcount = np.array([np.sum(spreaddata['year']==s) for s in singleyear])
    ind = np.argsort(singleyear)
    singleyear=singleyear[ind]
    journalcount=journalcount[ind]

    worksheet = sh.worksheet("Years")
    worksheet.update("A2",np.expand_dims(np.array(singleyear),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())

    print('Write Google Spreadsheet: Journals')

    shortpub = [convertjournal(j)[1] for j in spreaddata['journal']]

    singlepub = np.array([convertjournal(j)[1] for j in list(set(shortpub))])
    journalcount = np.array([np.sum(np.array([convertjournal(j)[1] for j in shortpub])==s) for s in singlepub])

    ind = np.argsort(journalcount)[::-1]
    singlepub=singlepub[ind]
    journalcount=journalcount[ind]

    longjournals=[]
    for s in singlepub:
        for j in list(set(spreaddata['journal'])):
            if convertjournal(j)[1]==s:
                longjournals.append(convertjournal(j)[0])
                break
    # longpub=[]
    # shortpub=[]
    # for j in singlepub:
    #     if j in journalconversion:
    #         longpub.append(journalconversion[j][0])
    #         shortpub.append(journalconversion[j][1])
    #     else:
    #         longpub.append(j)
    #         shortpub.append(j)

    worksheet = sh.worksheet("Journals")
    worksheet.update("A2",np.expand_dims(np.array(longjournals),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())
    worksheet.update("D2",np.expand_dims(np.array(singlepub),1).tolist())


    print('Write Google Spreadsheet: arXiv')

    singlearxiv=np.array(list(set(spreaddata['arxiv'])))
    # Remove empty
    singlearxiv=singlearxiv[singlearxiv!=""]
    journalcount = np.array([np.sum(spreaddata['arxiv']==s) for s in singlearxiv])

    ind = np.argsort(journalcount)[::-1]
    singlearxiv=singlearxiv[ind]
    journalcount=journalcount[ind]

    worksheet = sh.worksheet("arXiv")
    worksheet.update("A2",np.expand_dims(np.array(singlearxiv),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())


citationspreadsheet(papers)

sys.exit()

- TAKE CARE OF  UPDADING THE ADS KEY
- BUILD CVSHORT, PUBLIST AND TALKLIST


#########################################
print("Update CV")
#########################################

print("\tTotal number of citations: ", totalnumber)
print("\th-index: ", hindex)

with open('CV.tex', 'r') as f:
    CV = f.read()

with open('publist.bib','r') as f:
    bib = f.read()

CV = "%mark_hindex".join([CV.split("%mark_hindex")[0],"\n"+str(hindex)+" ",CV.split("%mark_hindex")[2]])

CV = "%mark_totalnumber".join([CV.split("%mark_totalnumber")[0],"\n"+str(round(totalnumber,-2))+" ",CV.split("%mark_totalnumber")[2]])

for have,found in zip(ADSbibs,retrievedbibcodes):
    if have!=found:
        print("\tReplacing ADS key:", have,"-->", found)
        # Update in CV file
        CV = "".join([CV.split(have)[0],found,CV.split(have)[1]])
        # Remove outdated entery from bib file
        bib = "@".join([b for b in bib.split("@") if have not in b])


with open('CV.tex', 'w') as f:
    f.write(CV)

with open('publist.bib','w') as f:
    f.write(bib)



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

#########################################
print("Bibbase bibliography")
#########################################

with open('publist.bib', 'r') as f:
    biblio = f.read()

# Conversion from ADS to whatever I want in bibbase
biblio = biblio.replace('\mnras', 'Monthly Notices of the Royal Astronomical Society')
biblio = biblio.replace('\mnrasl', 'Monthly Notices of the Royal Astronomical Society Letters')
biblio = biblio.replace('\prd', 'Physical Review D')
biblio = biblio.replace('\prl', 'Physical Review Letters')
biblio = biblio.replace('\cqg', 'Classical and Quantum Gravity')
biblio = biblio.replace('\\aap', 'Astronomy and Astrophysics')


with open('publist.bib', 'w') as f:
    f.write(biblio)

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
