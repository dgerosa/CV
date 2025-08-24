def checkinternet():
    url = "http://www.google.com"
    timeout = 5
    connected = True
    try:
	    requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
	    connected = False
    return connected




    #path = os.path.expandvars('$HOME/reps/dotfiles/adstoken.txt')
    #with open(path) as f:
    #    $ads.config.token = f.read()
    #    #token = f.read()

    # from requests.adapters import HTTPAdapter
    # from urllib3.util.retry import Retry

    # session = requests.Session()
    # session.headers.update({'Authorization': f'Bearer {token}'})

    # retry = Retry(total=5, backoff_factor=0.3, status_forcelist=[500,502,503,504])
    # adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    # session.mount('http://', adapter)
    # session.mount('https://', adapter)
	


                                    #with warnings.catch_warnings():
                                    #warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host")
                                    #r = requests.get("https://api.adsabs.harvard.edu/v1/search/query?q="+p['ads'].replace("&","%26")+"&fl=citation_count,bibcode",headers={'Authorization': 'Bearer ' + token},verify=False)
                                    # url = "https://api.adsabs.harvard.edu/v1/search/query?q=" + p['ads'].replace("&", "%26") + "&fl=citation_count,bibcode"
                                    # r = session.get(url, verify=False, timeout=10)
                                #q= r.json()['response']['docs']
                                #if len(q)!=1:
                                #    raise ValueError("ADS error in "+b)
                                
                                # query = p['ads'].replace("&", "%26")
                                # url = f"https://api.adsabs.harvard.edu/v1/search/query?q={query}&fl=citation_count,bibcode"
                                # req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
                                # with urllib.request.urlopen(req, context=None) as response:
                                #     q = response.read().decode('utf-8')
                                # q= json.loads(q)

                                # if int(q['response']["numFound"])!=1:
                                #     raise ValueError("ADS error in "+b)

                                # citation_count=int(q['response']['docs'][0]['citation_count'])

                                #p['ads_found'] = q['bibcode']
                                #q['response']['docs'][0]['bibcode']
								


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

    years = np.array([int(y) for y in spreaddata['year']])
    max_cits = np.array(spreaddata['max_citations'])
    # lexsort sorts by last key first, so we pass (years, max_cits)
    ind = np.lexsort(( -years, -max_cits ))
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




def makemap(talks, filename="map.html"):
    import folium
    from branca.element import Template, MacroElement
    print("Making map")

    #for k in talks:
    #    print(k)

    # Sample locations for each category
    blue_locations = [
        ("Statue of Liberty", 40.6892, -74.0445),
        ("Golden Gate Bridge", 37.8199, -122.4783),
    ]

    yellow_locations = [
        ("Great Pyramid of Giza", 29.9792, 31.1342),
        ("Sydney Opera House", -33.8568, 151.2153),
    ]

    green_locations = [
        ("Eiffel Tower", 48.8584, 2.2945),
        ("Colosseum", 41.8902, 12.4922),
    ]

    # Create the map centered roughly on Europe
    mymap = folium.Map(location=[20, 0], zoom_start=2)

    # Add blue markers
    for name, lat, lon in blue_locations:
        folium.Marker(
            location=(lat, lon),
            popup=name,
            tooltip=name,
            icon=folium.Icon(color='blue', icon='')  # blue pin, no icon
        ).add_to(mymap)

    # Add yellow markers (use orange color for yellow-ish pin)
    for name, lat, lon in yellow_locations:
        folium.Marker(
            location=(lat, lon),
            popup=name,
            tooltip=name,
            icon=folium.Icon(color='orange', icon='')  # orange ~ yellow pin, no icon
        ).add_to(mymap)

    # Add green markers
    for name, lat, lon in green_locations:
        folium.Marker(
            location=(lat, lon),
            popup=name,
            tooltip=name,
            icon=folium.Icon(color='green', icon='')  # green pin, no icon
        ).add_to(mymap)

    # Create a legend with matching colors in the order: blue, yellow, green
    legend_html = """
    {% macro html(this, kwargs) %}
    <div style="
        position: fixed;
        bottom: 50px;
        left: 50px;
        z-index: 9999;
        background-color: white;
        border: 2px solid grey;
        padding: 10px 12px;
        font-size: 14px;
        line-height: 1.6;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        font-family: Arial, sans-serif;
    ">
        <b>Legend</b><br>
        <span style="
            display: inline-block;
            width: 14px;
            height: 14px;
            background-color: #38aadd;
            border-radius: 50%;
            margin-right: 8px;
            border: 1px solid #555;
            vertical-align: middle;
        "></span>
        Blue Locations<br>
        <span style="
            display: inline-block;
            width: 14px;
            height: 14px;
            background-color: #72b025;
            border-radius: 50%;
            margin-right: 8px;
            border: 1px solid #555;
            vertical-align: middle;
        "></span>
        Yellow Locations<br>
        <span style="
            display: inline-block;
            width: 14px;
            height: 14px;
            background-color: #f69730;
            border-radius: 50%;
            margin-right: 8px;
            border: 1px solid #555;
            vertical-align: middle;
        "></span>
        Green Locations
    </div>
    {% endmacro %}
    """

    legend = MacroElement()
    legend._template = Template(legend_html)
    mymap.get_root().add_child(legend)

    # Save to HTML file
    mymap.save(filename)




        if os.getenv("GITHUB_ACTIONS") == "true": # Running inside GitHub Actions
            pass
        else:
            pushtogit()
            pushtowebsite()
            publishgithub()


#import gspread

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context




def pdflatex(filename):
    os.system('pdflatex '+filename+' >/dev/null')
    #os.system('pdflatex '+filename)


def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

def builddocs():

    print("Update CV")
    pdflatex("CV")

    print("Update publist")
    pdflatex("publist")

    print("Update talklist")
    pdflatex("talklist")

    print("Update CVshort")
    pdflatex("CVshort")



#### Latex and git things ####

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
    os.system("git -C "+relativepathwebsiterepo+" pull")
    os.system("git -C "+relativepathwebsiterepo+" add -u")
    os.system("git -C "+relativepathwebsiterepo+" commit -m '"+comment+"'")
    os.system("git -C "+relativepathwebsiterepo+" push")

def copyfiles():
    os.system("cp _*.md "+relativepathwebsiterepo+"/_pages/")
    shutil.copy2("CV.pdf", "DavideGerosa_fullCV.pdf")
    shutil.copy2("CVshort.pdf", "DavideGerosa_shortCV.pdf")
    shutil.copy2("publist.pdf", "DavideGerosa_publist.pdf")
    shutil.copy2("publist.bib", "DavideGerosa_publist.bib")
    shutil.copy2("talklist.pdf", "DavideGerosa_talklist.pdf")

def publishgithub():
    from github_release import gh_release_create

    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    print("Publish github release:", date)

    # Create a github token, see:
    # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    # Make sure a GITHUB_TOKEN variable is part of the environment variables

    gh_release_create("dgerosa/CV", date, publish=True, name=date, asset_pattern="DavideGerosa_*")

    os.system("git pull") # This is to get new tags from github


def clean():
    os.system("rm -f *.aux *.log *.out")



    # Latex and git things
    builddocs()
    copyfiles()
    pushtowebsite()
    pushtogit()
    publishgithub()
    clean()