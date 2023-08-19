import psycopg2


def send_human_info(command):
    mydb = psycopg2.connect(user="postgres",
                            password="karimbek2004",
                            host="127.0.0.1",
                            port="5432",
                            database="trading")
    mycursor = mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return res
