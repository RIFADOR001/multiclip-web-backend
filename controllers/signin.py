import bcrypt 

# # example password 
# password = 'password123'
  
# # converting password to array of bytes 
# bytes = password.encode('utf-8') 
  
# # generating the salt 
# salt = bcrypt.gensalt() 
  
# # Hashing the password 
# hash = bcrypt.hashpw(bytes, salt) 
  
# print(hash)

def isValid(pwd, hashed):
	# example password 
	# password = 'passwordabc'
	password = pwd
	# converting password to array of bytes 
	byts = password.encode('utf-8') 
	  
	# generating the salt 
	salt = bcrypt.gensalt() 
	hashed = hashed.encode('utf-8')
	print(f"{hashed = }")
	
	# Hashing the password 
	hash = bcrypt.hashpw(byts, salt) 
	print(f"{hash = }")
	# Taking user entered password  
	userPassword = password
	# encoding user password 
	userBytes = userPassword.encode('utf-8') 
	  
	# checking password 
	result = bcrypt.checkpw(userBytes, hashed) 
	print(f'{result = }')
	if result:
		print("Valid login")
		return True
	else:
		print("incorrect user information")
		return False
	  


def handleSignin(cur, usern, pwd):
	try:
		print('handle')
		# Delete an entry
		# select_script = 'SELECT * FROM mclogin WHERE username = %s'
		# select_record = (usern,)
		# cur.execute(select_script, select_record)
		# cur.execute("SELECT * FROM mclogin WHERE id = 1")
		select_script = "SELECT * FROM mclogin WHERE username = %s"
		cur.execute(select_script, (usern,))
		# cur.execute("SELECT * FROM mclogin")
		# rec = cur.fetchall()
		rec = cur.fetchone()
		if rec is None:
			print("user not found")
			return False
		print(f'{rec = }')
		print('fetch')
		valid = isValid(pwd, rec[2])
		if valid:
			return True
		else:
			return False

			print('record: ', record)
		# In case we don't find the user
		

	except Exception as error:
		print(error)
		return error




