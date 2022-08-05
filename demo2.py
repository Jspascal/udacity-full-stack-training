import psycopg2

dsn = "dbname={} user={} password={}".format('blog', 'josephnomo', '4705')
con = psycopg2.connect(dsn)
cur = con.cursor()

statement = 'INSERT INTO users (pwd, full_name) VALUES (%(pwd)s, %(full_name)s)'

datas = {
    'pwd' : 'banane',
    'full_name' : 'CodeHacker237'
}

cur.execute(statement, datas)
con.commit()

con.close()
cur.close()
