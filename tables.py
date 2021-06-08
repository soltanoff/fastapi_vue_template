import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ArticlesTable(Base):
    __tablename__ = 'Articles'

    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column("title", sqlalchemy.String)
    content = sqlalchemy.Column("content", sqlalchemy.Text)
