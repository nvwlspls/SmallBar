import psycopg2

conn = psycopg2.connect("dbname='postgres' port='5423' user='wayne' password='smallbar'")

curr = conn.cursor()

curr.execute("SELECT * FROM spatial_ref_sys;")
check = curr.fetchone()
print check


#conn.commit()

curr.close() 

conn.close()
