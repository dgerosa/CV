import numpy as np
import json
#import ads
from tqdm import tqdm
import copy
import sys
import time
import os
import requests
import urllib.request
import urllib.error
import html
from database import papers, talks, group
from datetime import datetime
import shutil
import warnings
import re
import unicodedata
from glob import glob   
#import gspread

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

relativepathwebsiterepo = "../website"

def hindex(citations):
    return sum(x >= i + 1 for i, x in enumerate(sorted(  list(citations), reverse=True)))

def roundto100(N):
    return int(N/100)*100

def pdflatex(filename):
    os.system('pdflatex '+filename+' >/dev/null')

def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

def checkinternet():
    url = "http://www.google.com"
    timeout = 5
    connected = True
    try:
	    requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
	    connected = False
    return connected

def slugify(text):
    # Normalize unicode characters to closest ASCII equivalent
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    # Convert to lowercase
    text = text.lower()
    # Remove all characters except alphanumerics, spaces, and hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    # Collapse multiple hyphens
    text = re.sub(r'-+', '-', text)
    # Strip leading/trailing hyphens
    return text.strip('-')


def nameinitial(name):
    parts = name.split()
    return f"{parts[0][0]}. {' '.join(parts[1:])}"

def ads_citations(papers,testing=False):

    print('Get citations from ADS')

    path = os.path.expandvars('$HOME/reps/dotfiles/adstoken.txt')
    with open(path) as f:
        #ads.config.token = f.read()
        token = f.read()

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:
                if p['ads']:
                    if testing:
                        p['ads_citations'] = np.random.randint(0, 100)
                        p['ads_found'] = p['ads']
                    else:
                        n_retries=0
                        
                        p['ads_citations'] = 0
                        p['ads_found'] = ""
                        
                        while n_retries<10:
                            try:
                                with warnings.catch_warnings():
                                    warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host")
                                    r = requests.get("https://api.adsabs.harvard.edu/v1/search/query?q="+p['ads'].replace("&","%26")+"&fl=citation_count,bibcode",headers={'Authorization': 'Bearer ' + token},verify=False)
                                q= r.json()['response']['docs']
                                #print(p['ads'], q)
                                if len(q)!=1:
                                    raise ValueError("ADS error in "+b)
                                q=q[0]
                                if q['citation_count'] is not None:
                                    p['ads_citations'] = q['citation_count']
                                else:
                                    print("Warning: citation count is None.", p['ads'])
                                    p['ads_citations'] = 0
                                p['ads_found'] = q['bibcode']

                            except:
                                retry_time = 10 #req.getheaders()["retry-in"]
                                print('ADS API error: retry in', retry_time, 's. -- '+p['ads'])
                                time.sleep(retry_time)
                                n_retries = n_retries + 1
                            
                                if n_retries==11:
                                    print('ADS API error: giving up -- '+p['ads'])

                                    #raise ValueError("ADS error in "+p['ads'])
                                continue
                            else:
                                break

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
                                    print('INSPIRE API error: retry in', retry_time, 's. -- '+p['inspire'])
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
            #out.append("\\textbf{"+str(i)+".} & & \\textit{"+p['title'].replace("_","\\_").strip(".")+".}")
            title = p['title'].replace("_", "\\_").rstrip(".")
            if not title.endswith("?"):
                title += "."
            out.append(f"\\textbf{{{i}.}} & & \\textit{{{title}}}")
            
            out.append("\\newline{}")
            out.append(p['author'].replace("D. Gerosa","\\textbf{D. Gerosa}").strip(".")+".")
            out.append("\\newline{}")
            line=""
            if p['link']:
                line +="\href{"+p['link']+"}"
            if p['journal']:
                line+="{"+p['journal'].strip(".")+"}. "
            if 'erratum' in p.keys():
                if p['errlink']:
                    line +="\href{"+p['errlink']+"}"
                if p['erratum']:
                    line+="{Erratum: "+p['erratum'].strip(".")+"}. "
            if p['arxiv']:
                line+="\href{https://arxiv.org/abs/"+p['arxiv'].split(":")[1].split(" ")[0].split(" ")[0]+"}{"+p['arxiv'].strip(".")+".}"
            out.append(line)
            if p['more']:
                out.append("\\newline{}")
                out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
            out.append("\\vspace{0.09cm}\\\\")
            out.append("%")
            i=i-1
        out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def markdownpapers(papers,filename="_publications.md"):

    print('Markdown paper list for website')

    out=[]

    papertype= ['submitted','published','proceedings']


    out.append("## Summary")

    for k in papertype:
        i = len(papers[k]['data'])
        out.append("**"+str(i)+"** ["+papers[k]['label']+"](#"+slugify(papers[k]['label'])+")")
        if k!=papertype[-1]:
            out[-1]+=("\\")
        else: 
            out.append("")

    out.append("")
    out.append("---")
    out.append("")

    for k in papertype:
        i = len(papers[k]['data'])

        if i>=1:
            out.append("## "+papers[k]['label'])
        out.append("")

        for p in papers[k]['data']:
            name = p['author'].replace("D. Gerosa","**D. Gerosa**").strip(".")
            name = name.replace("\\`o", "o'")
            name = name.replace("\\v{s}", "s")
            out.append("**"+str(i)+".**")
            #out.append("*"+p['title'].strip(".").replace("$", "$$")+"*.\\")
            title = p['title'].rstrip(".").replace("$", "$$")
            if not title.endswith("?"):
                title += "."
            out.append("*" + title + "*\\")
            out.append(name+".\\")
            line=""
            # if p['link']:
            #     line+='['
            # if p['journal']:
            #     line+=p['journal'].strip(".")
            # if p['link']:
            #     line+="]("+p['link']+")"
            # if p['journal']:
            #     line+=". "
            # if 'erratum' in p.keys():
            #     line+=" Erratum: "
            #     if p['errlink']:
            #         line+='['
            #     if p['erratum']:
            #         line+=p['erratum'].strip(".")
            #     if p['errlink']:
            #         line+="]("+p['errlink']+")"
            #     line+='. '
            if p['link']:
                line += '<a href="' + p['link'] + '" style="color: inherit; text-decoration: none;">'
            if p['journal']:
                line += p['journal'].strip(".")
            if p['link']:
                line += '</a>'
            if p['journal']:
                line += '. '

            if 'erratum' in p:
                line += ' Erratum: '
                if p['errlink']:
                    line += '<a href="' + p['errlink'] + '" style="color: inherit; text-decoration: none;">'
                if p['erratum']:
                    line += p['erratum'].strip(".")
                if p['errlink']:
                    line += '</a>'
                line += '. '
            if p['arxiv']:
                line += '<a href="https://arxiv.org/abs/' + p['arxiv'].split(":")[1].split()[0] + '" style="color: inherit; text-decoration: none;">' + p['arxiv'].strip(".") + '</a>.'
                #line+="["+p['arxiv'].strip(".")+"](https://arxiv.org/abs/"+p['arxiv'].split(":")[1].split(" ")[0].split(" ")[0]+")."
            out.append(line)
            if p['more']:
                out[-1]+="\\"
                out.append(p['more'].strip(".")+".")
            i=i-1

            out.append(" ")
            #break
        #continue
        out.append("")
        out.append("---")
        out.append("")
        
    out = apply_journal_conversion(out)

    with open(filename,"w") as f: f.write("\n".join(out))


