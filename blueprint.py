"""
Base blueprint for FRONTLINE projects
"""
from flask import Blueprint, url_for

# rename this in forks
NAME = "FRONTLINE base"

blueprint = Blueprint('base', __name__)


@blueprint.app_template_global('p')
def path_helper(path, **kwargs):
    """
    Helper function for getting preview URLs
    """
    return url_for('preview', path=path, **kwargs)