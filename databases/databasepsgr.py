import psycopg2

def create_table():
    conn = psycopg2.connect("dbname= 'test1' user='sbxaba' password='psg12345' host='localhost' port='5432'")        
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL )")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname= 'test1' user='sbxaba' password='psg12345' host='localhost' port='5432'")        
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view_db():
    conn = psycopg2.connect("dbname= 'test1' user='sbxaba' password='psg12345' host='localhost' port='5432'")        
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname= 'test1' user='sbxaba' password='psg12345' host='localhost' port='5432'")        
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname= 'test1' user='sbxaba' password='psg12345' host='localhost' port='5432'")        
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

# delete("apple") 
# create_table()
# insert("apple",10,15)
# update(1000,8,"Wine Glass")
# print(view_db())
# update(867,12,"apple")
