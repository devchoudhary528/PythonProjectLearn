# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class ToscrapeBookPipeline(object):
    def process_item(self, item, spider):
        return item

class BookPipeline(object):
    review_rating_map = {
       'One':     1,
       'Two':     2,
       'Three':  3,
       'Four':   4,
       'Five':   5,
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]
        return item


class SQLitePipeline(object):
  
  def open_spider(self, spider):
     db_name = spider.settings.get('SQLITE_DB_NAME', 'scrapy_defaut.db')
     self.db_conn = sqlite3.connect(db_name)
     self.db_cur = self.db_conn.cursor()

  def close_spider(self, spider):
     print('#'*20, 'close and commit')
     self.db_conn.commit()
     self.db_conn.close()


  def process_item(self, item, spider):
     self.insert_db(item)
     return item

  def insert_db(self, item):
     values = (
        item['upc'],
        item['name'],
        item['price'],
        item['review_rating'],
        item['review_num'],
        item['stock'],
     )
     sql = 'INSERT INTO books VALUES (?,?,?,?,?,?)'
     self.db_cur.execute(sql, values)
     # 每插入一条就commit一次会影响效率
     # self.db_conn.commit()
    # 每插入一条就commit一次会影响效率
     # self.db_conn.commit()