def checkblogposts(papers):
    today = datetime.today().strftime('%Y-%m-%d')

    print('Check blog posts for papers')
    posts = glob(relativepathwebsiterepo+"/_posts/*.md")        
    #print(posts)
    for k in ['submitted','published','proceedings']:
        for p in papers[k]['data']:

            target_substring = slugify(p['title'])
            #print(target_substring)
            # Build a regex pattern like r"\d{4}-\d{2}-\d{2}-report"
            pattern = rf"{relativepathwebsiterepo}/_posts/\d{{4}}-\d{{2}}-\d{{2}}-{re.escape(target_substring)}.md"

            # Check if any string matches the pattern
            #if any(re.fullmatch(pattern, s) for s in posts):
            #    pass
                #print("Found!")
            #else:
                #print("Not found", slugify(p['title']))
            if True:
                out=[]
                out.append("---")
                cleantitle = p['title'].strip(".").replace("$", "$$").replace("`", "'")
                out.append(f"title: \"{cleantitle}\"")
                out.append(f"date: {today}")
                out.append(f"permalink: /posts/{today}-{slugify(p['title'])}")
                out.append("tags:")
                out.append("  - Papers")
                out.append("  - Milano")
                out.append("---")

                [out.append("") for _ in range(5)] 

                #out.append("*"+p['title'].strip(".").replace("$", "$$")+"*.\\")
                out.append(p['author'].replace("D. Gerosa","**D. Gerosa**").strip(".")+".\\")
                line=""
                if p['link']:
                    line+='['
                if p['journal']:
                    line+=p['journal'].strip(".")
                if p['link']:
                    line+="]("+p['link']+")"
                if p['journal']:
                    line+=". "
                if 'erratum' in p.keys():
                    line+=" Erratum: "
                    if p['errlink']:
                        line+='['
                    if p['erratum']:
                        line+=p['erratum'].strip(".")
                    if p['errlink']:
                        line+="]("+p['errlink']+")"
                    line+='. '
 
                if p['arxiv']:
                    line+="["+p['arxiv'].strip(".")+"](https://arxiv.org/abs/"+p['arxiv'].split(":")[1].split(" ")[0].split(" ")[0]+")."
                out.append(line)
                if p['more']:
                    out[-1]+="\\"
                    out.append(p['more'].strip(".")+".")

                out = apply_journal_conversion(out)

                filename =f"temp/{today}-{slugify(p['title'])}.md"
                with open(filename,"w") as f: f.write("\n".join(out))
                print("--> Created blog post template:", filename)
                print("--> Please edit the file and move it to _posts/; requires manual intervention if there's latex in the title")



def parsetalks(talks,filename="parsetalks.tex"):

    print('Parse talks from database')

    out=[]
    out.append("Invited talks marked with *.")
    out.append("\\vspace{0.2cm}")
    out.append("")

    for k in ['conferences','seminars','lectures','posters','outreach']:
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
            out.append(p['what'].strip(".")+", "+p['where'].strip(".")+", "+p['when'].strip(".")+".")
            if p['more']:
                out.append("\\newline{}")
                out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
            out.append("\\vspace{0.05cm}\\\\")
            out.append("%")
            i=i-1
        out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))



