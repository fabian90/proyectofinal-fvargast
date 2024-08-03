# db.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.ingrediente import Ingrediente
from models.tipoVaso import TipoVaso
from models.productoIngrediente import ProductoIngrediente
from models.producto import Producto