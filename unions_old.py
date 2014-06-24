from BeautifulSoup import BeautifulSoup
import requests

urls = []

for x in range(1,46):
    print x
    urls.append("http://www.unions.org/union_search.php?&abbr=&abbr_key=&bizcat=0&zip=95230&local=&zip_key=95230&pagenum=" + repr(x))




for url in urls:
    html = requests.get(urls[0]).content
    soup = BeautifulSoup(html)
    #soup.findAll(attrs = {'class' : "searchResult"  })
    results = soup.findAll(attrs = {"class" : "searchResult"  })
    

    for result in results:
        #print result
        print result.text



       

# try:
            

 #           print result.text

           # for tag in result.findAll("a"):
            #    print tag.target
             #   print tag.title
               # print tag.class
              #  print tag.href

  #      except:
   #         pass