def markdowntalks(talks, filename="_talks.md"):

    print('Markdown talk list for website')

    out = []
    out.append("Invited talks marked with ✦.")
    out.append("")
    out.append("## Summary")

    categories = ['conferences', 'seminars', 'lectures', 'posters', 'outreach']

    for k in categories:
        total = len(talks[k]['data'])
        invited = sum(1 for p in talks[k]['data'] if p.get("invited", False))
        label = "["+talks[k]['label']+"](#"+slugify(talks[k]['label'])+")"
        
        # Format like: 78 (34✦) Conferences
        summary_line = f"**{total}**"
        if invited > 0:
            summary_line += f" (**{invited}**✦)"
        summary_line += f" {label}"
        # Add continuation backslash except last category
        if k != categories[-1]:
            summary_line += " \\"
        out.append(summary_line)

    out.append("")
    out.append("---")
    out.append("")


    for k in categories:
        i = len(talks[k]['data'])

        if i >= 1:
            out.append(f"## {talks[k]['label']}")
            out.append("")

        for p in talks[k]['data']:
            mark = "✦ " if p.get("invited", False) else ""
            out.append(f"**{i}.** {mark}*{p['title'].strip('.')}*  \\\\")
            out.append(f"{p['what'].strip('.')}, {p['where'].strip('.')}, {p['when'].strip('.')}.")
            if p['more']:
                out[-1] += "  \\\\"
                more = re.sub(r'\\textbf{(.*?)}', r'\1', p['more'].strip("."))
                out.append(more + ".")

            out.append("")
            i -= 1

        out.append("")
        out.append("---")
        out.append("")

    with open(filename, "w") as f:
        f.write("\n".join(out))


import re

import re

