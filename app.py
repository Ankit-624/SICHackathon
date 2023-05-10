from flask import Flask , render_template , redirect
import requests
from json import loads

app = Flask(__name__)


@app.route('/')
def portal():
    return  render_template('portal.html') 

@app.route('/index/')
def naya():
    return  render_template('index.html') 

@app.route('/login')
def nayaa():
    return  render_template('login.html')

@app.route('/query')
def nayaaa():
    return  render_template('query.html')

@app.route('/malogin')
def new():
    return  render_template('malogin.html')


@app.route('/admission')
def hello_world():
    return  render_template('admission.html') 
@app.route('/Link')
def link(): 
 return redirect("https://drive.google.com/drive/folders/1Z4KU-sOnIztqSCEro8Or7AwtMC_Mw2eB")

@app.route('/semster12')
def smeseter(): 
 return redirect("https://drive.google.com/file/d/1Wn4ikoPyTpsRHDR3lIEa1TmdI37uRcWy/view?usp=share_link")

@app.route('/semster34')
def sem34(): 
 return redirect("https://drive.google.com/file/d/17vCnrsflr4NKKTHURaES6lLX52YJZczy/view?usp=share_link")

@app.route('/semster56')
def sem56(): 
 return redirect("https://drive.google.com/file/d/1MYq43qlAG-BtEci_mxxY8OTR4ymq5a7s/view?usp=share_link")

@app.route('/semster78')
def sem78(): 
 return redirect("https://drive.google.com/file/d/1KDkhHDTE9i5XWt-Lq_SWapANysS4iSWH/view?usp=share_link")








if __name__ == '__main__':
    app.run(debug=True)