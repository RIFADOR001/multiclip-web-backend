import bcrypt 


def handleRegister(conn, usern, pwd):
	try:
	
		# pwd1 = "dog"
		# pwd2 = "cat"
		# pwd3 = "mouse"
		# bytes1 = pwd1.encode('utf-8')
		# bytes2 = pwd2.encode('utf-8')
		# bytes3 = pwd3.encode('utf-8')
		# salt1 = bcrypt.gensalt()
		# salt2 = bcrypt.gensalt()
		# salt3 = bcrypt.gensalt()
		# hash1 = bcrypt.hashpw(bytes1, salt1)
		# hash2 = bcrypt.hashpw(bytes2, salt2)
		# hash3 = bcrypt.hashpw(bytes3, salt3)

		byts = pwd.encode('utf-8')
		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(byts, salt)
		# In order to store it correctly we need to decode again
		# Otherwise the db stores it in a weird way. This just changes
		# from bytes to string, but it's still a hash
		hashd = hash.decode('utf-8')
		# print(f"{hash = }")
		# print(f"decoded {hashd = }")
		# print(f"{hash1 = }")
		# print(f"{hash2 = }")
		# print(f"{hash3 = }")


		# We define a script to insert and data to insert
		insert_script = 'INSERT INTO mclogin (username, hash) VALUES (%s, %s)'
		# insert_values = [('James', hash1), ('Robin', hash2), ('Xavier', hash3)]
		insert_value = [usern, hashd]
		# cur.execute(insert_script, insert_value)
		cur = conn.execute(insert_script, insert_value)
		# for record in insert_values:
		# 	cur.execute(insert_script, record)

		# Here we can print the information from the mclogin table
		# cur.execute('SELECT * FROM mclogin')
		# for record in cur.fetchall():
		# 	print(record)
		print('Entries of mclogin')
		cur = conn.execute("SELECT * FROM mclogin")
		for record in cur:
			print(record)

		return True

	except Exception as error:
		print(error)
		return error


