from requests_html import HTML
with open('sample.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('div.article')

print(match[0].text)