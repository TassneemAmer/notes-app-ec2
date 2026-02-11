from flask import Flask, request, redirect, render_template_string
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "noteuser",
    "password": "notepass",
    "database": "notesdb"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Notes App</title>
</head>
<body>
    <h2>Write a Note</h2>
    <form method="POST">
        <textarea name="content" rows="4" cols="50" required></textarea><br><br>
        <button type="submit">Save Note</button>
    </form>

    <hr>

    <h2>Saved Notes</h2>
    {% for note in notes %}
    <div>
        <small>{{ note[2] }}</small>
        <p>{{ note[1] }}</p>
        <hr>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == "POST":
        content = request.form["content"]
        cursor.execute(
            "INSERT INTO notes (content) VALUES (%s)",
            (content,)
        )
        conn.commit()
        return redirect("/")

    cursor.execute(
        "SELECT id, content, created_at FROM notes ORDER BY created_at DESC"
    )
    notes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template_string(HTML_TEMPLATE, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
