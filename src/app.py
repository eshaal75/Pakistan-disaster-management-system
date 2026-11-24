from flask import Flask, render_template, abort
from database import get_connection
from weather import get_weather

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_connection()
    districts = conn.execute("SELECT id, name FROM districts ORDER BY name").fetchall()
    conn.close()
    return render_template("home.html", districts=districts)

@app.route("/weather/<int:district_id>")
def district_weather(district_id):
    conn = get_connection()
    district = conn.execute(
        "SELECT * FROM districts WHERE id = ?", (district_id,)
    ).fetchone()
    conn.close()
    if district is None:
        abort(404)
    data = get_weather(district["latitude"], district["longitude"])
    return render_template("weather.html", district=district, data=data)

if __name__ == "__main__":
    app.run(debug=True)
