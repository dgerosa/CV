from __future__ import print_function
import sys,os

##########
print("Read CV")

file = open('CV.tex', 'r')
CV = file.read()
file.close()

os.system('pdflatex CV >/dev/null')

##########
print("Update talklist")

file = open('talklist.tex', 'r')
talklist = file.read()
file.close()

talklist = "%mark_intro".join([talklist.split("%mark_intro")[0],CV.split("%mark_intro")[1],talklist.split("%mark_intro")[2]])
talklist = "%mark_talknumbers".join([talklist.split("%mark_talknumbers")[0],CV.split("%mark_talknumbers")[1],talklist.split("%mark_talknumbers")[2]])
talklist = "%mark_talklist".join([talklist.split("%mark_talklist")[0],CV.split("%mark_talklist")[1],talklist.split("%mark_talklist")[2]])

file = open('talklist.tex', 'w')
file.write(talklist)
file.close()

os.system('pdflatex talklist >/dev/null')

##########
print("Update publist")

file = open('publist.tex', 'r')
publist = file.read()
file.close()

publist = "%mark_intro".join([publist.split("%mark_intro")[0],CV.split("%mark_intro")[1],publist.split("%mark_intro")[2]])
publist = "%mark_pubnumbers".join([publist.split("%mark_pubnumbers")[0],CV.split("%mark_pubnumbers")[1],publist.split("%mark_pubnumbers")[2]])
publist = "%mark_publist".join([publist.split("%mark_publist")[0],CV.split("%mark_publist")[1],publist.split("%mark_publist")[2]])

file = open('publist.tex', 'w')
file.write(publist)
file.close()

os.system('filltex publist >/dev/null') # Note filltex to get the bibliography right

##########
print("Bibbase bibliography")

file= open('publist.bib', 'r')
biblio = file.read()

# Conversion from ADS to whatever I want in bibbase
biblio = biblio.replace('\mnras', 'Monthly Notices of the Royal Astronomical Society')
biblio = biblio.replace('\mnrasl', 'Monthly Notices of the Royal Astronomical Society Letters')
biblio = biblio.replace('\prd', 'Physical Review D')
biblio = biblio.replace('\prl', 'Physical Review Letters')
biblio = biblio.replace('\cqg', 'Classical and Quantum Gravity')

file = open('publist.bib', 'w')
file.write(biblio)
file.close()

##########
print("Update shortCV")

CVshort = "%mark_short".join([CV.split("%mark_short")[0],CV.split("%mark_short")[2]])

file = open('CVshort.tex', 'w')
file.write(CVshort)
file.close()

os.system('pdflatex CVshort >/dev/null')


##########
print("Update transcript")

file = open('transcript.tex', 'r')
transcript = file.read()
file.close()

transcript = "%mark_intro".join([transcript.split("%mark_intro")[0],CV.split("%mark_intro")[1],transcript.split("%mark_intro")[2]])

file = open('transcript.tex', 'w')
file.write(transcript)
file.close()

os.system('pdflatex transcript >/dev/null')
##########

print("Cleaning...")
os.system('rm *aux *bbl *blg *out *log *synctex.gz')

print("Done!")
