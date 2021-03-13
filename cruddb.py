import mysql.connector

items = []

conn = mysql.connector.connect(host='sql0037',
                              #database='test',
                              user='root',
                              password='linux',
                              auth_plugin='mysql_native_password',
                              charset='utf8')

    
def insertab():
    i = 'in1216'
    mycursor = conn.cursor()
    mycursor.execute(f"use {i}")
    mycursor.execute("INSERT INTO offres2 (title, company, salary, summary) VALUES (%s, %s, %s, %s)", (job['title'],job['company'],job['salary'],job['summary']))
    conn.commit()
    conn.close()

def getoffre():
    i = 'in1218'
    mycursor = conn.cursor()
    mycursor.execute(f"use {i}")
    mycursor.execute("select * from offres2")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
   
    conn.close()

getoffre()



