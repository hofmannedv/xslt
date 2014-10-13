#!/bin/bash

# step 1: adjust given input file quelle.xml
python transform.py quelle.xml output.xml

# step 2: transform output.xml to output.xml via xslt transformation
xsltproc -o ausgabe.xml transform.xsl output.xml

# step 3: pretty-print output xml
cat ausgabe.xml | xmllint --format --output ausgabe2.xml -

# step 4: create docbook from output.xml
docbook2pdf ausgabe2.xml
