from typing import List # Python 3.8
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoas_fisicas(self) -> List[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = (database.session
                                        .query(PessoaFisicaTable)
                                        .all()
                                  )
                return pessoas_fisicas
            except NoResultFound:
                return []

    def delete_pessoa_fisica(self, pessoa_fisica_id: int) -> int:
        with self.__db_connection as database:
            try:
                result = (database.session
                                .query(PessoaFisicaTable)
                                .filter(PessoaFisicaTable.id == pessoa_fisica_id)
                                .delete()
                         )
                database.session.commit()
                return result
            except Exception as exception:
                database.session.rollback()
                raise exception
