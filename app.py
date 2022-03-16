from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "it's working"

@app.route("/chocoletier")
def home():
    return render_template("index.html")

@app.route("/chocoletier/products")
def products():
    return render_template("products.html")

@app.route("/chocolotier/productsdetails/<product>")
def getProduct(product: str):
    return render_template("productDetails.html", productName = product)

@app.route("/chocoletier/contact")
def contact():
    return render_template("contact.html")