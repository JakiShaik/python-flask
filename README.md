# python-flask

Intro to building web applications using Flask.

# Installation
 
 Make sure you have the following things installed.
    Python: https://www.python.org/downloads/
    Install Flask using pip install Flask (pip, a python package installer, comes with Python 2.7)
    Install MySQL

# Hello World!
    from flask import Flask
    app = Flask(__name__)
    @app.route(“/”)
    def hello():
	    return “Hello World!”
    If __name__ = “__main__”:
      app.run()

# Rendering HTML

  from flask import Flask, render_template
    app = Flask(__name__)
    @app.route(“/”)
    def render():
    return render_template(‘hey.html’)
    if __name__ = “__main__”:
    app.run()
    
# Connecting to Database

  Create a new mysql database flask.                                                                                           
  Install mysql extension, pip install flask-mysql                                                                             
  Provide DB credentials in your code to connect.                                                                             
  
  from flaskext.mysql import MySQL  
  mysql = MySQL()
  app = Flask(__name__)
  app.config['MYSQL_DATABASE_USER'] = '<username>'
  app.config['MYSQL_DATABASE_PASSWORD'] = '<password>'
  app.config['MYSQL_DATABASE_DB'] = 'flask'
  app.config['MYSQL_DATABASE_HOST'] = 'localhost'
  mysql.init_app(app)



