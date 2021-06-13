import databases
import sqlalchemy

import settings

metadata = sqlalchemy.MetaData()

ArticlesTable = sqlalchemy.Table(
    'Articles',
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("content", sqlalchemy.Text)
)

database = databases.Database(settings.DATABASE_URL)
engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
