from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('file:///home/insan/Documents/zz_GURBAGE/bs.html').read()
soup = BeautifulSoup(r,"lxml")
mydivs = soup.findAll("div", { "class" : "Answer AnswerBase" })
print len(mydivs)
howAmI = []
for div in mydivs:
    user = div.findAll("a", { "class" : "user" })[0].string
    print user.strip
 
 
 
   
    try:
        view = div.findAll("span", { "class" : "meta_num" })[0].string
        view = view.strip().replace(",","")
        if  view[-1] == 'k':
            view = view[:-1]
            view = int(float(view) * 1000)
        elif view[-1] == 'm':
            view = view[:-1]
            view = int(float(view) * 1000000)
    except Exception as e:
        #print e
        view = 0
    view = int(str(view))
    print str(view) + " views"
 
 
    try:
        upvote = div.findAll("a", { "class" : "VoterListModalLink" })[0].string
        upvote = upvote.strip().replace(",","")
        upvote = upvote.split(' ')[0]
 
        upvote = upvote.strip()
        if  upvote[-1] == 'k':
            upvote = upvote[:-1]
            upvote = int(float(upvote) * 1000)
        elif upvote[-1] == 'm':
            upvote = upvote[:-1]
            upvote = int(float(upvote) * 1000000)
    except Exception as e:
        #print e
        upvote = 0
    upvote = int(str(upvote))
    print str(upvote) + " upvotes"
 
    if upvote == 0 :
        print "No upvotes."
        viewPerUpvote = 100000000000000
    else:
        viewPerUpvote = float(view)/float(upvote)
        print str(viewPerUpvote) + " views per upvote ===============>\n\n"
 
    lisht = [user, view, upvote, viewPerUpvote]
    howAmI.append(lisht)
 
for l in howAmI:
    print l