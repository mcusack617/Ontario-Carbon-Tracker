from flask import Flask, render_template,request,redirect, url_for,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'wdjrfbhibjksdsdzcx'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.permanent_session_lifetime = timedelta(hours=1)

db = SQLAlchemy(app)

@app.route("/",methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('home.html')

@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        return redirect(url_for('cfp'))
    else:
        if ('username' in session) and ('password' in session):
            return redirect(url_for('cfp'))
        return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/cfp')
def cfp():
    if ('username' in session) and ('password' in session):
        return render_template('cfp.html')
    else:
        flash('Login First','error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username',None)    
    session.pop('password',None)
    flash('You have been logged out','info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)