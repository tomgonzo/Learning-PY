#Chapter 20 - Bringing it all Together! ChapterNotes

#Let's build a web scraper!

#A quick primer on HTML!
#HTML is one of the fundamental technologies programmers use to build sites,
#along with Javascript and CSS.

#HTML gives a website structure. It is made up of tags a browser uses to
#layout web pages. Entire websites can be built with HTML.

#Exercise 1!
#See file in directory - index.html

#The browser uses the HTML tags in the file to display the website. 

#An HTML tag (tag for short) tells the browser what to do.
#Tags have a beginning tag and a closing tag, often with text in between.

#The text between <head></head> is web page metadata.
#The text between <title></title?> is displayed in the browser tab.
#Everything in between <body></body> makes up the actual site.
#The <a></a> tags create a link.

#Tags can hold data. href="google.com" inside <a></a> links to google.

#With this knowledge, let's build a web scraper!

### Scraping Google News ###

#The scraper will fetch all Google News stores by extracting the <a></a> tags
#from Google News' HTML. Google News uses these tags to link to the different
#sites that make up the site. The scraper will collect the URLs for the
#stories Google News is displaying. 

#The BeautifulSoup module will parse Google News HTML. Parsing means taking
#a format like HTML and giving it structure. Begin by installing BeautifulSoup.

