import sqlite3
from flask import Flask, session, render_template, redirect, url_for, request
app = Flask('app')
app.secret_key = "VENDINGMACHINE"

@app.route('/', methods=['GET', 'POST'])
def home():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  if request.method == 'POST':
    if 'username' in session:
      a_name = request.form['a_name']
      a_type = request.form['a_type']
      a_price = request.form['a_price']
      a_quantity = request.form['a_quantity']
      if (int)(a_quantity) > 0:
        cart = session['cart']
        for product in cart:
          if product['name'] == a_name:
            if product['quantity'] + 1 <= (int)(a_quantity):
              new_quantity = product['quantity'] + 1
              product['quantity'] = new_quantity
              session['cart'] = cart
            return ('', 204)
        product = {"name" : a_name, "type" : a_type, "price" : a_price, "quantity" : 1}
        cart.append(product)
        session['cart'] = cart
        return ('', 204)
  return render_template('home.html', games=games, login=login, game_types=game_types)

@app.route('/console/<gametype>', methods=['GET', 'POST'])
def console(gametype):
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games WHERE type=(?)", (gametype, ))
  specific_games = cursor.fetchall()
  connection.commit()
  connection.close()
  if request.method == 'POST':
    if 'username' in session:
      a_name = request.form['a_name']
      a_type = request.form['a_type']
      a_price = request.form['a_price']
      a_quantity = request.form['a_quantity']
      cart = session['cart']
      for product in cart:
        if product['name'] == a_name:
          if product['quantity'] + 1 <=(int)(a_quantity):
            new_quantity = product['quantity'] + 1
            product['quantity'] = new_quantity
            session['cart'] = cart
          return ('', 204)
      product = {"name" : a_name, "type" : a_type, "price" : a_price, "quantity" : 1}
      cart.append(product)
      session['cart'] = cart
      return ('', 204)
  return render_template('console.html', gametype=gametype, games=games, specific_games=specific_games, login=login, game_types=game_types)

@app.route('/login', methods=['GET', 'POST'])
def login():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  error = False
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  if request.method == 'POST':
    uname = request.form['field_name']
    password = request.form['field_password']
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    for user in users:
      if uname == user['username']:
        if password == user['password']:
          session['username'] = user['username']
          session['cart'] = []
          session['user_name'] = user['name']
          login = False
          if 'username' in session:
            login = True
          return render_template('home.html', games=games, login=login, game_types=game_types)   
    error = True
    login = False
    if 'username' in session:
      login = True
  return render_template("login.html", error=error, games=games, login=login, game_types=game_types)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  # Log the user out and redirect them to the login page
  session.pop('username', None)
  session.pop('cart', None)
  session.clear()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  return render_template("home.html", games=games, login=login, game_types=game_types)

@app.route('/createaccount', methods=['GET', 'POST'])
def create():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  error = False
  created = False
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  if request.method == 'POST':
    name = request.form['field_name']
    username = request.form['field_username']
    password = request.form['field_password']
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)", (username, password, name))
    connection.commit()
    connection.close()  
    error = True
    created = True
    login = False
    if 'username' in session:
      login = True
  return render_template("create.html", error=error, games=games, created=created, login=login, game_types=game_types)

@app.route('/search', methods=['GET', 'POST'])
def search():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  query = "%"+request.args.get("query")+"%"
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games WHERE title LIKE ?", (query, ))
  specific_games = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  gametype = "Search"
  if 'username' in session:
    login = True
  return render_template('console.html', gametype=gametype, games=games, specific_games=specific_games, login=login, game_types=game_types)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  if request.method == 'POST':
    if request.form['submit'] == 'Checkout': 
      for game in games:
        for product in session['cart']:
          if(product['name'] == game['title']):
            connection = sqlite3.connect("myDatabase.db")
            connection.row_factory = sqlite3.Row 
            cursor = connection.cursor()
            new_quantity = (int)(game['quantity']) - (int)(product['quantity'])
            cursor.execute("UPDATE games SET quantity = ? WHERE title = ?", (new_quantity, game['title']))
            games = cursor.fetchall()
            connection.commit()
            connection.close()
            connection = sqlite3.connect("myDatabase.db")
            connection.row_factory = sqlite3.Row 
            cursor = connection.cursor()
            new_quantity = (int)(game['quantity']) - (int)(product['quantity'])
            cursor.execute("INSERT INTO orders(title, price, type, quantity) VALUES(?, ?, ?, ?)", (game['title'], game['price'], game['type'], product['quantity']))
            games = cursor.fetchall()
            connection.commit()
            connection.close()
      session['cart'] = []
    elif request.form['submit'] == 'Clear':
      session.pop('cart', None)
      session['cart'] = []
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  return render_template('cart.html', games=games, login=login, game_types=game_types)

@app.route('/orderhistory', methods=['GET', 'POST'])
def orderhistory():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM gametypes")
  game_types = cursor.fetchall()
  connection.commit()
  connection.close()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM games")
  games = cursor.fetchall()
  connection.commit()
  connection.close()
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM orders")
  orders = cursor.fetchall()
  connection.commit()
  connection.close()
  login = False
  if 'username' in session:
    login = True
  return render_template('orderhistory.html', orders=orders, games=games, login=login, game_types=game_types)
  
app.run(host='0.0.0.0', port=8080)
