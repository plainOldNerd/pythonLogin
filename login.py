from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import json

import dbCreate

''' This function splits the POST values into key and value pairs
    i.e. it splits the string about the & sign, and then about the
    = sign to extract keys and values
    Obviously it assumes that there are no = or & signs in the 
    given string. This should be validated on the front end!
'''
def splitFormValues(actualRequestLine):
    newDict = {}
    substringStart = 0
    substringEnd = 0
    key = ''
    value = ''
    for index in range(len(actualRequestLine)):
        if actualRequestLine[index] == '=':
            substringEnd = index
            key = actualRequestLine[substringStart:substringEnd]
            substringStart = index + 1
        if actualRequestLine[index] == '&':
            substringEnd = index
            value = actualRequestLine[substringStart:substringEnd]
            substringStart = index + 1
            newDict[key] = value
    else:
        substringEnd = index + 1
        value = actualRequestLine[substringStart:substringEnd]
        newDict[key] = value
    return newDict

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'login.html'
        self.path = '/Users/Xavier/Desktop/projects/pythonlogin/' + self.path
        try:
            file_to_open = open(self.path).read()
            self.send_response(200)
            #self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('Something f**ked up! Sorry.', 'utf-8'))

    def do_POST(self):
        #https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
        match self.path:
            case '/':
                try:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    content_len = int(self.headers.get('content-length'))
                    #returns a bytes type, NOT string!!
                    postbody = self.rfile.read(content_len)
                    #https://www.freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-bytestring/
                    #https://stackoverflow.com/questions/33143504/how-do-i-encode-decode-percent-encoded-url-strings-in-python
                    actualRequestLine = unquote(postbody.decode('utf-8'))
                    #print(actualRequestLine)
                    formKeyValues = splitFormValues(actualRequestLine)
                    '''
                    for key in formKeyValues.keys():
                        print(key, ' = ', formKeyValues[key])
                    '''
                    response = '<div style="color: '
                    response += formKeyValues['faveColour']
                    response += ';">hello '
                    response += formKeyValues['username']
                    response += ', your favourite animal is a '
                    response += formKeyValues['animalSize'] + ' '
                    response += formKeyValues['faveAnimal'] + '</div>'
                    self.wfile.write(bytes(response, 'utf-8'))
                except:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes('Something f**ked up in POST! Sorry.', 'utf-8'))

            case '/checkUsernameExists':
                try:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/javascript')
                    self.end_headers()
                    content_len = int(self.headers.get('content-length'))
                    #returns a bytes type, NOT string!!
                    postbody = self.rfile.read(content_len)
                    #https://www.freecodecamp.org/news/python-bytes-to-string-how-to-convert-a-bytestring/
                    #https://stackoverflow.com/questions/33143504/how-do-i-encode-decode-percent-encoded-url-strings-in-python
                    actualRequestLine = unquote(postbody.decode('utf-8'))
                    formKeyValues = splitFormValues(actualRequestLine)

                    usernameExists = False
                    response = json.dumps({
                        "usernameExists": usernameExists
                    })
                    self.wfile.write(bytes(response, 'utf-8'))
                except:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes('Something f**ked up in POST! Sorry.', 'utf-8'))

            case _:
                print('default case')

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()