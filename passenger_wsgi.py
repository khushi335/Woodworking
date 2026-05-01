import sys
import os

# Add your project directory to the sys.path
project_home = "/home/hightech/project21.quantumcoresoftware.com/wood_work"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtualenv
venv_path = "/home/hightech/virtualenv/project21.quantumcoresoftware.com/wood_work/3.10"
activate_this = os.path.join(venv_path, "bin", "activate_this.py")

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set Django settings module (change if your project name is different)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wood_work.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()