# -*- coding: utf-8 -*-
from bottle import static_file, abort, Bottle, run
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


def showPage(page):
    itemperpage = 16
    db = Store(SQLiteWriter("taobao.db", frozen=True))
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
