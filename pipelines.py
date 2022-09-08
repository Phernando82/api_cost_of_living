# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class NumbeoSpiderPipeline:
    def process_item(self, item, spider):
        return item


class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('numbeo.db')
        self.cursor = self.connection.cursor() # permite fazer pesquisa
        # Criar a tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cities(
                id_city INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                common_meal TEXT,
                meal_for_two TEXT,
                one_way_ticket TEXT,
                monthly_pass TEXT,
                gasoline TEXT,
                base_cost TEXT,
                internet TEXT,
                simple_apartment_centre TEXT,
                simple_apartment_outside TEXT,
                large_apartment_centre TEXT,
                large_apartment_outside TEXT,
                salary TEXT,
                status TEXT
            )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO cities(name,common_meal,meal_for_two,one_way_ticket,monthly_pass,gasoline,base_cost,internet,simple_apartment_centre,simple_apartment_outside,large_apartment_centre,large_apartment_outside,salary,status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
            item.get('name'),
            item.get('common_meal'),
            item.get('meal_for_two'),
            item.get('one_way_ticket'),
            item.get('monthly_pass'),
            item.get('gasoline'),
            item.get('base_cost'),
            item.get('internet'),
            item.get('simple_apartment_centre'),
            item.get('simple_apartment_outside'),
            item.get('large_apartment_centre'),
            item.get('large_apartment_outside'),
            item.get('salary'),
            item.get('status'),
        ))
        self.connection.commit()
        return item

