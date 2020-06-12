from flask import Flask, request, render_template, redirect, session
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key='secret123'


# Config the database.
if 'DB_USER' in os.environ :
    app.config["MYSQL_HOST"] = os.environ['DB_HOST']
    app.config["MYSQL_USER"] = os.environ['DB_USER']
    app.config["MYSQL_PASSWORD"] = os.environ['DB_PASSWORD']
    app.config["MYSQL_DB"] = os.environ['DB_NAME']
else :
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "M01019056637m"
    app.config["MYSQL_DB"] = "power_gym"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# Define a function to fetch data from the database.
def FetchFromTheDatabse(executeString):

    # Start connection with the database.
    cur = mysql.connection.cursor()

    # Fetch from the database.
    cur.execute(executeString)
    targetRows = cur.fetchall()

    # Close the connection with the database.
    cur.close()

    return targetRows


# Define a function to fetch data from the database with value.
def FetchFromTheDatabseWithValue(executeString, values):

    # Start connection with the database.
    cur = mysql.connection.cursor()

    # Fetch from the database.
    cur.execute(executeString, [values])
    targetRows = cur.fetchall()

    # Close the connection with the database.
    cur.close()

    return targetRows


# Define a function to put changes in the database.
def PutChangesInDatabase(executeString, values):
    cur = mysql.connection.cursor()

    cur.execute(executeString, values)
    mysql.connection.commit()

    cur.close()


@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html", home=True)


@app.route("/about-us")
def AboutUs():
    return render_template("about-us.html", aboutUs=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", formPage=True)
    else:

        # Clear session
        session.clear()

        # Get the request args
        email = request.form.get('email')
        password = request.form.get('password')

        userRow = FetchFromTheDatabseWithValue("SELECT * FROM users WHERE email = %s", email)

        # Check the validathion of fields
        if not userRow:
            return render_template("login.html", formPage=True, error="Invalid email. Try again")

        if not sha256_crypt.verify(password, userRow[0]['password']):
            return render_template("login.html", formPage=True, error="Tha passwprd in incorrect. Try again")
        
        session['user_row'] = userRow[0]

        print(session)

        return redirect('/')



@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html", formPage=True)
    else:
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = str(request.form.get('password'))
        confirm = str(request.form.get('confirm'))

        # Check the correctness of the form fields.
        if not 1 < len(name) < 50:
            return render_template("register.html", formPage=True, error="Invalid name. Try again")

        if not 8 < len(phone) < 28:
            return render_template("register.html", formPage=True, error="Invalid phone number. Try again")

        if len(email) > 50:
            return render_template("register.html", formPage=True, error="Invalid Email. Try again")

        if len(password) < 3:
            return render_template("register.html", formPage=True, error="The password is too short. Try again") 
        
        if len(password) > 50:
            return render_template("register.html", formPage=True, error="The password is too long. Try again") 

        if password != confirm:
            return render_template("register.html", formPage=True, error="Passwords didn't mach. Try again")

        if FetchFromTheDatabseWithValue("SELECT email FROM users WHERE email = %s", email):
            return render_template("register.html", formPage=True, error="The email is already used. Try again")

        PutChangesInDatabase("INSERT INTO users(name, phone, email, password) VALUES(%s, %s, %s, %s)", (name, phone, email, sha256_crypt.encrypt(password)))

        return redirect("/login")


@app.route("/contact-us", methods=['GET', 'POST'])
def contactUs():
    if request.method == "GET":
        return render_template("contact-us.html", contactUs=True)
    else:
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        if len(email) > 45:
            return render_template("contact-us.html", contactUs=True, error="Invalid email")
        if len(phone) > 25:
            return render_template("contact-us.html", contactUs=True, error="Invalid phone")
        
        PutChangesInDatabase("INSERT INTO contact_info(email, phone, message) VALUES(%s, %s, %s)", (email, phone, message))

        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

