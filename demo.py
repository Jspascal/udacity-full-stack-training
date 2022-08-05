import psycopg2

dsn = "dbname={} user={} password={}".format('blog', 'josephnomo', '4705')
con = psycopg2.connect(dsn)
cur = con.cursor()

cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        pwd varchar(255),
        full_name varchar(255)
    );
""")

cur.execute("""
    INSERT INTO users (pwd, full_name)
    VALUES ('basket', 'Jean Gatsi'),
    ('orange', 'Joseph Pascal'),
    ('ananas', 'NOMO SAMBOU');
""")

con.commit()
cur.close()
con.close()
