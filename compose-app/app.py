from flask import Flask
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="database",
        database="homelab",
        user="siddig",
        password="labpassword"
)

@app.route("/")

def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    output = "<h1>Siddig Home Lab</h1>"
    output += "<h2>Students from postgreSQL</h2>"

    for row in rows:
        output += f"<p>{row[0]} - {row[1]}</p>"
    return output

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
