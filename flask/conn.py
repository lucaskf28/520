from pymongo import MongoClient
from psycopg2 import connect as cn

def mongo_connect():
    con = MongoClient()
    return con['projeto']

def psy_connect(user, pw, base):
    con = cn("host=localhost user={} password={} dbname={}".format('lucas', '123456', 'fundamentals'))
    return con.cursor()