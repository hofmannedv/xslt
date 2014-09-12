#!/bin/bash

# transform input.xml to output.xml via xslt transformation
xsltproc -o ausgabe.xml transform.xsl quelle.xml

# pretty-print output xml
cat ausgabe.xml | xmllint --format --output ausgabe2.xml -

# create docbook from output.xml
