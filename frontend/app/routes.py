from flask import Flask, render_template
import requests

app = Flask(__name__)

BASE_URL = 'http://127.0.0.1:5000/'


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/about')
def about():
    return render_template('about.html')


@app.get('/tasks')
def all_tasks():
    url = "%s/%s" % (BASE_URL, "tasks")
    response = requests.get(url)
    raw_json = response.json()
    tasks = raw_json.get("tasks")
    return render_template('list.html', tasks_list=tasks)
