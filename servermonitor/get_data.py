from requests_html import HTML, HTMLSession

#with open('sample.html') as html_file:
    #source = html_file.read()
    #html = HTML(html=source)

#match = html.find('div.article')

#print(match[0].text)


#articles = html.find('')

#for article in articles:
    #headline = article.find('', first=True).text
    #summary = article.find('', first=True).text
    #print(headline)
    #print(summary)
payload = {
    'inUserName': '',
    'inUserPass': ''
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('LOGIN_URL', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print p.text

    # An authorised request.
    r = s.get('A protected web page url')
    print r.text



session = HTMLSession()
r = session.get('https://chess.com')

div = r.html.find("<span class="number">0</span>", first=True)
print(div.html)
