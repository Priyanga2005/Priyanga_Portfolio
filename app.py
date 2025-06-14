from flask import Flask, render_template
import json

app = Flask(__name__)

def load_data():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route('/')
def home():
    data = load_data()
    return render_template("index.html", data=data)

@app.route('/projects')
def projects():
    data = load_data()
    return render_template("projects.html", projects=data.get("projects", []))

@app.route('/contact')
def contact():
    data = load_data()
    return render_template("contact.html", contact=data.get("contact", {}), social=data.get("social", {}))

@app.route('/certificates')
def certificates():
    data = load_data()
    return render_template("certificates.html", certificates=data.get("certificates", []))

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)