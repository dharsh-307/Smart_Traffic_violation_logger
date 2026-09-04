from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# --------------------------------------------------
# APP CONFIGURATION
# --------------------------------------------------

app.secret_key = "traffic_logger_secret_key"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(BASE_DIR, "traffic.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --------------------------------------------------
# DATABASE MODEL
# --------------------------------------------------

class Violation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(db.String(20), nullable=False)

    violation_type = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(200), nullable=False)

    date = db.Column(db.Date, nullable=False)

    fine_amount = db.Column(db.Float, nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Unpaid"
    )


# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

def login_required():

    if not session.get("logged_in"):
        return False

    return True


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():

    return render_template("base.html")


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Demo officer credentials

        if username == "admin" and password == "admin123":

            session["logged_in"] = True
            session["username"] = username

            return redirect(url_for("history"))

        else:

            return render_template(
                "login.html",
                error="Invalid username or password"
            )

    return render_template("login.html")


# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# --------------------------------------------------
# ADD VIOLATION
# --------------------------------------------------

@app.route("/add", methods=["GET", "POST"])
def add():

    # Only logged-in officers can add violations

    if not login_required():
        return redirect(url_for("login"))

    if request.method == "POST":

        vehicle_number = request.form["vehicle_number"]

        violation_type = request.form["violation_type"]

        location = request.form["location"]

        date = datetime.strptime(
            request.form["date"],
            "%Y-%m-%d"
        ).date()

        fine_amount = float(
            request.form["fine_amount"]
        )

        violation = Violation(

            vehicle_number=vehicle_number,

            violation_type=violation_type,

            location=location,

            date=date,

            fine_amount=fine_amount,

            status="Unpaid"
        )

        db.session.add(violation)

        db.session.commit()

        return redirect(url_for("add"))

    return render_template("add_violation.html")


# --------------------------------------------------
# VIEW / SEARCH / FILTER HISTORY
# --------------------------------------------------

@app.route("/history")
def history():

    # Only logged-in officers can view history

    if not login_required():
        return redirect(url_for("login"))

    vehicle_number = request.args.get(
        "vehicle_number",
        ""
    )

    date = request.args.get(
        "date",
        ""
    )

    status = request.args.get(
        "status",
        ""
    )

    violation_type = request.args.get(
        "violation_type",
        ""
    )

    # Start query

    query = Violation.query

    # Vehicle number filter

    if vehicle_number:

        query = query.filter(
            Violation.vehicle_number.ilike(
                f"%{vehicle_number}%"
            )
        )

    # Date filter

    if date:

        try:

            selected_date = datetime.strptime(
                date,
                "%Y-%m-%d"
            ).date()

            query = query.filter(
                Violation.date == selected_date
            )

        except ValueError:

            pass

    # Status filter

    if status:

        query = query.filter(
            Violation.status == status
        )

    # Violation type filter

    if violation_type:

        query = query.filter(
            Violation.violation_type == violation_type
        )

    # Get records

    violations = query.order_by(
        Violation.id.desc()
    ).all()

    return render_template(

        "history.html",

        violations=violations,

        vehicle_number=vehicle_number,

        date=date,

        status=status,

        violation_type=violation_type
    )


# --------------------------------------------------
# MARK VIOLATION AS PAID
# --------------------------------------------------

@app.route(
    "/mark_paid/<int:violation_id>",
    methods=["POST"]
)
def mark_paid(violation_id):

    # Only logged-in officers

    if not login_required():
        return redirect(url_for("login"))

    violation = Violation.query.get_or_404(
        violation_id
    )

    violation.status = "Paid"

    db.session.commit()

    return redirect(url_for("history"))


# --------------------------------------------------
# DELETE VIOLATION
# --------------------------------------------------

@app.route(
    "/delete/<int:violation_id>",
    methods=["POST"]
)
def delete_violation(violation_id):

    # Only logged-in officers

    if not login_required():
        return redirect(url_for("login"))

    violation = Violation.query.get_or_404(
        violation_id
    )

    db.session.delete(violation)

    db.session.commit()

    return redirect(url_for("history"))


# --------------------------------------------------
# DIGITAL CHALLAN
# --------------------------------------------------

@app.route("/challan/<int:violation_id>")
def challan(violation_id):

    # Only logged-in officers can view challans
    # from the officer panel

    if not login_required():
        return redirect(url_for("login"))

    violation = Violation.query.get_or_404(
        violation_id
    )

    return render_template(

        "challan.html",

        violation=violation
    )


# --------------------------------------------------
# PUBLIC STATUS PAGE
# --------------------------------------------------

@app.route(
    "/public/status/<int:violation_id>"
)
def public_status(violation_id):

    # IMPORTANT:
    # No login required here.
    # This page is accessed through the QR code.

    violation = Violation.query.get_or_404(
        violation_id
    )

    return render_template(

        "public_status.html",

        violation=violation
    )


# --------------------------------------------------
# CREATE DATABASE
# --------------------------------------------------

with app.app_context():

    db.create_all()


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )