# Skrypt zapisujący wszystkie pliki z folderu CSS do jednego i usuwający komentarze
import re
from glob import glob
main_content = ""
files = glob("css/*.css")
files.sort()
def removeComments(string):
	string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string)
	return string
for file_name in files:
	f = open(file_name, "r")
	new_content = ""
	for line in f:
		new_content = new_content + removeComments(line)
	main_content = main_content + new_content
	f.close()
main = open("main.css", "w+")
main.write(main_content)
main.close()
main_ff = open("main_ff.css", "w+")
new_content = main_content.split("\n")
main_content = []
for line in new_content:
	main_content.append("\t" + line + "\n")
main_content = "".join(main_content)
main_content = "@namespace url(http://www.w3.org/1999/xhtml);\n@-moz-document domain(\"forum.jarock.pl\") {" + main_content + "}"
main_ff.write(main_content)
main_ff.close()
