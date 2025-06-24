# from sqlalchemy.ext.declarative import declarative_base (old versão antiga < 1.8)
from sqlalchemy.orm import declarative_base

# Criando uma base declarativa para informar ao SQLAlchemy os elementos de armazenamento
Base = declarative_base()
