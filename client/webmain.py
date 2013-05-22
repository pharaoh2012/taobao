# -*- coding: utf-8 -*-
from bottle import static_file, abort, Bottle, run
import pymongo
import json
import urllib2
from pybean import Store, SQLiteWriter

app = Bottle()


@app.route("/favicon.ico")
def fav():
    abort(404, "not find")


@app.route('/js/<path:path>')
def js(path):
    return static_file(path, root='./js')


@app.route('/')
def index():
    return static_file("index.html", root=".")


@app.route('/:page')
def index_page(page='1'):
    page = int(page)
    return showPage(page)
    # return static_file("reload.html", root="./js")


def showPage(page):
    mongo_con = pymongo.Connection("192.168.1.55", 27017)
    mongo_db = mongo_con.taobao
    itemperpage = 16
    db = Store(SQLiteWriter("taobao.db", frozen=True))
    # items = mongo_db.tabaotry.find().sort([("date", pymongo.DESCENDING), (
    #     "gailv", pymongo.ASCENDING)]).skip((page-1)*itemperpage).limit(itemperpage)
    rs = []
    items = db.find("freetry", "1 order by date desc,gailv  limit %s,%s" %
                    ((page - 1) * itemperpage, itemperpage))
    for item in items:
        item.uuid = 1
        rs.append(dict(item.__dict__))

    return json.dumps(rs)


def taobao(url):
    data = urllib2.urlopen(url).read()
    return data

run(app, host='127.0.0.1', port=7702, server="auto",
    debug=True, reloader=True, quiet=False)
# run(host='localhost', port=7702, debug=True, reloader=True, quiet=False)
