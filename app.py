from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contactus():
    return render_template("contact.html")


@app.route('/Products/<prId>')
def Products( prId : int):

    return render_template('Products.html', productsID=prId)
