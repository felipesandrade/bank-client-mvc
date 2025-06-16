from sqlalchemy import create_engine

# Create database and view logs
engine = create_engine('sqlite:///storage.db', echo=True)

# Connect to create storage.db file
with engine.connect() as conn:
    pass
