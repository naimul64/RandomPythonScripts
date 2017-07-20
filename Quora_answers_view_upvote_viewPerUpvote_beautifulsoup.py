from bs4 import BeautifulSoup
from operator import itemgetter
import urllib


def round(decimal_place, floating_no):
    floating_no_backup = floating_no

    if type(floating_no) == type(9):
        floating_no = float(str(floating_no) + '.0')

    divby2 = 100
    while divby2 != 0:
        divby2 = floating_no / 2
        divby2 = int(divby2)
        if divby2 >= 1:
            floating_no -= divby2
    floating_no -= 1

    for i in range(decimal_place + 1):
        floating_no *= 10
    fractionIntoInt = int(floating_no)
    if fractionIntoInt % 10 > 4:
        fractionIntoInt = int(fractionIntoInt / 10)
        fractionIntoInt += 1
    else:
        fractionIntoInt = int(fractionIntoInt / 10)
    back_to_fraction = float(fractionIntoInt)
    for i in range(decimal_place):
        back_to_fraction /= 10

    rounded_float = float(int(floating_no_backup))
    rounded_float += back_to_fraction

    return rounded_float



r = urllib.urlopen("file:///home/insan/Desktop/gurbaze/What%20is%20your%20most%20powerful%20tip_%20-%20Quora.html").read()
soup = BeautifulSoup(r,"lxml")
mydivs = soup.findAll("div", { "class" : "Answer AnswerBase" })
print str(len(mydivs)) + " answers found"
howAmI = []
for div in mydivs:
    try:
        user = div.findAll("a", { "class" : "user" })[0].string
    except:
        user = "ANONYMOUS!!!!!!!!!"
    # print user.strip

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
    #print str(view) + " views"


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
    # print str(upvote) + " upvotes"

    if upvote == 0 :
        # print "No upvotes."
        viewPerUpvote = 100000000000000
    else:
        viewPerUpvote = float(view)/float(upvote)
        # print str(viewPerUpvote) + " views per upvote ===============>\n\n"



    try:
        answer_link = div.findAll("a", { "class" : "answer_permalink" })[0]
        answer_link = answer_link['href']

    except Exception as e:
        answer_link =""


    lisht = [user, view, upvote, round(decimal_place=2, floating_no=viewPerUpvote), answer_link]
    howAmI.append(lisht)

sort_index = 3
howAmI = sorted(howAmI, key=itemgetter(sort_index))
for l in howAmI:
    print l