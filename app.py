# -*- coding: utf-8 -*-
from crypt import methods
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

name_list = []

app = Flask(__name__)

@app.route('/')
def index():
    li_all = len(name_list)
    return render_template("index.html", li = name_list, li_all = li_all)

@app.route('/', methods=['POST'])
def index_post():
    name = request.form['_method']
    if name == 'entry':
        return redirect(url_for('entry_get'))
    elif name == 'exit':
        return redirect(url_for('exit_get'))
    
    return redirect(url_for('index'))

@app.route('/entry/')
def entry_get():
    return render_template('entry.html')

@app.route('/entry/', methods=['POST'])
def entry_post():
    if request.form.get('index'):
        return redirect(url_for('index'))
    name = request.form['name']
    name_list.append(name)
    f = open('log.txt', 'a')
    dt_now = datetime.now()
    data = name + ' , ' + str(dt_now) + ' , ' + 'entry \n'
    f.write(data)
    f.close()
    return redirect(url_for('index'))
    
@app.route('/exit/')
def exit_get():
    return render_template('exit.html', li = name_list)

@app.route('/exit/', methods=['POST'])
def exit_post():
    if request.form.get('index'):
        return redirect(url_for('index'))
    name = request.form['name']
    name_list.remove(name)
    f = open('log.txt', 'a')
    dt_now = datetime.now()
    data = name + ' , ' + str(dt_now) + ' , ' + 'exit \n'
    f.write(data)
    f.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)