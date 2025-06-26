from sqlalchemy import Column, String, BIGINT, REAL, Integer
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL)
    idade = Column(Integer)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self):
        return f"Pessoa jurídica [nome_fantasia ={self.nome_fantasia}]"
