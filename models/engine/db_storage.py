from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base




class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        self.__session = sessionmaker(bind=self.__engine)
        sess = self.__session()
        