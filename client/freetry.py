# -*- coding: utf-8 -*-
# http://try.taobao.com/json/ajax_get_item_list.htm?tab=2&page=13&anchor=true&t=1367128346939&_input_charset=utf-8

import urllib2
import time
import json

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

        tb.gailv = item["requestNum"] / item["totalNum"]
        # item["_id"] = item["itemId"]
        # item["gailv"] = item["requestNum"] / item["totalNum"]
        if db.find_one("freetry", "itemId=?", (item["itemId"],)):
            print "skip...", item["itemId"]
            continue
        if tb.gailv > 0:
            tb.date = date
            tb.createtime = now
            db.save(tb)


if __name__ == '__main__':
    for x in xrange(1, 50):
        getList(x)
        time.sleep(5)
