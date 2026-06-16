from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base

db =  create_engine("sqlite:///banco.db")

base = declarative_base()

class messagem(base):
     __tablename__ = "messagem"

     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
     nome = Column("nome", String)
     email = Column("email", String)
     texto = Column("texto", String)

     def __init__(self, nome, email, texto):
          self.nome = nome
          self.email = email
          self.texto = texto