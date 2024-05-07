from flask import Flask
from model import Products, Locations, Inventory, Base, db

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dbpass3322@localhost/parus1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invenory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
#        db.create_all()

#       создаем тестовые товары
        # products1 = Products(name='Кружка', description='Кружка с ручкой', price=100)
        # products2 = Products(name='Ложка', description='Ложка метал', price=20)
        # products3 = Products(name='Ложка деревянная', description='Ложка из дерева с узором', price=80)
        # products4 = Products(name='Нож', description='Нож туристический', price=350)
        # products5 = Products(name='Тарелка', description='Тарелка походная', price=120)
        # db.session.add_all([products1, products2, products3, products4, products5])
        # db.session.commit()
       
        # #создаем тестовые локации
        # location1 = Locations(name='Ижевск Пойма')
        # location2 = Locations(name='Ижевск Славянка')
        # location3 = Locations(name='Игра')
        # location4 = Locations(name='Можга')
        # location5 = Locations(name='Сарапул')
        # db.session.add_all([location1, location2, location3, location4, location5])
        # db.session.commit()

        # # создаем позиции товаров
        inventory1 = Inventory(product_id=1, location_id=1, quantity=5)
        inventory2 = Inventory(product_id=1, location_id=4, quantity=3)
        inventory3 = Inventory(product_id=2, location_id=3, quantity=8)
        inventory4 = Inventory(product_id=2, location_id=2, quantity=6)
        inventory5 = Inventory(product_id=2, location_id=1, quantity=4)
        inventory6 = Inventory(product_id=3, location_id=2, quantity=6)
        inventory7 = Inventory(product_id=4, location_id=5, quantity=9)
        inventory8 = Inventory(product_id=4, location_id=5, quantity=7)
        inventory9 = Inventory(product_id=5, location_id=3, quantity=6)
        inventory10 = Inventory(product_id=5, location_id=4, quantity=3)
        db.session.add_all([inventory1, inventory2, inventory3,
                            inventory4, inventory5, inventory6,
                            inventory7, inventory8, inventory9, inventory10,])
        db.session.commit()

