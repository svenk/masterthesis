#!/bin/bash

# go to root where thesis.tex resides
cd `dirname $0`/.. 

bibtex --include-directory="bibliography" build/thesis
