import os
import sys

from flask import Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

# sys.path.append('./MYCODE')
sys.path.append(os.getenv('OPENSHIFT_REPO_DIR', './')+'MYCODE')
sys.path.append(os.getenv('OPENSHIFT_REPO_DIR', './')+'libatscc2py3')
from hello_dats import hello

@app.route('/')
def main0(): return hello()

if __name__ == '__main__':
    app.run()
