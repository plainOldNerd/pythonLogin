def htmlTemplate(username, faveColor, faveSize, faveAnimal):
    return f'''
    <html>
    <script>
        function logout() {{
            // although security is not an issue, sensative data should 
            // not be accessible by the back button.   ;) 
            document.location.replace('/');
        }}
    </script>
    <body>
        <div style="color:{faveColor};">
            Hello {username}, your favorite animal is a {faveSize} {faveAnimal}.
        </div>
        <br />
        <button onclick=logout()>Logout</button>
    </body>
    </html>
    '''