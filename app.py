from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response 
  
app = Flask(__name__) 
app.secret_key = "my_secret_key"

@app.route('/') 
def home(): 
    session['visits'] = session.get('visits', 0) + 1
    return f'You have visited this page {session["visits"]} times.'

@app.route('/add/<item>')
def add_to_cart(item):
    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart

    return f"{item} was added to the cart. Current cart: {cart}"

@app.route("/remove/<item>")
def remove_from_cart(item):
    cart = session.get('cart', [])

    if item in cart:
        cart.remove(item)
        session['cart'] = cart
        return f"{item} was removed from the cart."

    return f"{item} is not in the cart."
    

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', items=cart)


@app.route('/clear-cart')
def clear_cart():
    session.pop('cart', None)
    return "Cart has been cleared."

@app.route('/set-theme/<theme>')
def set_theme(theme):
    response = make_response(f"Theme changed to {theme}.")
    response.set_cookie('theme', theme, max_age=60 * 60 * 24 * 30)
    return response

@app.route('/show-theme')
def show_theme():
    theme = request.cookies.get('theme', 'light')
    return f"Your current theme is: {theme}"

@app.route("/add-score")
def add_score():
    score = session.get('score', 0)
    score += 10
    session['score'] = score

    return "Score increased"


@app.route("/score")
def score():
    score = session.get('score', 0)
    
    return f"Score is {score}"

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

@app.route('/register', methods=['GET', 'POST']) 
def register(): 
    if request.method == 'POST': 
        username = request.form.get('username') 
        age = request.form.get('age')
        
        if not username: 
            flash('You did not enter a username!', 'error')
            return redirect(url_for('register'))
        
        if len(username) < 5:
            flash("Username must be at least 5 characters long.", "error")
            return redirect(url_for("register")) 
        
        if not age:
            flash("You did not enter your age!", "error")
            return redirect(url_for("register"))

        if not age.isdigit():
            flash("Age must be a number.", "error")
            return redirect(url_for("register"))
        
        flash(f'✅ Registration completed successfully. Welcome, {username}!', 'success')
        return redirect(url_for('register')) 
    
    return render_template('register.html') 

@app.route('/search') 
def search(): 
    topics = ["python", "html", "css"]
    query = request.args.get('q', '') 
    if query:
        results = []
        for topic in topics:
                if query in topic:
                    results.append(topic)

        return f"Search results: {results}"
    return "You didn't enter anything to search."


if __name__ == '__main__': 
    app.run(debug=True) 