#!/bin/bash


# only read, do not write.
tex="thesis.tex"

function cecho { echo -e "\e[32m$@\e[0m"; }

cecho "> Testing figures"

for f in figures/*; do

	grep $f $tex > /dev/null
	texfound=$?
	if [ $texfound != '0' ]; then
		echo "$f not used in thesis"
	fi
done

