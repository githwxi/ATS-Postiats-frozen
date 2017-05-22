import os
import sys


################################################

from flask import Flask
from flask import request

################################################

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

################################################

sys.path.append(os.path.join(app.root_path, 'MYCODE'))
sys.path.append(os.path.join(app.root_path, 'MYCODE/libatscc2py3'))
sys.path.append(os.path.join(app.root_path, 'MYCODE/ASSIGN/assign0'))
sys.path.append(os.path.join(app.root_path, 'MYCODE/PROJECT/WordCounting/atscc2py3'))

################################################

from assign0_ex3_dats import assign0_ex3_2_test
from assign0_ex3_dats import assign0_ex3_3_test

################################################

from WordCounting_dats import WordCounting_main_url

################################################

@app.route('/')
def route_root():
  return "<pre>For teaching BUCS520, Fall, 2016</pre>"

################################################

@app.route(
'/assign0/ex3_2', methods=['get']
)
def route_assign0_ex3_2():
  arg = request.args.get('arg')
  retval = request.args.get('retval')
  return str(assign0_ex3_2_test(int(arg), int(retval)))

@app.route(
'/assign0/ex3_3', methods=['get']
)
def route_assign0_ex3_3():
  arg = request.args.get('arg')
  retval = request.args.get('retval')
  return str(assign0_ex3_3_test(int(arg), int(retval)))

################################################

@app.route(
'/WordCounting', methods=['get']
)
def route_WordCounting_get_url():
  url = request.args.get('url')
  if (url is None): url = 'http://www.ats-lang.org'
  return WordCounting_main_url(url)

@app.route('/WordCounting/MobyDick')
def route_WordCounting_MobyDick_1_44():
  return WordCounting_main_url('http://pastebin.com/raw/zxcukRJk')

@app.route('/WordCounting/TomSawyer')
def route_WordCounting_TomSawyer_all():
  return WordCounting_main_url('http://pastebin.com/raw/LLVmspdx')

################################################

if __name__ == '__main__':
    app.run()
