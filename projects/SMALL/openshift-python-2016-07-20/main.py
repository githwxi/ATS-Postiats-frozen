import os
import sys

from flask import Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

sys.path.append(os.path.join(app.root_path, 'MYCODE'))
sys.path.append(os.path.join(app.root_path, 'libatscc2py3'))

from hello_dats import hello

@app.route('/')
def main0(): return hello()

if __name__ == '__main__':
    app.run()
