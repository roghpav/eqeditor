'''
Latex equation maker
esample:

$python ltxeq.py -e "2x=\pi+c\rho" -o "equation"

Author: Pavel Figueroa
email: figueroa.pav@gmail.com


'''


import os
import argparse

from tkdocviewer import *
from tkinter import *

def showequation(fname):
	win= Tk()
	win.geometry("400x150")
	v = DocViewer(win)
	v.pack(side="top", expand=1, fill="both")
	v.display_file(fname)

	win.mainloop()


def mk_eq(eq, fname = 'eqtem', show = True ):
	fileA = open(fname+'.tex', "w")
	str_0 = '\\documentclass[border=1pt]{standalone} \n\\usepackage{amsmath} \n\\usepackage{graphicx} \n\\usepackage{physics} \n\\usepackage{amsmath,amsfonts} \n\\begin{document} \n\\scalebox{5}{  \n$\\displaystyle \n'
	str_1 = '\n$}\n\\end{document}'
	fileA.write(str_0+eq+str_1)
	fileA.close()
	os.system('latex '+fname+'.tex'+ ' --file-line-error --synctex=1')
	os.system('dvipdfm '+fname+'.dvi') #dvi to pdf
	if show == True:
		showequation(fname+'.pdf')


def main():
	parser = argparse.ArgumentParser(description='Latex equation maker \n $python ltxeq.py -e "2x=\pi+c" -o "equation"')
	parser.add_argument("-e", "--equation", help="Equation in latex format")
	parser.add_argument("-o", "--output", help="Name of ouput file, equation will be saved in pdf format")

	args = parser.parse_args()

	if not (args.equation==None):
		print(f'Render equation: {args.equation}')
		eq = f'{args.equation}'
		if not (args.output==None):
			mk_eq(eq, fname=args.output)
		else:
			mk_eq(eq)
	else:
		print(f'Enter an equation')

if __name__ == '__main__':
	main()