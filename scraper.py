####################################
2 #STARTHERE:Tutorial2:Basicscrapingandsavingtothedatastore.
 #FollowtheactionslistedinBLOCKCAPITALSbelow.
 ####################################

 import scraperwiki
 html = scraperwiki.scrape('http://inmo.ie/6022')
 print "Clickonthe...morelinktoseethewholepage"
 print html
#---------------------------
 #1.ParsetherawHTMLtogettheinterestingbits-thepartinside<tdtags.
 #--UNCOMMENTTHE6LINESBELOW(i.e.deletethe#atthestartofthelines)
 #--CLICKTHE'RUN'BUTTONBELOW
 #Checkthe'Console'tabagain,andyou'llseehowwe'reextracting
 #theHTMLthatwasinside<td</tdtags.
 #Weuselxml,whichisaPythonlibraryespeciallyforparsinghtml.
 #---------------------------
    importlxml.html
root = lxml.html.fromstring(html)#turnourHTMLintoanlxmlobject
tds = root.cssselect('td')#getallthe<tdtags
for td in tds:
print lxml.html.tostring(td) # the full HTML tag
print td.text # just the text inside the HTML tag

#---------------------------
#2.SavethedataintheScraperWikidatastore.
#--UNCOMMENTTHETHREELINESBELOW
 #--CLICKTHE'RUN'BUTTONBELOW
#Checkthe'Data'tab-hereyou'llseethedatasavedintheScraperWikistore.
#---------------------------
for td in tds:
 record = { "td" : td.text } # column name and value
scraperwiki.sqlite.save(["td"], record) # save the records one by one

#---------------------------
 #GobacktotheTutorialspageandcontinuetoTutorial3tolearnabout
#morecomplexscrapingmethods.
#---------------------------
