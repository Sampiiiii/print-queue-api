import os
import logging
import sys
from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv
from print_api.config import app_config

from print_api.extensions import (
    db,
    migrate,
    mail,
    bootstrap,
    api
)
# Resources
from print_api.resources import user_views
from print_api.resources.api_routes import auth_routes, maintenance_route, other_routes, print_job_route, printer_route, user_route

load_dotenv("../.env")


def create_app(config_object=app_config[os.getenv('FLASK_ENV')]):
    """
    Create application factory
    :param obj config_object: The configuration object to use.
    :return app: The newly created application
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_errorhandlers(app)
    configure_logger(app)
    return app


def register_extensions(app):
    """
    Register Flask extensions.
    :param app: the flask application
    """
    api.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    return None


def register_blueprints(app):
    """
    Register Flask blueprints.
    :param app: the flask application
    """
    api_prefix = app.config['API_PREFIX']
    app.register_blueprint(
        user_route.user_api,
        url_prefix=f'{api_prefix}/users')
    app.register_blueprint(
        printer_route.printer_api,
        url_prefix=f'{api_prefix}/printers')
    app.register_blueprint(
        maintenance_route.maintenance_api,
        url_prefix=f'{api_prefix}/maintenance')
    app.register_blueprint(
        print_job_route.print_job_api,
        url_prefix=f'{api_prefix}/queue')
    app.register_blueprint(
        other_routes.other_api,
        url_prefix=f'{api_prefix}/misc')
    app.register_blueprint(
        auth_routes.auth_api,
        url_prefix=f'{api_prefix}/auth')
    app.register_blueprint(
        user_views.user_view,
        url_prefix='/')
    return None


def register_errorhandlers(app):
    """
    Register error handlers.
    :param app: the flask application
    """
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"errors/{error_code}.j2"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def configure_logger(app):
    """
    Configure the logger
    """
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
    return None
