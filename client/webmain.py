# -*- coding: utf-8 -*-
from bottle import static_file, abort, Bottle, run, response
import json
import urllib2
import re
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
        item.uuid = item.itemId
        rs.append(dict(item.__dict__))

    return json.dumps(rs)


@app.route('/taobao/<path:path>')
def taobao(path):
    print path
    # return path
    data = urllib2.urlopen(path).read()
    data = data.decode('GBK')

    # index = data.index('J_AttrList') + 15
    response.set_header("Access-Control-Allow-Origin", "*")
    index = data.index('attributes-list') + 15
    data = data[index:]
    index = data.index('</div>')
    data = data[:index]
    data = re.subn("<.+?>", "\n", data)[0]
    return data

run(app, host='127.0.0.1', port=7702, server="auto",
    debug=True, reloader=True, quiet=False)
