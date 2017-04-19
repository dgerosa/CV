
mark='%CV_long'

file = open('CV.tex', 'r')
CV = file.read()
file.close()

file = open('publist.tex', 'r')
publist = file.read()
file.close()

file = open('talklist.tex', 'r')
talklist = file.read()
file.close()

CV.replace("\textbf{Full list of publications} available at", "\textbf{Full list of publications} available below and at")
CV.replace("\textbf{Full list of presentations} available at", "\textbf{Full list of presentations} available below and at")

file = open('CVlong.tex', 'w')
file.write(CV.split(mark)[0])

file.write("\n \pagebreak")
file.write("\n \\section{Full publication list}\\vspace{0.2cm} \n ")
file.write(publist.split(mark)[1])
file.write("\n \\section{Full presentation list}\\vspace{0.2cm} \n ")

file.write(talklist.split(mark)[1])
file.write("\n \\end{document}")
file.close()
