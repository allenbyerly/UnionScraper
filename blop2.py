from BeautifulSoup import BeautifulSoup
import requests

urls = []

for x in range(1,46):
    print x
    urls.append("http://www.unions.org/union_search.php?&abbr=&abbr_key=&bizcat=0&zip=95230&local=&zip_key=95230&pagenum=" + repr(x))


html = requests.get(urls[0]).content
soup = BeautifulSoup(html)
results = soup.findAll(attrs = {"class" : "searchResult"  })

for result in results:
            #print result
            print result.text


#<h3><a href="/unions/american-federation-of-government-employees/local-1208/18740" title="AFGE - GOVERNMENT EMPLOYEES Local 1208">AFGE - GOVERNMENT EMPLOYEES Local 1208</a></h3>
#<p> <br />SANGER, CA 936579737 <a target="_blank" href="http://maps.google.com/maps?q=+SANGER%2C+CA+93657" class="xSmall blue" title="View map">Map</a>
#<br />ELODIA CASTRO                            <br />Union Members: 49                                        </p>
#<div class="clear"></div>
#</div>



location = result.p.text.split("Map", 1)[0]
members = result.p.text.split("Members: ", 1)[1]

print location
print members