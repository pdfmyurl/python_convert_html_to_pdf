# This example converts the URL https://www.example.com to PDF in Python

import urllib2

# Specify your license key and the URL that you want to convert. You can also use more options as described at https://pdfmyurl.com/html-to-pdf-api
data = {
   'license': 'yourlicensekey',
   'url': 'https://www.example.com'
}

requesturl = 'https://pdfmyurl.com/api?license={license}&url={url}'.format(**data)
result = urllib2.urlopen(requesturl)
localFile = open('mypdf.pdf', 'w')
localFile.write(result.read())
localFile.close()
