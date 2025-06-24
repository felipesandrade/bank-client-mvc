from sqlalchemy import Column, String, BIGINT, Integer, REAL
from src.models.sqlite.settings.base import Base

class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key = True)
    renda_mensal =  Column(REAL)
    idade = Column(Integer)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self):
        return f"Pessoa física [nome_completo={self.nome_completo}, email={self.email}]"
