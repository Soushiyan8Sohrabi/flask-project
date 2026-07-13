from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/') 
def home(): 
    return 'Hi! my name is Soushiyan. My first website is working with Flask.'
@app.route('/about') 
def about(): 
    return 'This page is about us.' 
  
@app.route('/contact') 
def contact(): 
    return 'Please contact us at this email address.'

@app.route('/me') 
def me(): 
    return 'My first name is Soushiyan and my last name is Sohrabi. I am a programmer' 

@app.route('/calc/<int:a>/<int:b>')
def calc(a, b):
    return str(a + b)

if __name__ == '__main__': 
    app.run(debug=True) 