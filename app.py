from flask import Flask, render_template ,request

app = Flask(__name__)


@app.route('/')
def hello():
   
    return render_template("Index.html")

 



    

@app.route("/contact")
def contactus():
    return render_template("contact.html") 




@app.route('/Products/<name>')
def Products (name:str):
   
    return render_template("Products.html",name=name)   




 
