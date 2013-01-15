import os
import sys
import web

ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.abspath(os.path.join(ROOT, 'templates'))
PUBLIC_DIR = os.path.abspath(os.path.join(ROOT, 'public'))
PROJECT_DIR = os.path.abspath(os.path.join(ROOT, '..'))
PACKAGES_DIR = os.path.abspath(os.path.join(ROOT, '../packages'))
sys.path.extend([PROJECT_DIR, PACKAGES_DIR])

render = web.template.render(TEMPLATES_DIR)