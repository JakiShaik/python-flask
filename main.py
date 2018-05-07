from flask import Flask, request, render_template, redirect
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = '<username>'
app.config['MYSQL_DATABASE_PASSWORD'] = '<password>'
app.config['MYSQL_DATABASE_DB'] = '<database>'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/search')
def search():
    userId = request.args.get('userId')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Users where userId='" + userId + "'")
    data = cursor.fetchone()
    if data is None:
        return redirect('/users')
    else:
        return render_template('update.html',user=data)

@app.route('/')
@app.route('/<login>')
def index(login=None):
    num = ['1','2','3']
    return render_template('login.html', login=login,num=num)

@app.route('/users',methods=['GET'])
def users():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Users")
    data = cursor.fetchall()
    return render_template('users.html',users= data)

@app.route('/create',methods=['GET'])
def save1():
    return render_template('create.html')

@app.route('/create',methods=['POST'])
def save2():
    userId = request.form['userId']
    userName = request.form['userName']
    userPost = request.form['userPost']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("insert into Users values(" + userId + ",'" + userName + "','" + userPost + "')")
    data = cursor.rowcount
    conn.commit()
    if data is None:
        return redirect("/create", code=302)
    else:
        return redirect("/users", code=302)

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html',user=('','',''))

@app.route('/update',methods=['POST'])
def update1():
    update = request.form['update']

    if update == 'update' :
        #   retrieve userId, userName, userPost and update it to database and redirect to /users
    elif update == 'delete' :
        #   retrieve userId and delete from the database and redirect to /users

@app.route('/a')
def a():
    return "<h2>Hello IDK</h2>"

@app.route('/b',methods=['GET','POST'])
def b():
    if request.method == 'POST':
        return "POST"
    else:
        return 'GET'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/post/<int:post_id>')
def show(post_id):
    return "Hello IDK %s" % post_id

if __name__=="__main__":
    app.run(debug=True)
