from flask import Flask, request, render_template
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'rk'
app.config['MYSQL_DATABASE_PASSWORD'] = '8051'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/save')
def save():
    userId = request.args.get('userId')
    userName = request.args.get('userName')
    userPost = request.args.get('userPost')
    userKey = request.args.get('userKey')

    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Users where userId='" + userId + "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"

@app.route('/')
@app.route('/<us>')
def index(us=None):
    num = ['1','2','3']
    return render_template('us.html', us=us,num=num)

@app.route('/users',methods=['GET'])
def users():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Users")
    data = cursor.fetchall()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully" + str(data)
    #return render_template('post.html')

@app.route('/save1',methods=['GET'])
def save1():
    return render_template('post.html')

@app.route('/save1',methods=['POST'])
def save2():

    userId = request.form['userId']
    userName = request.form['userName']
    userPost = request.form['userPost']
    userKey = request.form['userKey']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("insert into Users values(" + userId + ",'" + userName + "','" + userPost + "')")
    data = cursor.rowcount
    print(data)
    conn.commit()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"

@app.route('/edit',methods=['POST'])
def edit1():

    userId = request.form['userId']
    userName = request.form['userName']
    userPost = request.form['userPost']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where userId='" + userId + "'")
    data = cursor.fetchone()
    if data is None:
        return "No Id is present"
    else:
        cursor.execute("update User set username='" + userName + "', userpost='" + userPost + "' where userId='" + userId + "'")
        return "Logged in successfully"

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