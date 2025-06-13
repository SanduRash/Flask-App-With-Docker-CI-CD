from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        return jsonify({"error": "DATABASE_URL not set"}), 500

    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        now = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"message": f"Database time: {now}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
