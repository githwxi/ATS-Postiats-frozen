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
from ats2pypre_intrange_dats import *
######
######
#ATSextcode_end()
######

######
#ATSextcode_beg()
######
######
def ats2pypre_matrixref_make_elt(m, n, x0):
  M = []
  i0 = 0
  mn = m * n
  while (i0 < mn): i0 = i0 + 1; M.append(x0)
  return M
######
######
#ATSextcode_end()
######

######
#ATSextcode_beg()
######
######
def ats2pypre_mtrxszref_make_matrixref(M, m, n):
  return { 'matrix' : M, 'nrow' : m, 'ncol' : n }
######
def ats2pypre_mtrxszref_get_nrow(MSZ): return MSZ['nrow']
def ats2pypre_mtrxszref_get_ncol(MSZ): return MSZ['ncol']
######
def ats2pypre_mtrxszref_get_at(MSZ, i, j):
  nrow = MSZ['nrow']
  ncol = MSZ['ncol']
  if (i < 0): raise IndexError('mtrxszref_get_at')
  if (j < 0): raise IndexError('mtrxszref_get_at')
  if (i >= nrow): raise IndexError('mtrxszref_get_at')
  if (j >= ncol): raise IndexError('mtrxszref_get_at')
  return MSZ['matrix'][i*ncol+j]
######
def ats2pypre_mtrxszref_set_at(MSZ, i, j, x0):
  nrow = MSZ['nrow']
  ncol = MSZ['ncol']
  if (i < 0): raise IndexError('mtrxszref_set_at')
  if (j < 0): raise IndexError('mtrxszref_set_at')
  if (i >= nrow): raise IndexError('mtrxszref_set_at')
  if (j >= ncol): raise IndexError('mtrxszref_set_at')
  MSZ['matrix'][i*ncol+j] = x0; return##_void
######
######
#ATSextcode_end()
######

def ats2pypre_matrixref_exists_cloref(arg0, arg1, arg2, arg3):
  tmpret0 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_matrixref_exists_cloref
  tmpret0 = ats2pypre_int2_exists_cloref(arg1, arg2, arg3)
  return tmpret0


def ats2pypre_matrixref_forall_cloref(arg0, arg1, arg2, arg3):
  tmpret1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_matrixref_forall_cloref
  tmpret1 = ats2pypre_int2_forall_cloref(arg1, arg2, arg3)
  return tmpret1


def ats2pypre_matrixref_foreach_cloref(arg0, arg1, arg2, arg3):
  funlab_py = None
  tmplab_py = None
  #__patsflab_matrixref_foreach_cloref
  ats2pypre_int2_foreach_cloref(arg1, arg2, arg3)
  return#_void


def ats2pypre_mtrxszref_make_elt(arg0, arg1, arg2):
  tmpret3 = None
  tmp4 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mtrxszref_make_elt
  tmp4 = ats2pypre_matrixref_make_elt(arg0, arg1, arg2)
  tmpret3 = ats2pypre_mtrxszref_make_matrixref(tmp4, arg0, arg1)
  return tmpret3


def ats2pypre_mtrxszref_exists_cloref(arg0, arg1):
  tmpret5 = None
  tmp6 = None
  tmp7 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mtrxszref_exists_cloref
  tmp6 = ats2pypre_mtrxszref_get_nrow(arg0)
  tmp7 = ats2pypre_mtrxszref_get_ncol(arg0)
  tmpret5 = ats2pypre_int2_exists_cloref(tmp6, tmp7, arg1)
  return tmpret5


def ats2pypre_mtrxszref_forall_cloref(arg0, arg1):
  tmpret8 = None
  tmp9 = None
  tmp10 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mtrxszref_forall_cloref
  tmp9 = ats2pypre_mtrxszref_get_nrow(arg0)
  tmp10 = ats2pypre_mtrxszref_get_ncol(arg0)
  tmpret8 = ats2pypre_int2_forall_cloref(tmp9, tmp10, arg1)
  return tmpret8


def ats2pypre_mtrxszref_foreach_cloref(arg0, arg1):
  tmp12 = None
  tmp13 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mtrxszref_foreach_cloref
  tmp12 = ats2pypre_mtrxszref_get_nrow(arg0)
  tmp13 = ats2pypre_mtrxszref_get_ncol(arg0)
  ats2pypre_int2_foreach_cloref(tmp12, tmp13, arg1)
  return#_void


def ats2pypre_matrixref_get_at(arg0, arg1, arg2, arg3):
  tmpret14 = None
  tmp15 = None
  tmp16 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_matrixref_get_at
  tmp16 = ats2pypre_mul_int1_int1(arg1, arg2)
  tmp15 = ats2pypre_add_int1_int1(tmp16, arg3)
  tmpret14 = PYlist_get_at(arg0, tmp15)
  return tmpret14


def ats2pypre_matrixref_set_at(arg0, arg1, arg2, arg3, arg4):
  tmp18 = None
  tmp19 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_matrixref_set_at
  tmp19 = ats2pypre_mul_int1_int1(arg1, arg2)
  tmp18 = ats2pypre_add_int1_int1(tmp19, arg3)
  PYlist_set_at(arg0, tmp18, arg4)
  return#_void

######
##
## end-of-compilation-unit
##
######
