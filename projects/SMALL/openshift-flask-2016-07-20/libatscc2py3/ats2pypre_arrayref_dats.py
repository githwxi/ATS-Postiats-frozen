######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-7-21: 12h:55m
##
######

######
#ATSextcode_beg()
######
######
from ats2pypre_basics_cats import *
######
from ats2pypre_bool_cats import *
from ats2pypre_integer_cats import *
######
from ats2pypre_PYlist_cats import *
######
######
#ATSextcode_end()
######

def ats2pypre_arrayref_exists_cloref(arg0, arg1, arg2):
  tmpret0 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_exists_cloref
  tmpret0 = ats2pypre_int_exists_cloref(arg1, arg2)
  return tmpret0


def ats2pypre_arrayref_forall_cloref(arg0, arg1, arg2):
  tmpret1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_forall_cloref
  tmpret1 = ats2pypre_int_forall_cloref(arg1, arg2)
  return tmpret1


def ats2pypre_arrayref_foreach_cloref(arg0, arg1, arg2):
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_foreach_cloref
  ats2pypre_int_foreach_cloref(arg1, arg2)
  return#_void


def ats2pypre_arrszref_make_elt(arg0, arg1):
  tmpret3 = None
  tmp4 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_make_elt
  tmp4 = ats2pypre_arrayref_make_elt(arg0, arg1)
  tmpret3 = ats2pypre_arrszref_make_arrayref(tmp4, arg0)
  return tmpret3


def ats2pypre_arrszref_exists_cloref(arg0, arg1):
  tmpret5 = None
  tmp6 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_exists_cloref
  tmp6 = ats2pypre_arrszref_size(arg0)
  tmpret5 = ats2pypre_int_exists_cloref(tmp6, arg1)
  return tmpret5


def ats2pypre_arrszref_forall_cloref(arg0, arg1):
  tmpret7 = None
  tmp8 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_forall_cloref
  tmp8 = ats2pypre_arrszref_size(arg0)
  tmpret7 = ats2pypre_int_forall_cloref(tmp8, arg1)
  return tmpret7


def ats2pypre_arrszref_foreach_cloref(arg0, arg1):
  tmp10 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_foreach_cloref
  tmp10 = ats2pypre_arrszref_size(arg0)
  ats2pypre_int_foreach_cloref(tmp10, arg1)
  return#_void


def ats2pypre_arrayref_make_elt(arg0, arg1):
  tmpret11 = None
  tmp12 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_make_elt
  tmp12 = PYlist_make_elt(arg0, arg1)
  tmpret11 = tmp12
  return tmpret11


def ats2pypre_arrayref_get_at(arg0, arg1):
  tmpret13 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_get_at
  tmpret13 = PYlist_get_at(arg0, arg1)
  return tmpret13


def ats2pypre_arrayref_set_at(arg0, arg1, arg2):
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrayref_set_at
  PYlist_set_at(arg0, arg1, arg2)
  return#_void


def ats2pypre_arrszref_make_arrayref(arg0, arg1):
  tmpret15 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_make_arrayref
  tmpret15 = arg0
  return tmpret15


def ats2pypre_arrszref_size(arg0):
  tmpret16 = None
  tmp17 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_size
  tmp17 = PYlist_length(arg0)
  tmpret16 = tmp17
  return tmpret16


def ats2pypre_arrszref_get_at(arg0, arg1):
  tmpret18 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_get_at
  tmpret18 = PYlist_get_at(arg0, arg1)
  return tmpret18


def ats2pypre_arrszref_set_at(arg0, arg1, arg2):
  funlab_py = None
  tmplab_py = None
  #__patsflab_arrszref_set_at
  PYlist_set_at(arg0, arg1, arg2)
  return#_void

######
##
## end-of-compilation-unit
##
######
