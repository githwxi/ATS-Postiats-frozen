######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-12-18: 14h:56m
##
######

######
#ATSextcode_beg()
######
import sys
######
sys.setrecursionlimit(1000000)
######
from libatscc2py3_all import *
from libatscc2py3_all_pylibc import *
######
######
#ATSextcode_end()
######

def multable_create():
  tmpret1 = None
  tmp2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_multable_create
  tmp2 = ats2pypre_PYlist_nil()
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__9(tmp2, "<!DOCTYPE html>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__10(tmp2, "<html>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__11(tmp2, "<head>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__12(tmp2, "<meta charset=\"utf-8\">\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__13(tmp2, "<title>MultiplicationTable</title>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__14(tmp2, "</head>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__15(tmp2, "<body>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__16(tmp2, "<h1>Multiplication Table</h1>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__17(tmp2, "<pre>\n")
  genall_3(tmp2, 9)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__18(tmp2, "</pre>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__19(tmp2, "</body>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__20(tmp2, "</html>\n")
  tmpret1 = ats2pypre_PYlist_string_join(tmp2)
  return tmpret1


def genall_3(env0, arg0):
  tmp5 = None
  tmp7 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_genall_3
  tmp5 = ats2pypre_gt_int0_int0(arg0, 1)
  if (tmp5):
    tmp7 = ats2pypre_sub_int0_int0(arg0, 1)
    genall_3(env0, tmp7)
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__1(env0)
    genone_4(env0, arg0, 1)
  else:
    genone_4(env0, 1, 1)
  #endif
  return#_void


def genone_4(env0, arg0, arg1):
  apy0 = None
  apy1 = None
  tmp12 = None
  tmp14 = None
  tmp31 = None
  tmp32 = None
  tmp38 = None
  tmp39 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab_genone_4
    tmp12 = ats2pypre_gte_int0_int0(arg0, arg1)
    if (tmp12):
      tmp14 = ats2pypre_gt_int0_int0(arg1, 1)
      if (tmp14):
        _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__2(env0, " | ")
      else:
        None#ATSINSmove_void
      #endif
      _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__1(env0, arg1)
      _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__4(env0, " x ")
      _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__2(env0, arg0)
      _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__6(env0, " = ")
      tmp32 = ats2pypre_mul_int0_int0(arg1, arg0)
      tmp31 = ats2pypre_lt_int0_int0(tmp32, 10)
      if (tmp31):
        _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__7(env0, "0")
      else:
        None#ATSINSmove_void
      #endif
      tmp38 = ats2pypre_mul_int0_int0(arg1, arg0)
      _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__3(env0, tmp38)
      tmp39 = ats2pypre_add_int0_int0(arg1, 1)
      #ATStailcalseq_beg
      apy0 = arg0
      apy1 = tmp39
      arg0 = apy0
      arg1 = apy1
      funlab_py = 1 #__patsflab_genone_4
      #ATStailcalseq_end
    else:
      None#ATSINSmove_void
    #endif
    if (funlab_py == 0): break
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__1(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__1(env0, "<br>")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__1(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__2(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__1(env0, arg0):
  tmp18__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp18__1 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__3(env0, tmp18__1)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__3(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__4(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__2(env0, arg0):
  tmp18__2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp18__2 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__5(env0, tmp18__2)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__5(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__6(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__7(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__8__3(env0, arg0):
  tmp18__3 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp18__3 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__8(env0, tmp18__3)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__8(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__9(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__10(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__11(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__12(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__13(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__14(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__15(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__16(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__17(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__18(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__19(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__20(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void

######
##
## end-of-compilation-unit
##
######
