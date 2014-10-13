# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import sys
import os
from lxml import etree
from copy import deepcopy

# usually call it like that:
# python transform.py source.xml output.xml

def createWordNode(nodeType, nodeValue):
	# create word node
	wordNode = etree.Element("wrd")
	
	if (nodeType == "pt-lexGloss"):
		# create gloss node
		contentNodeName = "gloss"
	else:
		# create language data node
		contentNodeName = "langData"

	# add language attribute with content
	contentNode = etree.Element(contentNodeName, lang=nodeType)
		
	# add node value
	contentNode.text = nodeValue

	# add content node as a child to wordNode
	wordNode.append(contentNode)

	return wordNode

def createBaselineNode (nodeValue):
	return createWordNode("wca-baseline", nodeValue)

def createMorphemeNode (nodeValue):
	return createWordNode("wca-morpheme", nodeValue)

def createLexGlossNode (nodeValue):
	return createWordNode("pt-lexGloss", nodeValue)

def analyzeLineGroup(lineGroupNode):

	# extract lines from the given node
	line1, line2, line3 = lineGroupNode
	#print(etree.tostring(lineGroupNode, pretty_print=True))

	# assume that the output node is empty
	lineGroupNodeList = []

	# count the columns for the table
	columns = len(line1)
	print "%i columns" % columns

	# case #1: exact number of columns as desired
	if columns == 5:
		print "keep line as is"
		# return the lineGroupNode unchanged
		lineGroupNodeList = [lineGroupNode]

	# case #2: less number of columns
	if columns < 5:
		# calculate the number of columns to add
		remainingColumns = 5 - columns
		print "adding %i further column(s) " % remainingColumns

		while remainingColumns:
			# create entry for line 1
			line1.append (createBaselineNode(""))
			# create entry for line 2
			line2.append (createMorphemeNode(""))
			# create entry for line 3
			line3.append (createLexGlossNode(""))
			remainingColumns = remainingColumns - 1
		
		# rebuild the lineGroup node
		lineGroupNode = etree.Element("lineGroup")
		lineGroupNode.append(line1)
		lineGroupNode.append(line2)
		lineGroupNode.append(line3)

		# return the lineGroup node with the added columns
		lineGroupNodeList = [lineGroupNode]

	# case #3: a higher number of columns than desired
	if columns > 5:
		lineBreaks = columns / 5
		print "adding %i linebreak(s) " % lineBreaks
		
		remainingColumns = 10 - columns
		print "adding %i further column(s) " % remainingColumns

		while remainingColumns:
			# create entry for line 1
			line1.append (createBaselineNode(""))
			# create entry for line 2
			line2.append (createMorphemeNode(""))
			# create entry for line 3
			line3.append (createLexGlossNode(""))
			remainingColumns = remainingColumns - 1

		# count line1
		columns = len(line1)
		print "new column count: %i" % columns

		# rebuild node 1
		lineGroupNode1 = etree.Element("lineGroup")
		newLine1 = etree.SubElement(lineGroupNode1, "line")
		newLine2 = etree.SubElement(lineGroupNode1, "line")
		newLine3 = etree.SubElement(lineGroupNode1, "line")

		# add the first five columns
		for i in range(5):
			newLine1.append(deepcopy(line1[i]) )
			newLine2.append(deepcopy(line2[i]) )
			newLine3.append(deepcopy(line3[i]) )
			# print "column %i: %s" % (i, line1[i].tag)

		# rebuild node 2
		lineGroupNode2 = etree.Element("lineGroup")
		newLine1 = etree.SubElement(lineGroupNode2, "line")
		newLine2 = etree.SubElement(lineGroupNode2, "line")
		newLine3 = etree.SubElement(lineGroupNode2, "line")

		# add the remaining five columns
		for i in range(5,10):
			newLine1.append(deepcopy(line1[i]) )
			newLine2.append(deepcopy(line2[i]) )
			newLine3.append(deepcopy(line3[i]) )
			# print "column %i: %s" % (i, line1[i].tag)

		print(etree.tostring(lineGroupNode1, pretty_print=True))
		print(etree.tostring(lineGroupNode2, pretty_print=True))

		lineGroupNodeList = [lineGroupNode1, lineGroupNode2]

	return lineGroupNodeList

# read source and output file from command line
if (len(sys.argv) == 3):
	sourceFile = sys.argv[1]
	outputFile = sys.argv[2]
else:
	# command line error with arguments
	print ("error: incorrect command line arguments given")
	print ("exiting.")
	exit (1)

# basic verify command line arguments
if (sourceFile == ""):
	print ("error: no source file name given")
	print ("exiting.")
	exit (1)

if (outputFile == ""):
	print ("error: no output file name given")
	print ("exiting.")
	exit (1)

# read xml source file
doc = etree.parse(sourceFile)

newDoc = etree.XML('''\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN" "../docbook-xml-4.5/docbookx.dtd">

<lingPaper automaticallywrapinterlinears="yes">
</lingPaper>
''')

# read document structure
lingPaper = doc.getroot()
newLingPaper = etree.XML('<lingPaper automaticallywrapinterlinears="yes"></lingPaper>')

# r = doc.xpath('/lingPaper/section1/example/interlinear/lineGroup')
# print len(r)
# print r

for element in doc.iter("lineGroup"):
	print "element: %s" % element.tag
	parent = element.getparent()
	print "parent: %s" % parent.tag
	print "number of children: %i" % len(parent)
	print "-"

	# analyze lineGroup structure
	lineGroupNodeList = analyzeLineGroup(element)

	# count returned nodes
	nodeCount = len(lineGroupNodeList)
	print "number of returned tables: %i" % nodeCount

	# remove original lineGroup element 
	parent.remove(element)

	position = 0
	for lineGroupNode in lineGroupNodeList:
		parent.insert(position, lineGroupNode)
		position = position + 1
	#	print(etree.tostring(lineGroupNode, pretty_print=True))

	#print "children: %i" % len(parent)

# save nodes in an output file
f = open(outputFile,'w')
outputData = etree.tostring(doc,pretty_print=True)
f.write(outputData)
f.close()

sys.exit(0)

