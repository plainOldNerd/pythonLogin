import dbConfig
#https://www.youtube.com/watch?v=RsKmsOHBmXM
import mysql.connector as connector

conn = connector.connect(host=dbConfig.host, user=dbConfig.user, password=dbConfig.pwd, database=dbConfig.db)
if conn.is_connected():
    print('connected')

    #https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    cursor = conn.cursor()
    createTableQuery = 'create table if not exists Users ('
    createTableQuery += 'username varchar(20) not null,'
    createTableQuery += 'password varchar(20) not null,'
    createTableQuery += 'faveColor varchar(7) not null,'
    createTableQuery += 'faveSize varchar(8) not null,'
    createTableQuery += 'faveAnimal varchar(20) not null,'
    createTableQuery += 'primary key (username)'
    createTableQuery += ');'
    cursor.execute(createTableQuery)

    conn.close()
else:
    print('DBMS said to fuck off')
