End of Year Report
==================

This is the LaTeX source for my 'long' end-of-year report for the first year of
my PhD.  The report is aimed at 'general' computer scientists and aims to give
some context for the work I'm doing and suggest where things may end up going.

This document is a work in progress. You have been warned.

Build
-----

This expects my bibtex database to be copied/symlinked to report.bib.

	mkdir -p tikzcache
	pdflatex -shell-escape report.tex
	bibtex report
	pdflatex -shell-escape report.tex
	pdflatex -shell-escape report.tex

The following (possibly less-standard) LaTeX libraries are required:

* TikZ
* Tikz3D (Part of Tex-SX http://bazaar.launchpad.net/~tex-sx/tex-sx/development/files)

In addition, Python 2 is required to generate some of the figures.
