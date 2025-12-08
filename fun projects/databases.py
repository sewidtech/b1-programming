import sqlite3


#used for connecting sqlite with python
connection = sqlite3.connect("store_DB")



#cursor used to navigate 
cursor = connection.cursor()

#store table
command1 = "CREATE TABLE IF NOT EXISTS " \
"stores(store_id INTEGER PRIMARY KEY , Location text)"

cursor.execute(command1)


#purchase table
command2 = "CREATE TABLE IF NOT EXISTS " \
"purchase(purchase_id INTEGER PRIMARY KEY , store_id INTEGER , total_cost FLOAT , " \
"FOREIGN KEY(store_id) REFERENCES stores(store_id))"


cursor.execute(command2)


cursor.execute("INSERT INTO stores VALUES(21 , 'EGYPT , EGY')")
cursor.execute("INSERT INTO stores VALUES (95 , 'chicago , IL')")
cursor.execute("INSERT INTO stores VALUES (64 , 'Iowa city , IA')")



#get results

cursor.execute("INSERT INTO purchase VALUES (54 ,21 ,15.49)")
cursor.execute("INSERT INTO purchase VALUES (23 , 64 , 21.12)")



cursor.execute("SELECT * FROM purchase")
rows = cursor.fetchall()




#whole value of purchase takes 12 places , store id 10 and cost 10
print(f"{'Purchase ID':<12} {'Store ID':<10} {'Total Cost':<10}")
print("-" * 35)

for p_id, s_id, cost in rows:
    print(f"{p_id:<12} {s_id:<10} {cost:<10}")


results = cursor.fetchall()
print(results)
