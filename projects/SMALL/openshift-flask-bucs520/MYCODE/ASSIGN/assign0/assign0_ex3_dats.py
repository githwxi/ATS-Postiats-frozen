######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-12-19:  1h: 6m
##
######

######
#ATSextcode_beg()
######
######
import sys
######
from libatscc2py3_all import *
######
sys.setrecursionlimit(1000000)
######
######
#ATSextcode_end()
######

def _057_home_057_hwxi_057_Research_057_OPENSHIFT_057_bucs520_057_mycode_057_ASSIGN_057_assign0_057_assign0_ex3_056_dats__count1(arg0):
  tmpret0 = None
  tmp1 = None
  tmp2 = None
  tmp3 = None
  tmp4 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_count1
  tmp1 = ats2pypre_gt_int0_int0(arg0, 0)
  if (tmp1):
    tmp3 = ats2pypre_div_int0_int0(arg0, 2)
    tmp2 = _057_home_057_hwxi_057_Research_057_OPENSHIFT_057_bucs520_057_mycode_057_ASSIGN_057_assign0_057_assign0_ex3_056_dats__count1(tmp3)
    tmp4 = ats2pypre_mod_int0_int0(arg0, 2)
    tmpret0 = ats2pypre_add_int0_int0(tmp2, tmp4)
  else:
    tmpret0 = 0
  #endif
  return tmpret0


def binrev(arg0):
  tmpret5 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_binrev
  tmpret5 = aux_2(arg0, 0)
  return tmpret5


def aux_2(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret6 = None
  tmp7 = None
  tmp8 = None
  tmp9 = None
  tmp10 = None
  tmp11 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab_aux_2
    tmp7 = ats2pypre_gt_int1_int1(arg0, 0)
    if (tmp7):
      tmp8 = ats2pypre_div_int1_int1(arg0, 2)
      tmp10 = ats2pypre_mul_int0_int0(2, arg1)
      tmp11 = ats2pypre_mod_int0_int0(arg0, 2)
      tmp9 = ats2pypre_add_int0_int0(tmp10, tmp11)
      #ATStailcalseq_beg
      apy0 = tmp8
      apy1 = tmp9
      arg0 = apy0
      arg1 = apy1
      funlab_py = 1 #__patsflab_aux_2
      #ATStailcalseq_end
    else:
      tmpret6 = arg1
    #endif
    if (funlab_py == 0): break
  return tmpret6


def assign0_ex3_2_test(arg0, arg1):
  tmpret12 = None
  tmp13 = None
  tmp14 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_assign0_ex3_2_test
  tmp13 = ats2pypre_gte_int1_int1(arg0, 0)
  if (tmp13):
    tmp14 = _057_home_057_hwxi_057_Research_057_OPENSHIFT_057_bucs520_057_mycode_057_ASSIGN_057_assign0_057_assign0_ex3_056_dats__count1(arg0)
    tmpret12 = ats2pypre_eq_int0_int0(tmp14, arg1)
  else:
    tmpret12 = False
  #endif
  return tmpret12


def assign0_ex3_3_test(arg0, arg1):
  tmpret15 = None
  tmp16 = None
  tmp17 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_assign0_ex3_3_test
  tmp16 = ats2pypre_gte_int1_int1(arg0, 0)
  if (tmp16):
    tmp17 = binrev(arg0)
    tmpret15 = ats2pypre_eq_int0_int0(tmp17, arg1)
  else:
    tmpret15 = False
  #endif
  return tmpret15

######
##
## end-of-compilation-unit
##
######
