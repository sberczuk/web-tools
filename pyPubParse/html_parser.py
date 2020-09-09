import re

from bs4 import BeautifulSoup

def process_article(article):
    dataMap = dict()
    type = 'article'
    time = article.time
    displayDate = ''
    timeStamp = ''
    if(time is not None):
        timeStamp = time['datetime']
        displayDate = time.get_text()

    titleLink = article.select_one('a:is(.title)')
    #print(titleLink['href'])
    publicationAnchor = article.select_one('a:is(.publication)')
    publicationSpan = article.select_one('span:is(.publication)')
    localUrlAnchor = article.select_one('a:is(.url-local)')
    publicationLink = ''
    publicationName = ''


    # remove extra whitespace chars inside title string
    title = re.sub("\s+", " ", titleLink.string)
    if(publicationAnchor is not None):
        publicationLink = publicationAnchor['href']
        publicationName = publicationAnchor.get_text()
    elif (publicationSpan is not None):
        publicationLink = ''
        publicationName = publicationSpan.get_text()
    else:
        print("no Anchor for " + title)

    localLink = ''
    if(localUrlAnchor is not None):
        localLink = localUrlAnchor['href']
        # look for a span or other element with 'publication'


    articleLink = titleLink["href"]
    # The text of what was there
    bodyContent = re.sub("\s+", " ", article.get_text())
    dataMap['type'] = type
    dataMap['text']  = bodyContent
    dataMap['title'] = title
    dataMap['source'] = ''
    dataMap['localUrl'] = localLink
    dataMap['docLink'] = articleLink
    dataMap ['timeStamp'] = timeStamp
    dataMap['displayDate'] = displayDate
    dataMap['publication'] = publicationName
    dataMap['publicationUrl'] = publicationLink
    print(dataMap)

with open("pubs.html") as fp:
    soup = BeautifulSoup(fp)
    body = soup.find(class_="bodytext")
    # get bodytext div. then search from that.
    # articles = body.find_all(attrs={'data-recordType':'article'})
    # TODO use body OR soup
    # Generate Strawman JSON from what is here.
    # Check for empty or missing attribs and display only what we have, since we have the catchall
    # Then do other pubs

    articles = soup.find_all(attrs={'data-record-type':'article'})
    # print(articles)
    for article in articles:
        process_article(article)


