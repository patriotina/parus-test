from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    #id = Column(Integer, nullable = False, unique = True, primary_key = True, autoincrement = True) #(тип данных - INTEGER, PRIMARY KEY)
    # name = Column(String(50)) #(тип данных - STRING(50))
    # description = Column(Text) #(тип данных - TEXT)
    # price = Column(Float) #(тип данных - FLOAT или DECIMAL)
    
class Locations(Base):
    __tablename__ = 'locations'
    # id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True) #(тип данных - INTEGER, PRIMARY KEY)
    # name = Column(String(50)) #(тип данных - STRING(50))
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: Mapped[str]
    
class Inventory(Base):
    __tablename__ = 'inventory'
    # id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True) #(тип данных - INTEGER, PRIMARY KEY)
    # product_id = Column(Integer, ForeignKey('Products.id')) #(тип данных - INTEGER, FOREIGN KEY)
    # location_id = Column(Integer, ForeignKey('Locations.id')) #(тип данных - INTEGER, FOREIGN KEY)
    # quantity = Column(Integer) #(тип данных - INTEGER)
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    location_id: Mapped[int] = mapped_column(ForeignKey('locations.id'))
    quantity: Mapped[int]


