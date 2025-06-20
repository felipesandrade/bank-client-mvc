from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) ->  None:
        # Criando a coneão com o banco de dados SQLite
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    def connect_to_db(self):
        # Criando o motor de conexão passando a string de conexão
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        # Retornando a engine de conexão
        return self.__engine

db_connection_handler = DBConnectionHandler()
