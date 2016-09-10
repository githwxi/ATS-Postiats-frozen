import os
import sys

from flask import Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

sys.path.append(os.path.join(app.root_path, 'MYCODE'))
sys.path.append(os.path.join(app.root_path, 'libatscc2py3'))

from hello_dats import hello
from hello_dats import hello_name

@app.route('/')
def route_hello(): return hello()

@app.route('/<name>')
def route_hello_name(name): return hello_name(name)

if __name__ == '__main__':
    app.run()
