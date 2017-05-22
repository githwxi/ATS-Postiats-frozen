import os
import sys

from flask import Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

sys.path.append(os.path.join(app.root_path, 'MYCODE'))
sys.path.append(os.path.join(app.root_path, 'libatscc2py3'))

from multable_dats import multable_create
from QueenPuzzle_dats import QueenPuzzle_solve

@app.route('/')
def route_root():
  return "<pre><b>Sorry, it is not supported!</b></pre>"

@app.route('/multable')
def route_multable(): return multable_create()
@app.route('/QueenPuzzle')
def route_QueenPuzzle(): return QueenPuzzle_solve()

if __name__ == '__main__':
    app.run()
