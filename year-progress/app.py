"""
Year Progress — Flask Backend
==============================

Folder structure:
    your-folder/
    ├── app.py
    ├── requirements.txt
    └── templates/
        └── index.html

Run locally:
    pip install -r requirements.txt
    python app.py
    → open http://localhost:5000

Deploy (production with Gunicorn):
    gunicorn -w 2 -b 0.0.0.0:8000 app:app
    → then point Nginx/Apache to port 8000
"""

from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/year-progress")
def year_progress():
    now   = datetime.now()
    year  = now.year
    start = datetime(year, 1, 1)
    end   = datetime(year + 1, 1, 1)

    total_seconds   = (end - start).total_seconds()
    elapsed_seconds = (now - start).total_seconds()
    percent         = (elapsed_seconds / total_seconds) * 100

    return jsonify({
        "year":        year,
        "percent":     round(percent, 6),  # precise float → used for bar width
        "percent_int": int(percent),       # integer       → used for display
    })


if __name__ == "__main__":
    # debug=False in production; keep True only for local development
    app.run(debug=True, host="0.0.0.0", port=5000)
