from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql
from os import path

app = Flask(__name__)
DATABASE = path.dirname(path.dirname(__file__)) + '\date.db'


@app.route('/', methods=['GET', 'POST'])
def index():
    global cur, con
    try:
        con = sql.connect(DATABASE)
        con.row_factory = sql.Row
        cur = con.cursor()
        if request.method in ['POST', 'GET']:
            col_list = ['source_url', 'date_title', 'date_content', 'date_time', 'date_tag']
            source = sqliteEscape(request.form['source'])
            title = sqliteEscape(request.form['title'])
            data = sqliteEscape(request.form['data'])
            time = sqliteEscape(request.form['time'])
            tag = sqliteEscape(request.form['tag'])
            old_list = [source, title, data, time,tag]
            form_list = []
            col_index = []
            for i in old_list:
                if len(i) != 0:
                    ind = old_list.index(i)
                    col_index.append(ind)
                    form_list.append(i)

            sqls = "SELECT * FROM InfoDate ORDER BY date_time DESC"
            if form_list:
                sqls = "SELECT * FROM InfoDate WHERE "
                for i in range(len(form_list)):
                    if i != len(form_list) - 1:
                        sqls += col_list[int(col_index[i])] + " like '%" + form_list[i] + "%' and "
                    else:
                        sqls += col_list[int(col_index[i])] + " like '%" + form_list[i] + "%' ORDER BY date_time DESC"

            cur.execute(sqls)
            con.commit()
            rows = cur.fetchall()
            return render_template('index.html', rows=rows, source=source, title=title, data=data, time=time, tag=tag)
        else:
            return render_template('index.html')
    except Exception as e:
        print(e)
        sqls = "SELECT * FROM InfoDate ORDER BY date_time DESC"
        cur.execute(sqls)
        con.commit()
        rows = cur.fetchall()
        return render_template('index.html', rows=rows)
    finally:
        cur.close()
        con.close()


def sqliteEscape(keyWord):
    try:
        keyWord = keyWord.replace("/", "//")
        keyWord = keyWord.replace("'", "''")
        keyWord = keyWord.replace("[", "/[")
        keyWord = keyWord.replace("]", "/]")
        keyWord = keyWord.replace("%", "/%")
        keyWord = keyWord.replace("&", "/&")
        keyWord = keyWord.replace("_", "/_")
        keyWord = keyWord.replace("(", "/(")
        keyWord = keyWord.replace(")", "/)")
        keyWord = keyWord.replace("<", "/<")
        keyWord = keyWord.replace(">", "/>")
        return keyWord
    except:
        return keyWord


if __name__ == '__main__':
    app.run(debug=True)
