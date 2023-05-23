from flask import Blueprint, render_template, redirect, url_for, request, session


bp = Blueprint("home", __name__, url_prefix="/")

@bp.route("/l")
def home():
    return "I am home"

@bp.route("/dashboard")
def index():
   return render_template('dashboard.html', session=session)


@bp.route("/")
def index1():
   return render_template('index.html', session=session)

@bp.route("/contact")
def contact():
   return render_template('contact.html', session=session)

@bp.route("/projects")
def project():
   return render_template('projects.html', session=session)

@bp.route("/resume")
def resume():
   return render_template('resume.html', session=session)

