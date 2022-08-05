import psycopg2

dsn = "dbname={} user={} password={}".format('blog', 'josephnomo', '4705')
con = psycopg2.connect(dsn)
cur = con.cursor()

cur.execute('SELECT full_name, pwd FROM users;')
values = cur.fetchone()
datas = {
    'pwd' : values[1],
    'full_name' : values[0] + 'Jr'
}

statement = 'INSERT INTO users (pwd, full_name) VALUES (%(pwd)s, %(full_name)s);'

cur.execute(statement, datas)
con.commit()

cur.execute('SELECT * FROM users;')
results = cur.fetchall()

for row in results:
    print(row)

con.close()
cur.close()
