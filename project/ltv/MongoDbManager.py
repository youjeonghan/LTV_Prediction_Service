import os
import pymongo
from dotenv import load_dotenv


class MongoDbManager:
    _instance = None
    load_dotenv(verbose=True)
    print("--------------------------MongoDbManager 선언-------------------------")
    client = pymongo.MongoClient(
        host=os.getenv("host"),
        port=27017,
        username=os.getenv("user"),
        password=os.getenv("password"),
        authSource="Capstone",
    )

    database = client["Capstone"]["cleaned_forweb"]
    database_len = database.count()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def db(cls):
        return cls.database

    def get_users_from_collection(cls, _query):
        assert cls.database
        return cls.database.find(_query).limit(10)
