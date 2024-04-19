import dbConfig
#https://www.youtube.com/watch?v=RsKmsOHBmXM
import mysql.connector as connector

def queryUsernameExists(username):
    conn = connector.connect(host=dbConfig.host, user=dbConfig.user, password=dbConfig.pwd, database=dbConfig.db)
    password = ''
    if conn.is_connected():
        print('queryUsernameExists says \'connected\'')

        #https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
        cursor = conn.cursor(buffered=True)
        #https://www.freecodecamp.org/news/how-to-lowercase-python-string/
        #https://www.tutorialspoint.com/is-there-a-mysql-command-to-convert-a-string-to-lowercase#:~:text=Yes%2C%20you%20can%20use%20the,convert%20the%20string%20into%20lowercase.&text=lower('yourStringValue)%3B,you%20can%20use%20LCASE()
        query = f'''select username, password
        from Users
        where lower(username) = '{username.lower()}';
        '''
        cursor.execute(query)
        numResults = cursor.rowcount
        if numResults == 1:
            row = cursor.fetchone()
            password = row[1]

        conn.close()
    else:
        print('DBMS said to fuck off')
    return password

def getUserData(username):
    conn = connector.connect(host=dbConfig.host, user=dbConfig.user, password=dbConfig.pwd, database=dbConfig.db)
    row = ()
    if conn.is_connected():
        cursor = conn.cursor(buffered=True)
        query = f'''select username, faveColor, faveSize, faveAnimal
        from Users
        where lower(username) = '{username.lower()}';
        '''
        cursor.execute(query)
        row = cursor.fetchone()
        conn.close()
    else:
        print('DBMS said to fuck off')
    print('now finishing getuserdata')
    return row

def insertUser(username, password, faveColor, faveSize, faveAnimal):
    conn = connector.connect(host=dbConfig.host, user=dbConfig.user, password=dbConfig.pwd, database=dbConfig.db)
    if conn.is_connected():
        try:
            cursor = conn.cursor(buffered=True)
            query = f'''insert into Users (username, password, faveColor, faveSize, faveAnimal)
            values ('{username}', '{password}', '{faveColor}', '{faveSize}', '{faveAnimal}');'''
            cursor.execute(query)
            #https://stackoverflow.com/questions/6027271/python-mysql-insert-not-working
            conn.commit()
            conn.close()
        except:
            print('something f**ked up inserting user into DB')
    return
