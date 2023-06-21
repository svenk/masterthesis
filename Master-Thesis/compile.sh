#!/bin/bash
# TeXLive 2014

# call "./compile.sh release" to make a copy with timestamp + compression.

set -e
cd `dirname $0`

# bibtex style files
# http://tex.stackexchange.com/questions/120427/where-should-i-put-the-bib-file-to-use-it-directly-in-bibliographybibfile
export BSTINPUTS=".;$(pwd)/bibliography"

# BIBINPUTS ginge auch

LATEX="pdflatex --synctex=1 --output-directory=build -interaction=nonstopmode"

# clean build
[ -e build/* ] && rm -v build/*

$LATEX thesis && echo "-- success at running latex run 1"
bibtex build/thesis && echo "-- success at running bibtex"
$LATEX thesis && echo "-- success at running latex run 2"
$LATEX thesis && echo "-- success at running latex run 3"

if [ "$1" == "release" ]; then

# copy and compress a release
TIME=$(date "+%F-T-%R" | tr ':' '-')
SOURCE="build/thesis.pdf"
TARGET="release/master-thesis-$TIME.pdf"
COMPR="${TARGET%.*}-compressed.pdf"

echo "Releasing as $TARGET"
cp $SOURCE $TARGET

echo "Compressing..."
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.7 -dNOPAUSE -dQUIET -dBATCH  \
   -sOutputFile=$COMPR $TARGET

optsize=$(stat -c "%s" $COMPR)
orgsize=$(stat -c "%s" $TARGET)
bytesSaved=$(expr $orgsize - $optsize)
percent=$(expr $optsize '*' 100 / $orgsize)
echo Saving $bytesSaved bytes \(now ${percent}% of old\)
echo Compressed file at $COMPR

fi

