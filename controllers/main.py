# import psycopg2
# import psycopg2.extras
import psycopg 
from psycopg.rows import dict_row

from register import handleRegister
from signin import handleSignin
from notes import new_note, update_note, delete_note, display_notes_all, display_notes_keyword

hostname = "dpg-cnj6a3821fec73f4k1cg-a.oregon-postgres.render.com"
database = "smartbrain_p98h"
username = "rif001"
pwd = "JtZvd458CW0HW2Td6Cp3UoZvW7QtONjZ"
port_id = 5432

conn = None

try:
	# with psycopg2.connect(
	# 	host=hostname,
	# 	dbname=database,
	# 	user=username,
	# 	password=pwd,
	# 	port=port_id) as conn:
	with psycopg.connect(
		host=hostname,
		dbname=database,
		user=username,
		password=pwd,
		port=port_id) as conn:

		# The cursor is what we use to interact the database
		# In this way, we get the information as touples. It works well, but
		# for tables with many columns it might be inconvenient
		# cur = conn.cursor()
		# In this way we can obtain the information on dictionaries. That way
		# it is easier to access the information that we need (since we don't
		# rely in finding the index, but just in using the key)
		# with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
		with conn.cursor(row_factory=dict_row) as cur:
			# conn = psycopg.connect(row_factory=dict_row)
			# print("conn")

			# cur.execute('DROP TABLE IF EXISTS mclogin')

			create_script = ''' CREATE TABLE IF NOT EXISTS mclogin (
				id serial PRIMARY KEY,
				username text UNIQUE NOT NULL,
				hash VARCHAR(200) NOT NULL)
			'''
			# cur.execute(create_script)
			cur = conn.execute(create_script)

			# cur.execute('DROP TABLE IF EXISTS mcnotes')
			create_script_notes = ''' CREATE TABLE IF NOT EXISTS mcnotes (
				id serial PRIMARY KEY,
				username text NOT NULL,
				keyword VARCHAR(40) NOT NULL,
				code text UNIQUE NOT NULL,
				note VARCHAR(600) NOT NULL)
			'''
			# cur.execute(create_script)
			cur = conn.execute(create_script_notes)

			# usern = "pon"
			# pwd = "chan"
			# usern = 'mika'
			# pwd = 'perro'
			usern = 'A'
			pwd = 'Z'
			# reg = handleRegister(cur, usern, pwd)
			# print("before reg")
			# reg = handleRegister(conn, usern, pwd)
			# if reg != True:
			# 	print(reg)
			# handleSignin(cur, usern, pwd)
			keyw = 'JS'
			note = 'stuff' + keyw
			new_note = 'updated note003'
			new_keyw = 'JS003'

			# new_note(conn, usern, keyw, note)
			# display_notes_all(conn, usern)
			# display_notes_keyword(conn, usern, keyw)

			# update_note(conn, 1, usern, new_keyw, new_note)

			delete_note(conn, usern, 1)

			# # We define a script to insert and data to insert
			# insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
			# insert_values = [(1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D2'), (3, 'Xavier', 20000, 'D2')]
			
			# for record in insert_values:
			# 	cur.execute(insert_script, record)

			# # Here we can print the information from the employee table
			# cur.execute('SELECT * FROM employee')
			# for record in cur.fetchall():
			# 	print(record['name'], record['salary'])

			# # Here we update the entries
			# update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
			# cur.execute(update_script)

			# # Delete an entry
			# delete_script = 'DELETE FROM employee WHERE dept_id = %s'
			# delete_record = ('D1',)
			# cur.execute(delete_script, delete_record)

			# cur.execute('SELECT * FROM employee')
			# for record in cur.fetchall():
			# 	print(record['name'], record['salary'])

except Exception as error:
	print(error)

finally:
	# connection should always be closed
	if conn is not None:
		conn.close()





