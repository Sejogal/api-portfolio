from fastapi import APIRouter, Depends
from schemas import messageSchemas
from dependecies import criarSessao
from models import messagem

formulario_router = APIRouter(prefix="/formulario", tags=["Formulário"])

@formulario_router.post("/enviar")
async def enviar(messageSchemas: messageSchemas, Session = Depends(criarSessao) ):
    nova_message = messagem(
        nome=messageSchemas.nome,
        email=messageSchemas.email,
        texto=messageSchemas.texto
    )

    Session.add(nova_message)
    Session.commit()
    Session.refresh(nova_message)

    return{
        "message":"sucesso!"
    }


@formulario_router.get("/receber")
async def receber(Session = Depends(criarSessao)):
    resposta = Session.query(messagem).all()

    return{
        "resposta": resposta
    }