from flask import Flask, render_template 
  
app = Flask(__name__) 
  
@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/about') 
def about(): 
    return render_template('about.html')
  

@app.route('/contact') 
def contact(): 
    return 'Please contact us at this email address.'


@app.route('/me') 
def me(): 
    return render_template("index.html", name='Soushiyan', age=15)


@app.route('/calc/<int:a>/<int:b>')
def calc(a, b):
    return str(a + b)


@app.route('/subjects')
def subjects():
    topics = ['math', 'physic', 'science']
    return render_template('subjects.html', topics=topics)


@app.route("/hobbies")
def hobbies():
    hobbies_list = ["Fencing", "Reading", "Video Games"]
    return render_template("hobbies.html", hobbies=hobbies_list)


if __name__ == '__main__': 
    app.run(debug=True) 