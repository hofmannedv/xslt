<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

<xsl:template match="/">
	<xsl:apply-templates/>
</xsl:template>

<xsl:template name="docbook">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN" "../docbook-xml-4.5/docbookx.dtd"&gt;</xsl:text>
</xsl:template>

<xsl:template name="articleinfo">
	<articleinfo>
		<title><xsl:value-of select="/lingPaper/frontMatter/title"/></title>
		<author>
			<firstname><xsl:value-of select="/lingPaper/frontMatter/author"/></firstname>
			<surname></surname>
		</author>
	</articleinfo>
</xsl:template>

<xsl:template name="secTitle">
	<title>
		<xsl:value-of select="secTitle"/>
	</title>
</xsl:template>

<xsl:template name="example">
	<xsl:variable name="fields" select="count(./interlinear/lineGroup/line/wrd)"></xsl:variable>
	<xsl:variable name="lines" select="3"></xsl:variable>
	<xsl:variable name="columns" select="$fields div $lines"></xsl:variable>
	<informaltable frame='none'>
		<!-- tgroup cols="$columns" -->
		<xsl:text disable-output-escaping="yes">&lt;tgroup cols="</xsl:text>
		<xsl:value-of select="$columns"/>
		<xsl:text disable-output-escaping="yes">"&gt;</xsl:text>
			<tbody>
				<xsl:for-each select="interlinear/lineGroup/line"> 
					<row>
						<xsl:for-each select="wrd/langData"> 
							<entry><xsl:value-of select="."/></entry>
						</xsl:for-each>
						<xsl:for-each select="wrd/gloss">
							<entry><xsl:value-of select="."/></entry>
						</xsl:for-each>
					</row>
				</xsl:for-each>
			</tbody>
		<xsl:text disable-output-escaping="yes">&lt;/tgroup&gt;</xsl:text>
		<!-- /tgroup -->
	</informaltable>
	<para>
		<xsl:value-of select="interlinear/free"/>
	</para>
</xsl:template>

<xsl:template match="/">
	<xsl:call-template name="docbook" />

	<article>
		<xsl:call-template name="articleinfo" />

		<xsl:for-each select="/lingPaper/section1">
			<section>
				<xsl:call-template name="secTitle" />
				<xsl:for-each select="example"> 
					<section>
						<title>Paragraph</title>
						<para>Test</para>

						<xsl:call-template name="example" />
						<!-- para><xsl:value-of select="name(../example)"/></para-->
					</section>
				</xsl:for-each>
			</section>
		</xsl:for-each>
	</article>
</xsl:template>

</xsl:stylesheet>
