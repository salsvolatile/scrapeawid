# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://economia.icaew.com/en/accountancy-rich-list-2017/100-to-51")
#create an empty dictionary variable to hold our data later
record = {}
root = lxml.html.fromstring(html)
names = root.cssselect("article class div class h3")
for name in names:
  #print name.text
  print name.attrib['href']
  #store the link in the variable under the key 'link'
  record ['link'] = name.attrib['href']
  print record
  scraperwiki.sqlite.save(unique_keys=['link'], data=record)
  
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
