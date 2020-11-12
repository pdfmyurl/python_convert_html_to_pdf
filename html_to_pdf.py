# This example converts raw HTML to PDF in Python

import requests

url = 'https://pdfmyurl.com/api'
# We need to send at least our license and the HTML that we want to convert, but more options can be used as described at https://pdfmyurl.com/html-to-pdf-api
mydata = {'license': 'yourlicensekey', 'html': 'Write Your Html Here'}

x = requests.post(url, data = mydata)

# Now x.text contains the PDF
localFile = open('mypdf.pdf', 'w')
localFile.write(x.text)
localFile.close()
