from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridca import PessoaJuridicaTable
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJurdicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_pessoa_jurifica(self,
                                faturamento: float,
                                idade: int,
                                nome_fantasia: str,
                                celular: str,
                                email_corporativo: str,
                                categoria: str,
                                saldo: float
                                 ) -> None:
        with self.__db_connection as database:
            try:
                pessoa_juridica_data = PessoaJuridicaTable(
                                                            faturamento = faturamento,
                                                            idade = idade,
                                                            nome_fantasia = nome_fantasia,
                                                            celular = celular,
                                                            email_corporativo = email_corporativo,
                                                            categoria = categoria,
                                                            saldo = saldo
                                                            )
                database.session.add(pessoa_juridica_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_pessoas_juridicas(self) -> List:
        with self.__db_connection as database:
            try:
                pessoas_juridicas = (database.session
                                        .query(PessoaJuridicaTable)
                                        .all()
                                    )
                return pessoas_juridicas
            except NoResultFound:
                return []

    def delete_pessoa_juridica(self, pessoa_juridica_id: int) -> None:
        with self.__db_connection as database:
            try:
                result = (database.session
                            .query(PessoaJuridicaTable)
                            .filter(PessoaJuridicaTable.id == pessoa_juridica_id)
                            .delete()
                        )
                database.session.commit()

                return result
            except Exception as exception:
                database.session.rollback()
                raise exception
