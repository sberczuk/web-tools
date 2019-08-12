from bs4 import BeautifulSoup


with open("pubs.html") as fp:
    soup = BeautifulSoup(fp)
    body = soup.find(class_="bodytext")
    # get bodytext div. then search from that.
    print(body.find_all(attrs={'data-record-type':'article'}))
    #print(soup.find_all(attrs={'data-record-type':'article'}))