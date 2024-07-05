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
#    return render_template('index.html')
    return redirect('/all')
    
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
    

    prods = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
    return render_template('addprod.html', stuff=prods)

@app.route('/delproduct/<int:prodid>', methods=['POST', 'GET'])
def delproduct(prodid):
    if request.method != 'POST':
        del_product = db.session.query(Products).filter_by(id = prodid).one()
        print(del_product)
        db.session.delete(del_product)
        db.session.commit()

    return redirect('/addprod')

@app.route('/addprodm', methods=['POST', 'GET'])
def addprodm():
    prod = request.get_json()
    print("hello from modal")
    print(prod)

    if request.method == 'POST':
        name = prod['name']
        description = prod['description']
        price = prod['price']

        print(name)
        product = Products(name=name, description=description, price=price)
        print(product)
        #try:
        db.session.add(product)
        db.session.commit()

    products = db.session.execute(db.select(Products).order_by(Products.name)).scalars()
    return render_template('addprodm.html', stuff=products)

@app.route('/addloc', methods=['POST', 'GET'])
def addloc():
    if request.method == 'POST':
        name = request.form['name']
        location = Locations(name=name)
        db.session.add(location)
        db.session.commit()
    
    locs = db.session.execute(db.select(Locations).order_by(Locations.name)).scalars()
    return render_template('addloc.html', stuff=locs)

@app.route('/dellocation/<int:locid>', methods=['POST', 'GET'])
def dellocation(locid):
    if request.method != 'POST':
        del_location = db.session.query(Locations).filter_by(id = locid).one()
        print(del_location)
        db.session.delete(del_location)
        db.session.commit()

    return redirect('/addloc')


@app.route('/addlocationmodal', methods=['POST', 'GET'])
def addlocationsm():
    prod = request.get_json()
    print("hello from adding location modal")
    print(prod)

    if request.method == 'POST':
        name = prod['name']

        print(name)
        new_location = Locations(name=name)
        print(new_location)
        #try:
        db.session.add(new_location)
        db.session.commit()

    all_locations = db.session.execute(db.select(Locations).order_by(Locations.name)).scalars()
    return render_template('addlocationsm.html', stuff=all_locations)


from sqlalchemy import text, and_

@app.route('/addtostore', methods=['POST', 'GET'])
def addtostore():
    inventory = db.session.execute(db.select(Products))
    locs = db.session.execute(db.select(Inventory, Locations).join(Inventory, and_(Inventory.location_id == Locations.id, Inventory.product_id == 12), isouter=True).where(Inventory.product_id == None))
    return render_template('addtostore.html', stuff=inventory, stores=locs)
    
@app.route('/getfreelocations/<int:pid>', methods=['POST', 'GET'])
def addtostoreloc(pid):
    if request.method == 'GET':
        locs = db.session.execute(db.select(Inventory, Locations).join(Inventory, and_(Inventory.location_id == Locations.id, Inventory.product_id == pid), isouter=True).where(Inventory.product_id == None))
        return render_template('freelocations.html', stores = locs, pid=pid)
    else:
        loc_id = request.form['location_id']
        amount = request.form['amount']
        inventory = Inventory(product_id=pid, location_id=loc_id, quantity=amount)
        #try:
        db.session.add(inventory)
        db.session.commit()
        return redirect('/all')

if __name__ == '__main__':
    app.run(debug=True)