def markdowngroup(group, filename="_group.md"):
    print('Markdown group list for website')

    out = []

    # Intro
    out.append("Here are the amazing people in my group. Come visit and chat science with us! If you're interested in joining, please check out the [jobs](/jobs) page.")
    out.append("")
    #out.append("<br>")
    #out.append("")
    out.append("## Current group members")

    # CURRENT MEMBERS
    merged_current = []

    for x in group['fellowships']['data']:
        if x.get("current", False) and x.get("bio"):
            merged_current.append({
                "name": x["name"].replace("~", " "),
                "role": x["fellowship"],
                "email": x.get("email", ""),
                "bio": x.get("bio", ""),
                "order": 0
            })
    for x in group['postdocs']['data']:
        if x.get("current", False) and x.get("bio"):
            merged_current.append({
                "name": x["name"].replace("~", " "),
                "role": "Postdoc",
                "email": x.get("email", ""),
                "bio": x.get("bio", ""),
                "order": 0
            })
    for x in group['phd']['data']:
        if x.get("current", False):
            merged_current.append({
                "name": x["name"].replace("~", " "),
                "role": "PhD student",
                "email": x.get("email", ""),
                "bio": x.get("bio", ""),
                "order": 1
            })

    merged_current = sorted(merged_current, key=lambda x: x["order"])

 #   for x in merged_current:
 #       out.append(f"**{x['name']}**  ")
 #       out.append(f"*{x['role']}*;  ")
 #       if x['email']:
 #           out[-1] += f"[{x['email']}](mailto:{x['email']})  "
 #       if x['bio']:
 #           out.append(f"{x['bio']}")
 #       out.append("")

    out.append("<div class=\"people-list\">")
    for x in merged_current:
        out.append(f"<div class=\"person\">")
        out.append(f"  <img src=\"{{{{ '/images/{slugify(x['name'])}.jpg' | relative_url }}}}\" alt=\"{x['name']}\" class=\"person-photo\">")
        out.append(f"  <div class=\"person-text\">")
        out.append(f"    <strong>{x['name']}</strong><br>")
        out.append(f"    {x['role']}<br>")
        if x['email']:        
            #out[-1] += f"[{x['email']}](mailto:{x['email']})  "
            #Link in html format
            out.append(f"<a href=\"mailto:{x['email']}\">{x['email']}</a><br>")
        if x['bio']:
            out.append(f"    <em>{x['bio']}</em>")
        out.append(f"  </div>") 
        out.append(f"</div>")
    out.append("</div>")


    # MSc and BSc current
    msc_current = [x for x in group['msc']['data'] if x.get("current", False)]
    bsc_current = [x for x in group['bsc']['data'] if x.get("current", False)]

    if msc_current or bsc_current:
        out.append("## Current MSc and Bsc students")
        out.append("Here are the amazing students who are currently completing research projects with us in the group… Taking the first fun steps into the perilous world of black holes!")
        out.append("")
        for x in msc_current:
            out.append(f"- **{x['name'].replace('~', ' ')}**, MSc thesis, {x['where']}, {x['year']}.")
        for x in bsc_current:
            out.append(f"- **{x['name'].replace('~', ' ')}**, BSc thesis, {x['where']}, {x['year']}.")
        out.append("")

    out.append("<br>")
    out.append("")
    out.append("---")
    #out.append("<br>")
    out.append("")

    # FORMER MEMBERS
    out.append("# Former group members")
    out.append("")
    out.append("...and here are those who passed through our group at some stage. Thank you all!")
    out.append("")

    def former_section(title, entries):
        if entries:
            out.append(f"## {title}")
            out.append("")
            for x in entries:
                line = f"- **{x['name']}**. {x['where']}, {x['years']}."
                then_fmt = format_then(x.get("note", ""))
                if then_fmt:
                    line += f" {then_fmt}"
                out.append(line)
            out.append("")

    def format_then(then_str):
        if not then_str:
            return ""
        then_str = re.sub(
            r'arXiv:(\d{4}\.\d{5})',
            r'[arXiv:\1](https://arxiv.org/abs/\1)',
            then_str.strip()
        )
        if then_str and not then_str.endswith('.'):
            then_str += '.'
        return then_str

    def extract_former_longterm(data):
        entries = []
        for x in data:
            if not x.get("current", False):
                start = str(x.get("start", ""))
                end = str(x.get("end", ""))
                years = f"{start}–{end}" if start and end else start or end
                entries.append({
                    "name": x["name"].replace("~", " "),
                    "where": x["where"],
                    "years": years,
                    "note": x.get("note", "")
                })
        return entries

    def extract_former_shortterm(data):
        entries = []
        for x in data:
            if not x.get("current", False):
                entries.append({
                    "name": x["name"].replace("~", " "),
                    "where": x["where"],
                    "years": str(x["year"]),
                    "note": x.get("note", "")
                })
        return entries

    former_fellowships = extract_former_longterm(group['fellowships']['data'])
    former_postdocs = extract_former_longterm(group['postdocs']['data'])
    former_phds = extract_former_longterm(group['phd']['data'])
    former_mscs = extract_former_shortterm(group['msc']['data'])
    former_bscs = extract_former_shortterm(group['bsc']['data'])

    former_section("Former postdocs", former_fellowships + former_postdocs)
    former_section("Former PhD students", former_phds)
    former_section("Former MSc students", former_mscs)
    former_section("Former BSc students", former_bscs)

    out.append("<br>")
    out.append("")
    out.append("---")
    out.append("")

    with open(filename, "w") as f:
        f.write("\n".join(out))



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
    out.append("\\textbf{"+str(len(papers['proceedings']['data']))+"} other publications (white papers, proceedings, etc.)")
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

    # including long-authorlist
    ads_citations = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in papers])
    inspire_citations = np.concatenate([[p['inspire_citations'] for p in papers[k]['data']] for k in papers])
    max_citations_including = np.maximum(ads_citations,inspire_citations)
    totalnumber_including = np.sum(max_citations_including)
    hind_including = hindex(max_citations_including)

    # excluding long-authorlist
    ads_citations = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in ['submitted','published']])
    inspire_citations = np.concatenate([[p['inspire_citations'] for p in papers[k]['data']] for k in ['submitted','published']])
    max_citations_excluding = np.maximum(ads_citations,inspire_citations)
    totalnumber_excluding = np.sum(max_citations_excluding)
    hind_excluding = hindex(max_citations_excluding)

    print("\tTotal number of citations:", totalnumber_including, totalnumber_excluding)
    print("\th-index:", hind_including, hind_excluding)
    out.append("Summary metrics reported using ADS and InSpire excluding [including] long-authorlist papers:")
    out.append("\\\\")
    out.append("\\textcolor{mark_color}{\\textbf{Total number of citations}}: >"+str(roundto100(totalnumber_excluding))+" [>"+str(roundto100(totalnumber_including))+"]")
    out.append(" --- ")
    out.append("\\textcolor{mark_color}{\\textbf{h-index}}: "+str(hind_excluding)+" ["+str(hind_including)+"].")
    out.append("\\\\")  
    out.append("\\textcolor{mark_color}{\\textbf{Web links to list services}}:")
    out.append("\href{https://davidegerosa.com/myads}{\\textsc{ADS}};")
    out.append("\href{https://davidegerosa.com/myinspire}{\\textsc{InSpire}};")
    out.append("\href{http://davidegerosa.com/myarxiv}{\\textsc{arXiv}};")
    out.append("\href{https://davidegerosa.com/myorcid}{\\textsc{ORCID}}.")

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

    plural = "s" if len(talks['lectures']['data'])>1 else ""

    out.append("(out of which \\textbf{"+str(np.sum(invited))+"} invited presentations),")
    out.append("\\textbf{"+str(len(talks['lectures']['data']))+"} lecture"+plural+" at PhD schools,")
    out.append("\\textbf{"+str(len(talks['outreach']['data']))+"} outreach talks.")

    out.append("\end{tabular} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def parsegroup(group,filename="parsegroup.tex"):

    print('Parse group from database')

    out=[]

    out.append("\cvitem{}{\\begin{tabular}{l@{\hspace{10pt}}c@{\hspace{4pt}}l@{\hspace{4pt}}c@{\hspace{3pt}}l}")

    for k in ['fellowships','postdocs','phd','msc','bsc']:
        overall = len(group[k]['data'])
        current = np.sum([x['current'] for x in group[k]['data']])
        #if current>0:
        #    currentlabel = "(of which \\textbf{"+str(current)+"} &currently in my group)"
        #else:
        #    currentlabel = "&"
        if current>0:
            out.append("\\textbf{"+group[k]['labelshort']+"}: & \\textbf{"+str(overall)+"} & so far (of which &\\textbf{"+str(current)+"}& currently in my group). \\\\")
        if current==0:
            out.append("\\textbf{"+group[k]['labelshort']+"}: & \\textbf{"+str(overall)+"} & so far. \\\\")
    out.append("\end{tabular} }")
    
    out.append("\\vspace{0.2cm}")
    out.append("")
    out.append("Current group members marked with *.  More information at \href{http://www.davidegerosa.com/group}{\\texttt{www.davidegerosa.com/group}}")

    def current(x):
        if x['current']:
            return "*"
        else:
            return ""
    def name(x):
        return "\\textit{"+x['name'].replace(" ","~")+"}"

    for k in ['fellowships','postdocs','phd','msc','bsc']:
        out.append("")
        out.append("\\vspace{0.2cm}")
        out.append("\\textbf{"+group[k]['labellong']+":}")
        out.append("")

        if k=="fellowships":
            for x in group[k]['data']:
                out.append("\\cvitemwithcomment{}{\hspace{0.4cm}$\circ\;$ "+name(x)+" ("+x['where']+", "+x['fellowship']+")."+current(x)+"}{"+x['start']+"-"+x['end']+"}")    
                out.append("\\vspace{-0.1cm}")
                
        elif k in ["postdocs","phd"]:
            for x in group[k]['data']:
                out.append("\\cvitemwithcomment{}{\hspace{0.4cm}$\circ\;$ "+name(x)+" ("+x['where']+")."+current(x)+"}{"+x['start']+"-"+x['end']+"}")    
                out.append("\\vspace{-0.1cm}")
        elif k in ["msc","bsc"]:
            for x in group[k]['data']:
                line = "\\textit{"+nameinitial(x['name'])+"} ("+x['where']+", "+x['what']+", "+str(x['year'])+")"+current(x)
                if x==group[k]['data'][-1]:
                    line+='.'
                else:
                    line+=' --- '
                out.append(line)           

    with open(filename,"w") as f: f.write("\n".join(out))


# Declare the dictionary outside
journalconversion = {}
journalconversion['\prd'] = ["Physical Review D", "PRD"]
journalconversion['\prdrc'] = ["Physical Review D", "PRD"]
journalconversion['\prdl'] = ["Physical Review D", "PRD"]
journalconversion['\prl'] = ["Physical Review Letters", "PRL"]
journalconversion['\prr'] = ["Physical Review Research", "PRR"]
journalconversion['\mnras'] = ["Monthly Notices of the Royal Astronomical Society", "MNRAS"]
journalconversion['\mnrasl'] = ["Monthly Notices of the Royal Astronomical Society", "MNRAS"]
journalconversion['\cqg'] = ["Classical and Quantum Gravity", "CQG"]
journalconversion['\\aap'] = ["Astronomy & Astrophysics", "A&A"]
journalconversion['\\apj'] = ["Astrophysical Journal", "APJ"]
journalconversion['\\apjl'] = ["Astrophysical Journal", "APJ"]
journalconversion['\grg'] = ["General Relativity and Gravitation", "GRG"]
journalconversion['\lrr'] = ["Living Reviews in Relativity", "LRR"]
journalconversion['\\natastro'] = ["Nature Astronomy", "NatAstro"]
journalconversion['Proceedings of the International Astronomical Union'] = ["IAU Proceedigs", "IAU"]
journalconversion['Journal of Physics: Conference Series'] = ["Journal of Physics: Conference Series", "JoPCS"]
journalconversion['Journal of Open Source Software'] = ["Journal of Open Source Software", "JOSS"]
journalconversion['Astrophysics and Space Science Proceedings'] = ["Astrophysics and Space Science Proceedings", "AaSSP"]
journalconversion['Caltech Undergraduate Research Journal'] = ["Caltech Undergraduate Research Journal", "CURJ"]
journalconversion['Chapter in: Handbook of Gravitational Wave Astronomy, Springer, Singapore'] = ['Book contribution', 'book']
journalconversion['Rendiconti Lincei. Scienze Fisiche e Naturali'] = ['Rendiconti Lincei', 'Lincei']
journalconversion['Proceedings of the 57th Rencontres de Moriond'] = ['Moriond proceedings', 'Moriond']
journalconversion["arXiv e-prints"] = ["arXiv", "arXiv"]

def convertjournal(j):
    if j in journalconversion:
        return journalconversion[j]
    else:
        return [j, j]

def apply_journal_conversion(lines):
    converted = []
    # Sort tags by length descending
    sorted_tags = sorted(journalconversion.keys(), key=len, reverse=True)

    for line in lines:
        new_line = line
        for tag in sorted_tags:
            full_name, short_name = journalconversion[tag]
            if short_name == "book":
                continue  # Skip conversion for 'book'
            if tag in new_line:
                new_line = new_line.replace(tag, full_name)
        converted.append(new_line)
    return converted

# def citationspreadsheet(papers):

#     gc = gspread.service_account()
#     sh = gc.open("Citation count")

#     print('Write Google Spreadsheet: List')

#     spreaddata={}
#     spreaddata['first_author']=[]
#     spreaddata['ads_citations']=[]
#     spreaddata['inspire_citations']=[]
#     spreaddata['max_citations']=[]
#     spreaddata['title']=[]
#     spreaddata['journal']=[]
#     spreaddata['year']=[]
#     spreaddata['arxiv']=[]

#     for k in papers:
#         for p in papers[k]['data']:
#             spreaddata['first_author'].append(p['author'].split(",")[0].split(".")[-1].strip().replace("\`",""))
#             spreaddata['ads_citations'].append(p['ads_citations'])
#             spreaddata['inspire_citations'].append(p['inspire_citations'])
#             spreaddata['max_citations'].append(max(p['ads_citations'],p['inspire_citations']))
#             spreaddata['title'].append(p['title'])
#             if p['journal']:
#                 spreaddata['journal'].append(p['journal'].split("(")[0].replace("in press","").rstrip(" 0123456789.,") )
#             elif p['arxiv']:
#                 spreaddata['journal'].append('arXiv')
#             else:
#                 spreaddata['journal'].append("")
#             if p['journal'] == "PhD thesis":
#                 spreaddata['year'].append(2016)
#             elif p['journal'] and "(" in  p['journal'] and ")" in  p['journal']:
#                 spreaddata['year'].append(p['journal'].split("(")[-1].split(")")[0])
#             elif p['arxiv']:
#                 spreaddata['year'].append("20"+p['arxiv'].split(':')[1][:2])
#             else:
#                 spreaddata['year'].append()
#             if p['arxiv']:
#                 spreaddata['arxiv'].append(p['arxiv'].split(']')[0].split("[")[1])
#             else:
#                 spreaddata['arxiv'].append("None")
#     tot = len(spreaddata['title'])
#     for x in spreaddata:
#         assert(len(spreaddata[x]) == tot)

#     years = np.array([int(y) for y in spreaddata['year']])
#     max_cits = np.array(spreaddata['max_citations'])
#     # lexsort sorts by last key first, so we pass (years, max_cits)
#     ind = np.lexsort(( -years, -max_cits ))
#     for x in spreaddata:
#         spreaddata[x]=np.array(spreaddata[x])[ind]

#     worksheet = sh.worksheet("List")
#     worksheet.update("A3",np.expand_dims(np.arange(tot)+1,1).tolist())
#     worksheet.update("C3",np.expand_dims(spreaddata['first_author'],1).tolist())
#     worksheet.update("D3",np.expand_dims(spreaddata['year'],1).tolist())
#     worksheet.update("E3",np.expand_dims(spreaddata['title'],1).tolist())
#     worksheet.update("F3",np.expand_dims(spreaddata['ads_citations'],1).tolist())
#     worksheet.update("G3",np.expand_dims(spreaddata['inspire_citations'],1).tolist())
#     worksheet.update("H3",np.expand_dims(spreaddata['max_citations'],1).tolist())
#     worksheet.update("F2",str(np.sum(spreaddata['ads_citations'])))
#     worksheet.update("G2",str(np.sum(spreaddata['inspire_citations'])))
#     worksheet.update("H2",str(np.sum(spreaddata['max_citations'])))
#     worksheet.update("I2",str(hindex(spreaddata['max_citations'])))

#     print('Write Google Spreadsheet: Year')

#     singleyear=np.array(list(set(spreaddata['year'])))
#     journalcount = np.array([np.sum(spreaddata['year']==s) for s in singleyear])
#     ind = np.argsort(singleyear)
#     singleyear=singleyear[ind]
#     journalcount=journalcount[ind]

#     worksheet = sh.worksheet("Years")
#     worksheet.update("A2",np.expand_dims(np.array(singleyear),1).tolist())
#     worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())

#     print('Write Google Spreadsheet: Journals')

#     shortpub = [convertjournal(j)[1] for j in spreaddata['journal']]
#     singlepub = np.array([convertjournal(j)[1] for j in list(set(shortpub))])
#     journalcount = np.array([np.sum(np.array([convertjournal(j)[1] for j in shortpub])==s) for s in singlepub])

#     ind = np.argsort(journalcount)[::-1]
#     singlepub=singlepub[ind]
#     journalcount=journalcount[ind]

#     longjournals=[]
#     for s in singlepub:
#         for j in list(set(spreaddata['journal'])):
#             if convertjournal(j)[1]==s:
#                 longjournals.append(convertjournal(j)[0])
#                 break
#     # longpub=[]
#     # shortpub=[]
#     # for j in singlepub:
#     #     if j in journalconversion:
#     #         longpub.append(journalconversion[j][0])
#     #         shortpub.append(journalconversion[j][1])
#     #     else:
#     #         longpub.append(j)
#     #         shortpub.append(j)

#     worksheet = sh.worksheet("Journals")
#     worksheet.update("A2",np.expand_dims(np.array(longjournals),1).tolist())
#     worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())
#     worksheet.update("D2",np.expand_dims(np.array(singlepub),1).tolist())


#     print('Write Google Spreadsheet: arXiv')

#     singlearxiv=np.array(list(set(spreaddata['arxiv'])))
#     # Remove empty
#     singlearxiv=singlearxiv[singlearxiv!=""]
#     journalcount = np.array([np.sum(spreaddata['arxiv']==s) for s in singlearxiv])

#     ind = np.argsort(journalcount)[::-1]
#     singlearxiv=singlearxiv[ind]
#     journalcount=journalcount[ind]

#     worksheet = sh.worksheet("arXiv")
#     worksheet.update("A2",np.expand_dims(np.array(singlearxiv),1).tolist())
#     worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())



def markdowncitations(papers, output_file="_citations.md"):
    spreaddata = {
        'first_author': [],
        'ads_citations': [],
        'inspire_citations': [],
        'max_citations': [],
        'title': [],
        'journal': [],
        'year': [],
        'arxiv': [],
    }

    for k in papers:
        for p in papers[k]['data']:
            name = p['author'].split(",")[0].split(".")[-1].strip()
            name = name.replace("\\`o", "o'")
            name = name.replace("\\v{s}", "s")
            spreaddata['first_author'].append(name)
            spreaddata['ads_citations'].append(p['ads_citations'])
            spreaddata['inspire_citations'].append(p['inspire_citations'])
            spreaddata['max_citations'].append(max(p['ads_citations'], p['inspire_citations']))
            spreaddata['title'].append(p['title'])

            if p['journal']:
                spreaddata['journal'].append(p['journal'].split("(")[0].replace("in press", "").rstrip(" 0123456789.,"))
            elif p['arxiv']:
                spreaddata['journal'].append('arXiv')
            else:
                spreaddata['journal'].append("")

            if p['journal'] == "PhD thesis":
                spreaddata['year'].append("2016")
            elif p['journal'] and "(" in p['journal'] and ")" in p['journal']:
                spreaddata['year'].append(p['journal'].split("(")[-1].split(")")[0])
            elif p['arxiv']:
                spreaddata['year'].append("20" + p['arxiv'].split(':')[1][:2])
            else:
                spreaddata['year'].append("")

            if p['arxiv']:
                spreaddata['arxiv'].append(p['arxiv'])  # Keep full for now
            else:
                spreaddata['arxiv'].append("")

    # Sort by max citations
    years = np.array([int(y) for y in spreaddata['year']])
    max_cits = np.array(spreaddata['max_citations'])
    # lexsort sorts by last key first, so we pass (years, max_cits)
    ind = np.lexsort(( -years, -max_cits ))
    for x in spreaddata:
        spreaddata[x]=np.array(spreaddata[x])[ind]

    def hindex(citations):
        citations = np.sort(citations)[::-1]
        return max([i + 1 for i in range(len(citations)) if citations[i] >= i + 1] + [0])

    total_ads = np.sum(spreaddata['ads_citations'])
    total_inspire = np.sum(spreaddata['inspire_citations'])
    total_max = np.sum(spreaddata['max_citations'])
    h_idx = hindex(spreaddata['max_citations'])

    with open(output_file, "w") as f:
        # === Summary ===
        f.write("## Citation Summary\n\n")
        f.write(f"- **Total ADS citations**: {total_ads}\n")
        f.write(f"- **Total INSPIRE citations**: {total_inspire}\n")
        f.write(f"- **Total MAX citations**: {total_max}\n")
        f.write(f"- **h-index**: {h_idx}\n\n")

        # === Table: List ===
        f.write("## Paper list sorted by citation count\n\n")
        f.write("| # | Author | Year | Title | ADS | INSPIRE | MAX |\n")
        f.write("|---|--------|------|-------|-----|---------|-----|\n")
        for i in range(len(spreaddata['title'])):
            title = spreaddata['title'][i].replace("$", "$$")
            f.write(f"| **{i+1}** | {spreaddata['first_author'][i]} | {spreaddata['year'][i]} | {title} | "
                    f"{spreaddata['ads_citations'][i]} | {spreaddata['inspire_citations'][i]} | {spreaddata['max_citations'][i]} |\n")

        # === Table: Year stats ===
        f.write("\n## Papers per year\n\n")
        singleyear = sorted(set(spreaddata['year']))
        yearcount = [np.sum(spreaddata['year'] == y) for y in singleyear]

        f.write("| Year | Paper count |\n")
        f.write("|------|--------------|\n")
        for y, c in zip(singleyear, yearcount):
            f.write(f"| {y} | {c} |\n")

        # === Table: Journals ===
        f.write("\n## Papers per journal\n\n")
        shortpub = [convertjournal(j)[0] for j in spreaddata['journal']]
        singlepub = sorted(set(shortpub), key=lambda s: -shortpub.count(s))

        f.write("| Journal | Paper count |\n")
        f.write("|---------|--------------|\n")
        for s in singlepub:
            count = shortpub.count(s)
            f.write(f"| {s} | {count} |\n")

        # === Table: arXiv categories ===
        f.write("\n## Papers per arXiv category\n\n")
        arxiv = spreaddata['arxiv']
        arxiv = arxiv[arxiv != ""]

        def extract_category(arx):
            if '/' in arx:  # old format: gr-qc/0410123
                return arx.split('/')[0]
            elif ':' in arx:  # new format: arXiv:1901.00001 [astro-ph.HE]
                if '[' in arx:
                    return arx.split('[')[1].split(']')[0]
                else:
                    return "unknown"
            else:
                return "unknown"

        categories = np.array([extract_category(a) for a in arxiv])
        unique_cats = sorted(set(categories), key=lambda c: -np.sum(categories == c))

        f.write("| Category | Paper Count |\n")
        f.write("|----------|--------------|\n")
        for cat in unique_cats:
            f.write(f"| {cat} | {np.sum(categories == cat)} |\n")

    print(f"Markdown citation list for website")

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

            if p['ads'] != p['ads_found'] and p['ads_found'] not in ["","None"]:

                print("\tReplace:", p['ads'],"-->", p['ads_found'])

                # Update in database
                database = database.replace(p['ads'],p['ads_found'])
                # Remove from bib file
                publist = "@".join([b for b in publist.split("@") if p['ads'] not in b])


    with open('database.py', 'w') as f:
        f.write(database)

    with open('publist.bib', 'w') as f:
        f.write(publist)


# def makemap(talks, filename="map.html"):
#     import folium
#     from branca.element import Template, MacroElement
#     print("Making map")

#     #for k in talks:
#     #    print(k)

#     # Sample locations for each category
#     blue_locations = [
#         ("Statue of Liberty", 40.6892, -74.0445),
#         ("Golden Gate Bridge", 37.8199, -122.4783),
#     ]

#     yellow_locations = [
#         ("Great Pyramid of Giza", 29.9792, 31.1342),
#         ("Sydney Opera House", -33.8568, 151.2153),
#     ]

#     green_locations = [
#         ("Eiffel Tower", 48.8584, 2.2945),
#         ("Colosseum", 41.8902, 12.4922),
#     ]

#     # Create the map centered roughly on Europe
#     mymap = folium.Map(location=[20, 0], zoom_start=2)

#     # Add blue markers
#     for name, lat, lon in blue_locations:
#         folium.Marker(
#             location=(lat, lon),
#             popup=name,
#             tooltip=name,
#             icon=folium.Icon(color='blue', icon='')  # blue pin, no icon
#         ).add_to(mymap)

#     # Add yellow markers (use orange color for yellow-ish pin)
#     for name, lat, lon in yellow_locations:
#         folium.Marker(
#             location=(lat, lon),
#             popup=name,
#             tooltip=name,
#             icon=folium.Icon(color='orange', icon='')  # orange ~ yellow pin, no icon
#         ).add_to(mymap)

#     # Add green markers
#     for name, lat, lon in green_locations:
#         folium.Marker(
#             location=(lat, lon),
#             popup=name,
#             tooltip=name,
#             icon=folium.Icon(color='green', icon='')  # green pin, no icon
#         ).add_to(mymap)

#     # Create a legend with matching colors in the order: blue, yellow, green
#     legend_html = """
#     {% macro html(this, kwargs) %}
#     <div style="
#         position: fixed;
#         bottom: 50px;
#         left: 50px;
#         z-index: 9999;
#         background-color: white;
#         border: 2px solid grey;
#         padding: 10px 12px;
#         font-size: 14px;
#         line-height: 1.6;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
#         font-family: Arial, sans-serif;
#     ">
#         <b>Legend</b><br>
#         <span style="
#             display: inline-block;
#             width: 14px;
#             height: 14px;
#             background-color: #38aadd;
#             border-radius: 50%;
#             margin-right: 8px;
#             border: 1px solid #555;
#             vertical-align: middle;
#         "></span>
#         Blue Locations<br>
#         <span style="
#             display: inline-block;
#             width: 14px;
#             height: 14px;
#             background-color: #72b025;
#             border-radius: 50%;
#             margin-right: 8px;
#             border: 1px solid #555;
#             vertical-align: middle;
#         "></span>
#         Yellow Locations<br>
#         <span style="
#             display: inline-block;
#             width: 14px;
#             height: 14px;
#             background-color: #f69730;
#             border-radius: 50%;
#             margin-right: 8px;
#             border: 1px solid #555;
#             vertical-align: middle;
#         "></span>
#         Green Locations
#     </div>
#     {% endmacro %}
#     """

#     legend = MacroElement()
#     legend._template = Template(legend_html)
#     mymap.get_root().add_child(legend)

#     # Save to HTML file
#     mymap.save(filename)



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

def pushtowebsite():
    comment='updated from dgerosa/cv'
    os.system("cp _*.md "+relativepathwebsiterepo+"/_pages/")
    os.system("git -C "+relativepathwebsiterepo+" add -u")
    os.system("git -C "+relativepathwebsiterepo+" commit -m '"+comment+"'")
    os.system("git -C "+relativepathwebsiterepo+" push")


def publishgithub():
    from github_release import gh_release_create

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

    os.system("git pull") # This is to get new tags from github


def clean():
    os.system("rm -f .aux *.log *.out")


#####################################


if __name__ == "__main__":

    # Set testing=True to avoid API limit
    testing = False

    papers = ads_citations(papers,testing=testing)
    papers = inspire_citations(papers,testing=testing)

    parsepapers(papers)
    parsetalks(talks)
    metricspapers(papers)
    metricstalks(talks)
    parsegroup(group)
    buildbib()
    

    #For website
    markdownpapers(papers)
    markdowntalks(talks)
    markdowncitations(papers)   
    markdowngroup(group)
    #citationspreadsheet(papers)
    checkblogposts(papers)

    #makemap(talks)

    if not testing:
        replacekeys()
        builddocs()
        pushtogit()
        pushtowebsite()

        if os.getenv("GITHUB_ACTIONS") == "true": # Running inside GitHub Actions
            pass
        else:
            publishgithub()

    clean()