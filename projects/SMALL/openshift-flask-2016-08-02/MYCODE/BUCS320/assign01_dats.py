######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-12-18: 15h: 5m
##
######

######
#ATSextcode_beg()
######
######
import os
import sys
######
from libatscc2py3_all import *
from libatscc2py3_all_pylibc import *
######
sys.setrecursionlimit(1000000)
######
######
#ATSextcode_end()
######

def assign01_create():
  tmpret0 = None
  tmp1 = None
  tmp2 = None
  tmp3 = None
  tmp4 = None
  tmp6 = None
  tmp7 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab0():
    nonlocal tmpret0, tmp1, tmp2, tmp3, tmp4, tmp6, tmp7
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptrisnull(tmp2)): tmplab_py = 4 ; return#__atstmplab3
    __atstmplab1()
    return
  def __atstmplab1():
    nonlocal tmpret0, tmp1, tmp2, tmp3, tmp4, tmp6, tmp7
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp3 = tmp2[0]
    #ATSINSfreecon(tmp2);
    tmp4 = ats2pypre_fileref_get_file_string(tmp3)
    ats2pypre_fileref_close(tmp3)
    tmpret0 = tmp4
    return
  def __atstmplab2():
    nonlocal tmpret0, tmp1, tmp2, tmp3, tmp4, tmp6, tmp7
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab3()
    return
  def __atstmplab3():
    nonlocal tmpret0, tmp1, tmp2, tmp3, tmp4, tmp6, tmp7
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp7 = ats2pypre_string_append_2("<p>", tmp1)
    tmp6 = ats2pypre_string_append_2(tmp7, "</p>\n")
    tmpret0 = ats2pypre_string_append_2(tmp6, "<p>IOError: [assign01.html] cannot be opened!</p>\n")
    return
  mbranch_1 = { 1: __atstmplab0, 2: __atstmplab1, 3: __atstmplab2, 4: __atstmplab3 }
  #__patsflab_assign01_create
  tmp1 = os.getcwd()
  tmp2 = ats2pypre_fileref_open_opt("app-root/repo/MYDATA/BUCS320/assign01.html", "r")
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret0

######
##
## end-of-compilation-unit
##
######
