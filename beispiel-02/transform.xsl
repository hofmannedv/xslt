<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

<xsl:template match="/">
     <xsl:apply-templates/>
</xsl:template>

<xsl:template match="/">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN" "../docbook-xml-4.5/docbookx.dtd"&gt;</xsl:text>

	<book>
		<title>
			<xsl:value-of select="//title"/>
		</title>
		<chapter>
			<title>Teil 1</title>
			<para>
				<xsl:value-of select="//author"/>
			</para>
		</chapter>
	</book>
</xsl:template>

</xsl:stylesheet>
