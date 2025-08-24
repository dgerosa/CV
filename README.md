# Davide Gerosa, CV
Here is where I keep my (hopefully updated) CV, publication list, talks, etc.

For more information on my research, please visit my personal homepage: [davidegerosa.com](https://davidegerosa.com)

Pdf files can be accessed using the links below:

- [**Full CV**](https://github.com/dgerosa/CV/releases/latest/download/DavideGerosa_fullCV.pdf)
- [**Short CV**](https://github.com/dgerosa/CV/releases/latest/download/DavideGerosa_shortCV.pdf)
- [**Publication list**](https://github.com/dgerosa/CV/releases/latest/download/DavideGerosa_publist.pdf)
- [**Talk list**](https://github.com/dgerosa/CV/releases/latest/download/DavideGerosa_talklist.pdf)

Additionally, my citation count is available [here](https://davidegerosa.com/citations).



### My CV and website workflow

This is how I handle it. 

The only files one needs to change are `database.py` and `CV.tex`. Everything else is machine-generated.

- Add new papers, talks, and students in `database.py` in the same format as the others. The order is important.
- Touch the other things in the CV directly in `CV.tex`.
- Tags `%mark_CVshort` indicate what to exclude when building the short version of the CV.

Then run `makeCV.py`:

- Fetch citations from [ADS](https://ui.adsabs.harvard.edu/search/filter_bibstem_facet_fq_bibstem_facet=NOT&filter_bibstem_facet_fq_bibstem_facet=*%3A*&filter_bibstem_facet_fq_bibstem_facet=bibstem_facet%3A%22cosp%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq=%7B!type%3Daqp%20v%3D%24fq_bibstem_facet%7D&fq_bibstem_facet=(*%3A*%20NOT%20bibstem_facet%3A%22cosp%22)&fq_doctype=(doctype%3A%22misc%22%20OR%20doctype%3A%22inproceedings%22%20OR%20doctype%3A%22article%22%20OR%20doctype%3A%22eprint%22)&p_=0&q=%20author%3A%22Gerosa%2C%20Davide%22&sort=citation_count%20desc%2C%20bibcode%20desc) and [INSPIRE](https://inspirehep.net/literature?sort=mostcited&size=25&page=1&q=exactauthor%3AD.Gerosa.1).
- Put together a papers and talks list in tex format (`parsepapers.tex`  and `parsetalks.tex`).
- Compute some basic indicators like h-index, etc (`metricspapers.tex`  and `metricstalks.tex`).
- Fetch bibtex record from  [ADS](https://ui.adsabs.harvard.edu/search/filter_bibstem_facet_fq_bibstem_facet=NOT&filter_bibstem_facet_fq_bibstem_facet=*%3A*&filter_bibstem_facet_fq_bibstem_facet=bibstem_facet%3A%22cosp%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq=%7B!type%3Daqp%20v%3D%24fq_bibstem_facet%7D&fq_bibstem_facet=(*%3A*%20NOT%20bibstem_facet%3A%22cosp%22)&fq_doctype=(doctype%3A%22misc%22%20OR%20doctype%3A%22inproceedings%22%20OR%20doctype%3A%22article%22%20OR%20doctype%3A%22eprint%22)&p_=0&q=%20author%3A%22Gerosa%2C%20Davide%22&sort=citation_count%20desc%2C%20bibcode%20desc) (`publist.bib `). This is useful for services like [bibbase](https://davidegerosa.com/bibbase).
- Create markdown pages `_*.md` for a Jekyll website like my own [davidegerosa.com](https://davidegerosa.com/citations).
- Sanitize the database if the ADS key changed.
- Build the full CV with publication and presentation lists (`CV.tex`).
- Push to git

Then there's a github action `.github/workflows/CV_website.yml` that:

- Compile full CV, short CV, standalone publication list, presentation list.
- Publish [Github releases](https://github.com/dgerosa/CV/releases) to get permanent URLs.
- Push updates to the [CV repo](https://github.com/dgerosa/CV) if any.
- Push updates to the [website repo](https://github.com/dgerosa/website) if any (from there, another action will publish the website itself).

At the end of the day: you change something and then type
```shell
python makeCV.py "commit messsage"
```
