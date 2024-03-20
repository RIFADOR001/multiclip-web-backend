# In this module we define the functions to interact with notes
def new_note(conn, usern, keyw, note):
	insert_script = 'INSERT INTO mcnotes (username, keyword, code, note) VALUES (%s, %s, %s, %s)'
	insert_value = (usern, keyw, usern + keyw, note)

	cur = conn.execute(insert_script, insert_value)

	cur.execute('SELECT * FROM mcnotes')
	for record in cur.fetchall():
		print(record)

def update_note(conn, note_id, usern, keyw, note):
	update_script = 'UPDATE mcnotes SET keyword = %s, code = %s, note = %s WHERE id = %s and username = %s'
	print('before updating')
	cur = conn.execute(update_script, (keyw, usern + keyw, note, note_id, usern))
	print('after')

	cur.execute('SELECT * FROM mcnotes')
	for record in cur.fetchall():
		print(record)

def delete_note(conn, usern, note_id):
	delete_script = 'DELETE FROM mcnotes WHERE id = %s and username = %s'
	delete_record = (note_id, usern)
	cur = conn.execute(delete_script, delete_record)

	cur.execute('SELECT * FROM mcnotes')
	for record in cur.fetchall():
		print(record)

def display_notes_all(conn, usern):
	select_script = "SELECT * FROM mcnotes WHERE username = %s"
	cur = conn.execute(select_script, (usern,))
	print(f"List of records from {usern}")
	for record in cur:
		print(record)

def display_notes_keyword(conn, usern, keyw):
	select_script = "SELECT * FROM mcnotes WHERE username = %s AND keyword ILIKE %s"
	key="%"+keyw+"%"
	cur = conn.execute(select_script, (usern, key))
	print(f"List of records from {usern} where keyword is like {keyw}")
	for record in cur:
		print(record)












