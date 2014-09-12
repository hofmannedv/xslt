<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

<xsl:template match="/">
     <xsl:apply-templates/>
</xsl:template>

<xsl:template match="/">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN" "../docbook-xml-4.5/docbookx.dtd"&gt;</xsl:text>

	<article>
		<articleinfo>
			<title><xsl:value-of select="/lingPaper/frontMatter/title"/></title>
			<author>
				<firstname><xsl:value-of select="/lingPaper/frontMatter/author"/></firstname>
				<surname></surname>
			</author>
		</articleinfo>

		<section>
			<title><xsl:value-of select="/lingPaper/section1/secTitle"/></title>
			<para>Test</para>
			<table frame='none'>
				<title></title>
				<tgroup cols="5">
					<tbody>
						<xsl:for-each select="//example/interlinear"> 
							<xsl:for-each select="lineGroup/line"> 
								<row>
								<xsl:for-each select="wrd/langData"> 
										<entry><xsl:value-of select="."/></entry>
								</xsl:for-each>
								<xsl:for-each select="wrd/gloss">
										<entry><xsl:value-of select="."/></entry>
								</xsl:for-each>
								</row>
							</xsl:for-each>
						</xsl:for-each>
					</tbody>
				</tgroup>
			</table>
		</section>
	</article>
</xsl:template>

</xsl:stylesheet>
