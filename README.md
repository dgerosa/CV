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

- Fetch citations from [ADS](https://davidegerosa.com/myads) and [INSPIRE](https://davidegerosa.com/myinspire).
- Put together papers and talks in tex format.
- Fetch full bibtex record from [ADS](https://davidegerosa.com/myads) for a `.bib` file.
- Create markdown pages `_*.md` for a Jekyll website like [my own](https://davidegerosa.com).
- Sanitize the database if the ADS key changed.
- Push to git

Then there's a github action `.github/workflows/CV_website.yml` that:

- Compile full CV, short CV, standalone publication list, standalone presentation list.
- Publish a [Github release](https://github.com/dgerosa/CV/releases) to get permanent URLs.
- Push updates to the [CV repo](https://github.com/dgerosa/CV) if any.
- Push updates to the [website repo](https://github.com/dgerosa/website) if any (from there, another action will publish the website itself).

At the end of the day: you change something and then type
```shell
python makeCV.py "commit message"
```
