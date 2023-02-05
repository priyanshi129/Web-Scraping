import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent,"html.parser")
print(soup.prettify)

print(type(title))                                       #Tag object
print(type(title.string))                                #Navigable string object
print(type(soup))                                        #BeautifulSoup object
markup="<p><!-- Twitter Bootstrap --><p>"                #Comment object
soup2=BeautifulSoup(markup, features="html5lib") 
print(soup2.p.string)
print(type(soup2))


title=soup.title                                         #title of HTML page

paras=soup.find_all("p")                                 #paras tag of HTML page
print(paras)

print(soup.find("p"))                                    #first element
print((soup.find("p")),["class"])                        #class of first element
print(soup.find_all("p",class_="instock availability"))  #elements with class instock availability
print(soup.find("p").get_text())                         # text from elements
print(soup.get_text())                                   #entire text of HTML page

anchors=soup.find_all("a")                               #anchor tag of HTML page
print(anchors)
all_links=set()
for link in anchors:                                     #getting all the links
  if(link.get("href")!="#"):
    linkText="https://books.toscrape.com/"+ link.get("href")
    all_links.add(linkText)
    print(linkText)

promotions_left=soup.find(id="promotion_left")
for ele in promotions_left.contents:
  print(ele)






