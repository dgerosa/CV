import gspread
import numpy as np
import json
import skywalker
import ads
from tqdm import tqdm
import copy
import sys
import time
import os
import requests
import urllib.request
import urllib.error
import html
from database import papers, talks
from datetime import datetime
import shutil
from github_release import gh_release_create


def hindex(citations):
    return sum(x >= i + 1 for i, x in enumerate(sorted(  list(citations), reverse=True)))

def pdflatex(filename):
    os.system('pdflatex '+filename+' >/dev/null')

def checkinternet():
    url = "http://www.google.com"
    timeout = 5
    connected = True
    try:
	    requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
	    connected = False
    return connected

def ads_citations(papers,testing=False):

    print('Get citations from ADS')

    with open('/Users/dgerosa/reps/dotfiles/adstoken.txt') as f:
        ads.config.token = f.read()

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:
                if p['ads']:
                    if testing:
                        p['ads_citations'] = np.random.randint(0, 100)
                        p['ads_found'] = p['ads']
                    else:
                        q = list(ads.SearchQuery(q=p['ads'],fl=['citation_count','bibcode']))
                        if len(q)!=1:
                            raise ValueError("ADS error in "+b)
                        q=q[0]
                        if q.citation_count is not None:
                            p['ads_citations'] = q.citation_count
                        else:
                            print("Warning: citation count is None.", p['ads'])
                            p['ads_citations'] = 0
                        p['ads_found'] = q.bibcode
                else:
                    p['ads_citations'] = 0
                    p['ads_found'] = ""
                pbar.update(1)

    return papers


def inspire_citations(papers,testing=False):

    print('Get citations from INSPIRE')

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:
                if p['inspire']:
                    print(p['inspire'])
                    if testing:
                        p['inspire_citations'] = np.random.randint(0, 100)
                    else:
                        n_retries=0
                        while n_retries<10:
                            try:
                                req = urllib.request.urlopen("https://inspirehep.net/api/literature?q=texkey:"+p['inspire'])
                            except urllib.error.HTTPError as e:
                                if e.code == 429:
                                    retry_time = 10 #req.getheaders()["retry-in"]
                                    print('INSPIRE API error: retry in', retry_time, 's.')
                                    time.sleep(retry_time)
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
                pbar.update(1)

    return papers


def parsepapers(papers,filename="parsepapers.tex"):

    print('Parse papers from database')

    out=[]
    for k in ['submitted','published','proceedings']:
        i = len(papers[k]['data'])


        if i>=1:
            out.append("\\textcolor{color1}{\\textbf{"+papers[k]['label']+":}}")
        out.append("\\vspace{-0.5cm}")
        out.append("")
        out.append("\cvitem{}{\small\hspace{-1cm}\\begin{longtable}{rp{0.3cm}p{15.8cm}}")
        out.append("%")

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
    if len(papers['submitted']['data'])>1:
        out.append("\\textbf{"+str(len(papers['submitted']['data']))+"} papers in submission stage,")
    elif len(papers['submitted']['data'])==1:
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
    inspire_citations = np.concatenate([[p['inspire_citations'] for p in papers[k]['data']] for k in papers])

    max_citations = np.maximum(ads_citations,inspire_citations)


    totalnumber = np.sum(max_citations)
    print("\tTotal number of citations:", totalnumber)
    hind = hindex(max_citations)
    print("\th-index:", hind)

    rounded = int(totalnumber/100)*100

    out.append("\\textcolor{mark_color}{\\textbf{Total number of citations}}: >"+str(rounded)+".")
    out.append("\\textcolor{mark_color}{\\textbf{h-index}}: "+str(hind)+" (using ADS and InSpire).")
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
    journalconversion["arXiv e-prints"]=["arXiv","arXiv"]


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


def builddocs():

    print("Update CV")
    pdflatex("CV")

    print("Update publist")
    pdflatex("publist")

    print("Update talklist")
    pdflatex("talklist")

    print("Update CVshort")
    with open('CV.tex', 'r') as f:
        CV = f.read()
    CVshort = "%".join(CV.split("%mark_CVshort")[::2])
    with open('CVshort.tex', 'w') as f:
        f.write(CVshort)
    pdflatex("CVshort")


def buildbib():

    print("Build bib file from ADS")

    with open('publist.bib', 'r') as f:
        publist = f.read()

    stored = []
    for p in publist.split('@'):
        if "BibDesk" not in p:
            stored.append(p.split("{")[1].split(",")[0])

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:

                if  p['ads_found'] and p['ads_found'] not in stored:
                    with urllib.request.urlopen("https://ui.adsabs.harvard.edu/abs/"+p['ads_found']+"/exportcitation") as f:
                        bib = f.read()
                    bib=bib.decode()
                    bib = "@"+list(filter(lambda x:'adsnote' in x, bib.split("@")))[0].split("</textarea>")[0]
                    bib=html.unescape(bib)

                    if "journal =" in bib:
                        j  = bib.split("journal =")[1].split("}")[0].split("{")[1]
                        bib = bib.replace(j,convertjournal(j)[0])

                    with open('publist.bib', 'a') as f:
                        f.write(bib)
                pbar.update(1)

def replacekeys():

    print("Checking ADS keys")

    with open('database.py', 'r') as f:
        database = f.read()

    with open('publist.bib', 'r') as f:
        publist = f.read()

    for k in (papers):
        for p in (papers[k]['data']):

            #if p['ads']== "2021ApJ...915...56G":
            #    p['ads'] = "2021arXiv210411247G"

            if p['ads'] != p['ads_found']:

                print("\tReplace:", p['ads'],"-->", p['ads_found'])

                # Update in database
                database = database.replace(p['ads'],p['ads_found'])
                # Remove from bib file
                publist = "@".join([b for b in publist.split("@") if p['ads'] not in b])


    with open('database.py', 'w') as f:
        f.write(database)

    with open('publist.bib', 'w') as f:
        f.write(publist)


def pushtogit():
    try:
        comment = sys.argv[1]
    except:
        comment = "Generic update"

    print("Push to git:", comment)
    print(" ")
    os.system("git add -u")
    os.system("git commit -m '"+comment+"'")
    os.system("git push")


def publishgithub():
    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    print("Publish github release:", date)

    shutil.copy2("CV.pdf", "DavideGerosa_fullCV.pdf")
    shutil.copy2("CVshort.pdf", "DavideGerosa_shortCV.pdf")
    shutil.copy2("publist.pdf", "DavideGerosa_publist.pdf")
    shutil.copy2("publist.bib", "DavideGerosa_publist.bib")
    shutil.copy2("talklist.pdf", "DavideGerosa_talklist.pdf")

    # Create a github token, see:
    # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    # Make sure a GITHUB_TOKEN variable is part of the environment variables

    gh_release_create("dgerosa/CV", date, publish=True, name=date, asset_pattern="DavideGerosa_*")



#####################################


if __name__ == "__main__":

    connected= True
    if connected:
        # Set testing=True to avoid API limit
        papers = ads_citations(papers,testing=False)
        papers = inspire_citations(papers,testing=False)
        parsepapers(papers)
        parsetalks(talks)
        metricspapers(papers)
        metricstalks(talks)
        buildbib()
        citationspreadsheet(papers)

    replacekeys()
    builddocs()

    if connected:
        pushtogit()
        publishgithub()
