#!/bin/bash
#
# A collection script to get together a copy of all (relevant) Calc documents
# in one directory for simpler browsing. It can also concatenate all PDFs
# into one (rather useless) big file to demonstrate the glory amount of work
# done by writing all the stuff ;-)
#
# -- Sven 2014
#

# Remove all PDF files in this directory
rm *.pdf

# Link all PDF files sorted by human numbering (1,2,...,10,11,...)
find .. | grep 'calc[0-9]*.pdf' | sort -V | xargs -IK cp -v -s K .

# Rename natural numbers to 01..09
rename 's/([^\d])(\d).pdf$/${1}0$2.pdf/' *.pdf 

if type sejda >/dev/null 2>&1; then
	# Call sejda-console, if possible.
	# Sejda can preserve links and make a decent toc (cat all)
	echo "using sejda-console to merge PDFs (preserves links and toc)"
	sejda merge -d . -o calc-series.pdf
elif type pdftk >/dev/null 2>&1; then
	echo "using pdftk to merge PDFs (preserves links but not toc)"
	pdftk calc*.pdf cat output calc-series.pdf
elif type pdfunite >/dev/null 2>&1; then
	echo "using pdfunite to merge PDFs (hyperlinks will be broken)"
	pdfunite calc*.pdf calc-series.pdf
else
	echo "Found no tool to merge PDFs."
fi
