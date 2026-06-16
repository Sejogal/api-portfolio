from pydantic import BaseModel, ConfigDict

class messageSchemas(BaseModel):
    nome: str
    email: str
    texto: str

    class config :
        from_attributes = True