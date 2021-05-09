from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')
if __name__ == "__main__":
    app.run(debug = True)