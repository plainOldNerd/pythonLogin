import dbConfig
#https://www.youtube.com/watch?v=RsKmsOHBmXM
import mysql.connector as connector

conn = connector.connect(host=dbConfig.host, user=dbConfig.user, password=dbConfig.pwd, database=dbConfig.db)
if conn.is_connected():
    print('dbCreate says \'connected\'')

    #https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    cursor = conn.cursor()
    createTableQuery = '''create table if not exists Users (
    username varchar(20) not null,
    password varchar(20) not null,
    faveColor varchar(7) not null,
    faveSize varchar(8) not null,
    faveAnimal varchar(20) not null,
    primary key (username)
    );'''
    cursor.execute(createTableQuery)

    conn.close()
else:
    print('DBMS said to fuck off')
