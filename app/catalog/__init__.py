# app/catalog/__init__.py
import flask

main = flask.Blueprint("main", __name__, template_folder="template")

from app.catalog import routes
