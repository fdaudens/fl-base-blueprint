"""
Base blueprint for FRONTLINE projects
"""
import os
import shutil
from flask import Blueprint, g, url_for
from tarbell.hooks import register_hook

# rename this in forks
NAME = "FRONTLINE base"

COPY_FILES = ('bower.json', 'config.rb', 'requirements.in', 'requirements.txt')
COPY_DIRS = ('_scss', 'font')

blueprint = Blueprint('base', __name__)
root = os.path.realpath(os.path.dirname(__file__))

@blueprint.app_template_global('p')
def path_helper(path, **kwargs):
    """
    Helper function for getting preview URLs
    """
    return url_for('preview', path=path, **kwargs)


@blueprint.app_context_processor
def add_to_context():
    """
    General-purpose context processor for this blueprint
    """
    site = g.current_site
    context = {}

    # no assumptions about project config
    if "production" in getattr(site.project, 'S3_BUCKETS', {}):
        context['BASE_URL'] = "http://{production}".format(**site.project.S3_BUCKETS)
    else:
        # set a safe default
        context['BASE_URL'] = ""

    return context

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

    message = "Copied blueprint assets into project"
    git.add('.')
    git.commit(m=message)
