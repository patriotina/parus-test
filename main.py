from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from model import Products, Locations, Inventory, db

print("Hello Parus")

#db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dbpass3322@localhost/parus1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invenory.db'
db.init_app(app)

@app.route('/')
def hello():
#    return 'Hello World!'
    return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = int(request.form['price'])

        product = Products(name=name, description=description, price=price)
        #try:
        db.session.add(product)
        db.session.commit()
        return redirect('/')
        #except:
        #    return 'Error while adding data to db'
    else:
        return render_template('create.html')
    
@app.route('/products')
def getrpoducts():
    products = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
    return render_template('products.html', products=products)

@app.route('/all')
def getall():
    allprods = db.session.execute(db.select(Inventory, Products, Locations).join(Products).join(Locations))
    return render_template('all.html', stuff = allprods)

@app.route('/additem/<int:invid>')
def additem(invid, methods=['POST', 'GET']):
    inventory = db.session.execute(db.select(Inventory).filter_by(id = invid)).scalar_one()
    inventory.quantity += 1
    db.session.commit()

    return redirect('/all')

@app.route('/delitem/<int:invid>')
def delitem(invid):
    inventory = db.session.execute(db.select(Inventory).filter_by(id = invid)).scalar_one()
    
    if inventory.quantity > 0:
        inventory.quantity -= 1
    db.session.commit()

    return redirect('/all')

@app.route('/addprod', methods=['POST', 'GET'])
def addprod():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = int(request.form['price'])

        product = Products(name=name, description=description, price=price)
        #try:
        db.session.add(product)
        db.session.commit()
    

    prods = db.session.execute(db.select(Products)).scalars()
    return render_template('addprod.html', stuff=prods)

@app.route('/addloc', methods=['POST', 'GET'])
def addloc():
    if request.method == 'POST':
        name = request.form['name']
        location = Locations(name=name)
        db.session.add(location)
        db.session.commit()
    
    locs = db.session.execute(db.select(Locations)).scalars()
    return render_template('addloc.html', stuff=locs)

if __name__ == '__main__':
    app.run(debug=True)