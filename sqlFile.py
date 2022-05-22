import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.execute("insert into customer_assignment(name, email, dob, slug, address, status, reference_id) values('daksh','daksh@mail.com', '18-05-2001', 'daksh','test address',0,1)")
con.commit()
con.close()
