from typing import List # Python 3.8
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_pessoa_fisica(self,
                             renda_mensal: float,
                             idade: int,
                             nome_completo: str,
                             celular: str,
                             email: str,
                             categoria: str,
                             saldo: float
                             ) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = PessoaFisicaTable(
                                                    renda_mensal = renda_mensal,
                                                    idade = idade,
                                                    nome_completo = nome_completo,
                                                    celular = celular,
                                                    email = email,
                                                    categoria = categoria,
                                                    saldo = saldo
                                                  )
                database.session.add(pessoa_fisica_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_pessoa_fisica(self) -> List[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoas_fisicas = (database.session
                                        .query(PessoaFisicaTable)
                                        .all()
                                  )
                return pessoas_fisicas
            except NoResultFound:
                return []

    def delete_pessoa_fisica(self, pessoa_fisica_id: int) -> None:
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
