import json
import re

from bs4 import BeautifulSoup

def process_book(b):
    dataMap = dict()
    for child in b.children:
        if child.name is not None:
            if len(child.contents) > 1:
              print ("map")
              key =child.name
              values = []
              for c in child.children:
                  if c.name is not None:
                    values.append(c.string)
              dataMap[key] = values
            else:
                stringValue = child.string
                if stringValue is None:
                    stringValue = ""
                dataMap[child.name] =str(stringValue).strip()
                print(">", len(child.contents), child.name, stringValue, "<")

    # bodyContent = re.sub("\s+", " ", b.get_text())
    # dataMap['type'] = type
    # dataMap['text']  = bodyContent
    # dataMap['title'] = title
    # dataMap['source'] = ''
    # dataMap['localUrl'] = localLink
    # dataMap['docLink'] = articleLink
    # dataMap ['timeStamp'] = timeStamp
    # dataMap['displayDate'] = displayDate
    # dataMap['publication'] = publicationName
    # dataMap['publicationUrl'] = publicationLink
    return dataMap



article_f = open('bookRecs.json', 'w+')
chapters_f = open('chapters.json', 'w+')
with open("books.xml") as fp:
    soup = BeautifulSoup(fp, features="html.parser")
    # get bodytext div. then search from that.
    # articles = body.find_all(attrs={'data-recordType':'article'})
    # TODO use body OR soup
    # Generate Strawman JSON from what is here.
    # Check for empty or missing attribs and display only what we have, since we have the catchall
    # Then do other pubs

    books = soup.find_all('book')
    # print(articles)
    jsonList = []
    for book in books:
        print("----")
        jsonList.append(process_book(book))
    print(json.dump(jsonList, article_f, sort_keys=True, indent=4))



    #print(json.dump(chapter_list, chapters_f, sort_keys=True, indent=4))
    # output pretty printed JSON To a file

    # Process book and other links
