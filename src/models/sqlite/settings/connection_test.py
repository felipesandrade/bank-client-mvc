import pytest
from sqlalchemy import Engine
from .connection import db_connection_handler

# caso seja necessário skipar o teste
@pytest.mark.skip(reason="interação com o banco de dados")
def test_connect_to_db():
    # Verifica primeiro se o engine é None
    assert db_connection_handler.get_engine() is None

    # Conecta com o banco de dados
    db_connection_handler.connect_to_db()
    # Pega o engine
    db_engine = db_connection_handler.get_engine()

    # Verifica se o engine não é mais None
    assert db_engine is not None
    # Verifica se db_engine é uma instancia de Engine
    assert isinstance(db_engine, Engine)
