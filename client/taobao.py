# -*- coding: utf-8 -*-
from bottle import static_file, Bottle, run
#import json
import urllib2
import re

app = Bottle()


@app.route('/')
def index():
    return taobao("http://detail.tmall.com/item.htm?spm=a1z0i.1000972.0.81.xHzDBC&id=23707432609&source=superboss&appId=19&viewfrom=try#J_TabBar")


def taobao(url):
    data = urllib2.urlopen(url).read()
    data = data.decode('GBK')
    index = data.index('J_AttrList') + 15
    data = data[index:]
    index = data.index('</div>')
    data = data[:index]
    data = re.subn("<.+?>", "", data)[0]
    return data

run(app, host='127.0.0.1', port=7702, server="auto",
    debug=True, reloader=True, quiet=False)
# run(host='localhost', port=7702, debug=True, reloader=True, quiet=False)
