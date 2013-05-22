# -*- coding: utf-8 -*-
# http://try.taobao.com/json/ajax_get_item_list.htm?tab=2&page=13&anchor=true&t=1367128346939&_input_charset=utf-8

import urllib2
import time
import json
import pymongo

mongo_con = pymongo.Connection("192.168.1.55", 27017)
mongo_db = mongo_con.taobao
# mongo_db.authenticate("redhat", "3.14159")
from pybean import Store, SQLiteWriter
db = Store(SQLiteWriter("taobao.db", frozen=False))


def getList(page):
        # page >=1
    print "page:", page
    url = "http://try.taobao.com/json/ajax_get_item_list.htm?tab=2&page=%s&anchor=true&t=1367128346939&_input_charset=utf-8" % (
        page,)
    js = urllib2.urlopen(url).read()
    items = json.loads(js)
    now = time.time()
    tm = time.gmtime(now + 8 * 3600)
    date = tm.tm_year * 10000 + tm.tm_mon * 100 + tm.tm_mday
    for item in items["data"]:
        print item["itemId"]
        tb = db.new("freetry")
        for key in item:
            tb.__setattr__(key, item[key])
        # tb.uuid = item["itemId"]
        tb.gailv = item["requestNum"] / item["totalNum"]
        item["_id"] = item["itemId"]
        item["gailv"] = item["requestNum"] / item["totalNum"]
        if db.find_one("freetry", "itemId=?", (item["itemId"],)):
            print "skip..."
            continue
        if item["gailv"] > 0:
            item["createtime"] = now
            item["date"] = date
            tb.date = date
            tb.createtime = now
            mongo_db.tabaotry.save(item)
            db.save(tb)


if __name__ == '__main__':
    for x in xrange(1, 3):
        getList(x)
        time.sleep(5)
    for book in db.find("freetry", "1 order by date desc,gailv  limit 0,5"):
        print 'find'
        print book.itemId, book.gailv, book.createtime
        # print tojson(book)
