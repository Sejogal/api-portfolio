from models import db
from sqlalchemy.orm import sessionmaker #permitir criação de sessão


def criarSessao():
    try:
        sessao =  sessionmaker(bind=db)

        Sessao = sessao() #iniciando uma sessão, usado para fazer busca no banco de dados de forma correta
    
        yield Sessao
    finally:
        Sessao.close()