"""
Base blueprint for FRONTLINE projects
"""
import os
import shutil
from flask import Blueprint, url_for, g
from tarbell.hooks import register_hook

# rename this in forks
NAME = "FRONTLINE base"

COPY_FILES = ('bower.json', 'config.rb', 'requirements.in', 'requirements.txt')
COPY_DIRS = ('_scss', 'font')

blueprint = Blueprint('base', __name__)
root = os.path.realpath(os.path.dirname(__file__))

@blueprint.record_once
def app_setup(state):
    """
    Add extensions and configuration to site.app
    """
    # use project config
    if 'site' in state.options:
        site = state.options['site']
        #state.app.config.from_object(site.project)

    # assets config


@blueprint.app_template_global('p')
def path_helper(path, **kwargs):
    """
    Helper function for getting preview URLs
    """
    return url_for('preview', path=path, **kwargs)


@register_hook('newproject')
def copy_project_files(site, git):
    """
    Copy useful files into project path
    """
    for filename in COPY_FILES:
        src = os.path.join(root, filename)
        dst = os.path.join(site.path, filename)
        shutil.copy2(src, dst)

    for dirname in COPY_DIRS:
        src = os.path.join(root, dirname)
        dst = os.path.join(site.path, dirname)
        shutil.copytree(src, dst)
