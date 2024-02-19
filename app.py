from flask import Flask, render_template, url_for, request
import json
import os
app = Flask(__name__, static_folder='static')


@app.route('/member')
def main_func():
    with open(os.path.join('templates', 'persons.json'), mode='r', encoding='utf-8') as json_file:
        dict_person = json.load(json_file)
    return render_template('index.html', dict_person=dict_person['person'])


if __name__ == '__main__':
    app.run(port=8080)
