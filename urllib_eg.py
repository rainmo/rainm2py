import urllib.request
file = urllib.request.urlopen('http://helloworldbook.com/data/message .txt')
msg = file.read()
print (msg)
