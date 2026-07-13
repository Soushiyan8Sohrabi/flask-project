from flask import Flask 
  
app = Flask(__name__) 
  
@app.route('/') 
def home(): 
    return ' کند می کار فلسک با من سایت اولین ! سالم 🎉' 

@app.route('/about') 
def about(): 
    return ' ماست ی درباره ی صفحه  این .' 
  
@app.route('/contact') 
def contact(): 
    return ' بزنید ایمیل آدرس این به ما با تماس  برای .' 

if __name__ == '__main__': 
    app.run(debug=True) 