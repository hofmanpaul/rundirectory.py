import os
import subprocess
import sys
origWD = os.getcwd()

statalocwin="C:/Program Files (x86)/Stata13/StataMP-64.exe"
statalocmac="/Applications/Stata/StataMP.app/Contents/MacOS/stata-mp"
print("Wait for the message 'DONE' to show up. The Stata dofile run in the background so it might seem like the program is finished when it isn't")

def parse_location(fileloc):
	filepath = fileloc.split("/")
	script = filepath[-1]
	scriptdir = "/".join(filepath[0:-1])
	return script, scriptdir

def run_stata(fileloc):
	"""Run stata dofile in batch mode, deletes the log file and fix the working directory"""
	script, scriptdir = parse_location(fileloc)
	os.chdir(scriptdir)
	if sys.platform == "win32":
		subprocess.call([statalocwin, "-e", "do", script])
	else:
		subprocess.call([statalocmac, "-b", "do", script])
	os.remove("{}.log".format(script[0:-3]))
	os.chdir(origWD)

def run_python(fileloc):
	"""Run Python script and fix the working directory"""
	script, scriptdir = parse_location(fileloc)
	os.chdir(scriptdir)
	subprocess.call(["python", script])  
	os.chdir(origWD)

def run_R(fileloc):
	"""Run R script and fix the working directory"""
	script, scriptdir = parse_location(fileloc)
	os.chdir(scriptdir)
	subprocess.call(["Rscript", "--vanilla", script])
	os.chdir(origWD)

def run_latex(fileloc):
	"""Run a Tex script, run bibtex and then the Tex script twice more. Then fix the working directory"""
	script, scriptdir = parse_location(fileloc)
	os.chdir(scriptdir)
	subprocess.call(["pdflatex", script])
	subprocess.call(["bibtex", script[0:-4] ])
	subprocess.call(["pdflatex", script])
	subprocess.call(["pdflatex", script])
	os.chdir(origWD)

run_python("01_Data/01_Raw/merge.py")

run_R("01_Data/02_Clean/graphing.r")

run_stata("01_Data/02_Clean/analysis.do")

run_latex("03_Paper/Paper.tex")

#Clean up intermediate files
os.remove("01_Data/02_Clean/appended.csv")
os.remove("02_Output/balance.jpg")
os.remove("02_Output/results.tex")
os.remove("03_Paper/Paper.aux")
