from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/progress')
def get_progress():
    with open('static/deck_progress.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/status")
def status_progress_view():
    return render_template("status_progress.html")  # ou global_progress.html si tu réutilises

@app.route('/api/status-progress')
def api_status_progress():
    with open('static/card_status_progress.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)