from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do SQLAlchemy.
# Nossos modelos irão herdar desta classe 'db.Model'.
db = SQLAlchemy()