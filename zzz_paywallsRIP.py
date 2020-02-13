import pdfkit, urllib.request, urllib.error, urllib.parse, random, re, time
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def download(url):
    temp = urllib.request.Request(
        url, 
        data=None,
        # we disguise as a google bot to get access to the p2w news lel
        headers={
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html',
            'Referrer': 'https://www.google.com/'
        })
    response = urllib.request.urlopen(temp)
    webContent = response.read()

    temp2 = webContent.decode('utf8')
    temp2[:60]
    soup = BeautifulSoup(temp2, 'html.parser')
    title = soup.find('title').get_text()
    title = title[:len(title)-18]
    title = title.replace(" ", "_")
    title = re.sub(r'\W+', '', title)
        

    html_file = title + ".html"
    pdf_file = title + ".pdf"

    f = open(html_file, 'wb')
    f.write(webContent)
    f.close

    '''
    # i dont like pdfkit, it takes super long to convert to pdf on my pc
    try:
        pdfkit.from_file(html_file, pdf_file)

    except:
        pass
    '''


def get_all_links(url):
    liste = []
    good_links = []
    html = str(urllib.request.urlopen(url).read())
    for i in range(len(html) - 3):
        if html[i] == '<' and html[i+1] == 'a' and html[i+2] == ' ':
            pos = html[i:].find('</a>')
            liste.append(html[i: i+pos+4])
    for z in liste:
        if "href" in z:
            z = z[z.find('href="'):]
            z = z[6:]
            z = z.split(" ", 1)[0]
            if "/content/" in z:
                good_links.append("https://www.ft.com" + z[:-1])

    return good_links

        

lel = input("Press Enter to download all Financial Times articles: ")
url = "https://www.ft.com/"
url_list = get_all_links(url)
# if u cancel download and continue later so u dont have to wait
random.shuffle(url_list)
# random timeouts to not get httperrors that often
counter = 1
for i in url_list:
    if counter % 60 == 0:
        time.sleep(5)
    try:
        download(i)
    except HTTPError as err:
        time.sleep(7)
    counter += 1
    timeout = random.uniform(1, 3)
    time.sleep(timeout)
print("Congrats, you have downloaded all FT front page articles.") 


    

