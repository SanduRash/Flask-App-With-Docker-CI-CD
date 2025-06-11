from flask import Flask, render_template, jsonify

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api(){}:
    return jsonify({"message": "Hey there python"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)