
from flask import Flask, render_template, request, redirect, url_for, flash

from database import connect_db
from student import (
    get_students,
    add_student,
    update_student,
    delete_student
)
from company import get_companies, add_company
from placement import get_placements, add_placement
from analysis import get_placement_analysis


app = Flask(__name__)
app.secret_key = "student-placement-development-key"


# HOME PAGE
@app.route("/")
def home():

    conn = connect_db()

    if conn is None:
        return "MySQL Connection Failed! Please check database settings.", 500

    conn.close()

    keyword = request.args.get("search", "").strip()

    students = get_students(keyword)
    companies = get_companies()
    placements = get_placements()
    analysis = get_placement_analysis()

    return render_template(
        "index.html",
        students=students,
        companies=companies,
        placements=placements,
        analysis=analysis,
        keyword=keyword
    )


# ADD STUDENT
@app.route("/add_student", methods=["POST"])
def student_add():

    try:
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        course = request.form["course"].strip()
        percentage = float(request.form["percentage"])

        if not name or not email or not course:
            flash("All student fields are required!")
            return redirect(url_for("home"))

        if not 0 <= percentage <= 100:
            flash("Percentage must be between 0 and 100!")
            return redirect(url_for("home"))

        success = add_student(
            name,
            email,
            course,
            percentage
        )

        if success:
            flash("Student Added Successfully!")
        else:
            flash("Unable to add student. Check email or database.")

    except (ValueError, KeyError):
        flash("Please enter valid student details!")

    return redirect(url_for("home"))


# UPDATE STUDENT
@app.route("/update_student/<int:id>", methods=["POST"])
def student_update(id):

    try:
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        course = request.form["course"].strip()
        percentage = float(request.form["percentage"])

        if not name or not email or not course:
            flash("All fields are required!")
            return redirect(url_for("home"))

        if not 0 <= percentage <= 100:
            flash("Percentage must be between 0 and 100!")
            return redirect(url_for("home"))

        success = update_student(
            id,
            name,
            email,
            course,
            percentage
        )

        if success:
            flash("Student Updated Successfully!")
        else:
            flash("Student not found or no changes made.")

    except (ValueError, KeyError):
        flash("Invalid student details!")

    return redirect(url_for("home"))


# DELETE STUDENT
@app.route("/delete_student/<int:id>", methods=["POST"])
def student_delete(id):

    success = delete_student(id)

    if success:
        flash("Student Deleted Successfully!")
    else:
        flash("Unable to delete student.")

    return redirect(url_for("home"))


# ADD COMPANY
@app.route("/add_company", methods=["POST"])
def company_add():

    try:
        company_name = request.form["company_name"].strip()
        job_role = request.form["job_role"].strip()
        package = float(request.form["package"])

        if not company_name or not job_role or package < 0:
            flash("Please enter valid company details!")
            return redirect(url_for("home"))

        success = add_company(
            company_name,
            job_role,
            package
        )

        if success:
            flash("Company Added Successfully!")
        else:
            flash("Unable to add company.")

    except (ValueError, KeyError):
        flash("Invalid company details!")

    return redirect(url_for("home"))


# ADD PLACEMENT
@app.route("/add_placement", methods=["POST"])
def placement_add():

    try:
        student_id = int(request.form["student_id"])
        company_id = int(request.form["company_id"])
        status = request.form["status"]

        if student_id <= 0 or company_id <= 0:
            flash("Enter valid Student ID and Company ID!")
            return redirect(url_for("home"))

        if status not in ["Selected", "Rejected", "Pending"]:
            flash("Invalid placement status!")
            return redirect(url_for("home"))

        success = add_placement(
            student_id,
            company_id,
            status
        )

        if success:
            flash("Placement Added Successfully!")
        else:
            flash("Unable to add placement. Check IDs.")

    except (ValueError, KeyError):
        flash("Invalid placement details!")

    return redirect(url_for("home"))


# HEALTH CHECK
@app.route("/health")
def health():

    conn = connect_db()

    if conn is None:
        return {"status": "error", "database": "disconnected"}, 500

    conn.close()

    return {
        "status": "success",
        "database": "connected"
    }


# RUN APPLICATION
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
