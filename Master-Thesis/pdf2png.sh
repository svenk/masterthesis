#!/bin/bash

# for OpenOffice: PDFs als PNGs machen

mkdir -p png-figures

for f in figures/*.pdf; do
	b=$(basename "$f" .pdf);
	echo
	echo "Converting $f => $b.png"
	convert -verbose -density 150 -trim "$f" -quality 100 -sharpen 0x1.0 png-figures/$b.png
done;

echo "done"
