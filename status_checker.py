import requests

gursavid_separate = ["accenture", "bmo", "deloitte", "ey", "google", "kpmg", "loblaw", "rbc", "roche", "td"]
gursavid_merged = ["Ada", "Air Canada", "EllisDon", "Georgian", "Ada", "Magna International", "BenchSci", "Air Canada", "Clearpath", "integrate.ai", "Borealis AI", "CN Internship", "Scotiabank", "Delphia", "CN", "Intact Financial Corporation", "Deep Genomics", "League"]

accepted_url = []
rejected_url = []

#Checking for separate urls

for link in gursavid_separate:

    url = "https://vectorinstitute.github.io/talent-hub-extractor/" + link + '.xml'
    response = requests.get(url)

    if response.status_code == 404:
        rejected_url.append(link)

    else:
        accepted_url.append(link)


#checking for merged url

url = "https://vectorinstitute.github.io/talent-hub-extractor/merged.xml"

response = requests.get(url)
html = response.text

for link in gursavid_merged:

    if link in html:
        accepted_url.append(link)

    else:
        rejected_url.append(link)

gursahaj_separate = ["Borealis%20AI", "CIBC", "Manulife", "Sun%20Life%20Financial", "Thomson%20Reuters", "Vector%20Institute"]
gursahaj_merged = ["Canvass Analytics Inc.", "OMERS", "Thales", "NVIDIA", "Shopify Inc."]

for link in gursahaj_separate:

    url = "https://vectorinstitute.github.io/talent-hub-selenium/" + link + '.xml'
    response = requests.get(url)

    if response.status_code == 404:
        rejected_url.append(link.replace("%20", " "))

    else:
        accepted_url.append(link.replace("%20", " "))


#checking for merged url

url = "https://vectorinstitute.github.io/talent-hub-selenium/merged.xml"

response = requests.get(url)
html = response.text

for link in gursahaj_merged:

    if link in html:
        accepted_url.append(link)

    else:
        rejected_url.append(link)

html_page = "<html><body><img src = './vectorlogo.png'><h1 style='text-align:center;'>Scraper summary<br><br>"
table = "<table align='center'><tr><th>Company</th><th>Status</ht></tr>"
for i in accepted_url:
    table = table + "<tr><td>" + i + "</td><td>Successful</td></tr>"
for i in rejected_url:
    table = table + "<tr><td>" + i + "</td><td>Failed</td></tr>"
html_page = html_page + table + "</body></html>"

text_file = open("index.html", "w")
n = text_file.write(html_page)
text_file.close()
