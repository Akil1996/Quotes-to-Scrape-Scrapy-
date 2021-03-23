import pymongo

class QuotesPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['my_quotes']
        self.collection = db['quotes_db']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
#

import sqlite3
import mysql.connector

# class QuotesPipeline:
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         # self.conn = sqlite3.connect("myquotes.db")
#         # self.curr = self.conn.cursor()
#
#
#         self.conn = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             passwd = "Akil@2007",
#             database = "my_quotes",
#             auth_plugin='mysql_native_password'
#         )
#         self.curr = self.conn.cursor()
#
#     def create_table(self):
#
#         # self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         # self.curr.execute("""create table quotes_tb(
#         #                     title text,
#         #                     author text,
#         #                     tag text)""")
#
#
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         self.curr.execute("""create table quotes_tb(
#                                     title text,
#                                     author text,
#                                     tag text)""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         # print("pipe", item['title'])
#         return item
#
#     def store_db(self, item):
#         # self.curr.execute("""insert into quotes_tb values(?,?,?)""",
#         #                   (item['title'][0],
#         #                    item['author'][0],
#         #                    item['tag'][0]))
#         # self.conn.commit()
#
#
#         self.curr.execute("""insert into quotes_tb values(%s,%s,%s)""",
#                           (item['title'][0],
#                            item['author'][0],
#                            item['tag'][0]))
#         self.conn.commit()