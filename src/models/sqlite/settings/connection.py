from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) ->  None:
        # Criando a coneão com o banco de dados SQLite
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        # Criando o motor de conexão passando a string de conexão
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        # Retornando a engine de conexão
        return self.__engine

    # Criando uma sessão
    def __enter__(self):
        session_maker = sessionmaker()
        # Session feita a partir do nosso engine
        self.session = session_maker(bind=self.__engine)
        return self

    # Fechando a sessão
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()
