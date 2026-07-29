from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


# -----------------------------
# Database Connection Function
# -----------------------------
def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():

    connection = get_db_connection()

    expenses = connection.execute(
        """
        SELECT * FROM expenses
        ORDER BY id DESC
        """
    ).fetchall()

    total = connection.execute(
        """
        SELECT SUM(amount) AS total
        FROM expenses
        """
    ).fetchone()

    connection.close()

    total_amount = total["total"]

    if total_amount is None:
        total_amount = 0

    return render_template(
        "index.html",
        expenses=expenses,
        total=total_amount
    )


# -----------------------------
# Add Expense
# -----------------------------
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        title = request.form["title"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"]

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO expenses
            (title, amount, category, date)
            VALUES (?, ?, ?, ?)
            """,
            (title, amount, category, date)
        )

        connection.commit()
        connection.close()

        return redirect("/")

    return render_template("add.html")

# -----------------------------
# Edit Expense
# -----------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    connection = get_db_connection()

    expense = connection.execute(
        """
        SELECT * FROM expenses
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if request.method == "POST":

        title = request.form["title"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"]

        connection.execute(
            """
            UPDATE expenses
            SET title = ?,
                amount = ?,
                category = ?,
                date = ?
            WHERE id = ?
            """,
            (title, amount, category, date, id)
        )

        connection.commit()
        connection.close()

        return redirect("/")

    connection.close()

    return render_template(
        "edit.html",
        expense=expense
    )

# -----------------------------
# Delete Expense
# -----------------------------
@app.route("/delete/<int:id>")
def delete(id):

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")

# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
    