from flask import Flask, request, render_template

app = Flask(__name__)

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
        return render_template("login.html")
    else:
        print("in POST request")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        print("in POST request")


if __name__ == "__main__":
    app.run(debug=True)

