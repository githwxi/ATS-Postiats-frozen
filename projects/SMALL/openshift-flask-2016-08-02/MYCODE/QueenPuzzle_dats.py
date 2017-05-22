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

def __patsfun_5__closurerize():
  def __patsfun_5__cfun(cenv, arg0): return __patsfun_5(arg0)
  return (__patsfun_5__cfun, )

def __patsfun_6__closurerize():
  def __patsfun_6__cfun(cenv, arg0): return __patsfun_6(arg0)
  return (__patsfun_6__cfun, )

def __patsfun_7__closurerize(env0):
  def __patsfun_7__cfun(cenv, arg0, arg1): return __patsfun_7(cenv[1], arg0, arg1)
  return (__patsfun_7__cfun, env0)

def __patsfun_9__9__1__closurerize(env0):
  def __patsfun_9__9__1__cfun(cenv): return __patsfun_9__9__1(cenv[1])
  return (__patsfun_9__9__1__cfun, env0)

def __patsfun_13__13__1__closurerize():
  def __patsfun_13__13__1__cfun(cenv): return __patsfun_13__13__1()
  return (__patsfun_13__13__1__cfun, )

def __patsfun_16__closurerize(env0):
  def __patsfun_16__cfun(cenv, arg0, arg1): return __patsfun_16(cenv[1], arg0, arg1)
  return (__patsfun_16__cfun, env0)

def __patsfun_24__closurerize(env0):
  def __patsfun_24__cfun(cenv, arg0): return __patsfun_24(cenv[1], arg0)
  return (__patsfun_24__cfun, env0)

def __patsfun_25__closurerize(env0, env1):
  def __patsfun_25__cfun(cenv, arg0): return __patsfun_25(cenv[1], cenv[2], arg0)
  return (__patsfun_25__cfun, env0, env1)

def QueenPuzzle_solve():
  tmpret1 = None
  tmp2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_QueenPuzzle_solve
  tmp2 = ats2pypre_PYlist_nil()
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__8(tmp2, "<!DOCTYPE html>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__9(tmp2, "<html>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__10(tmp2, "<head>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__11(tmp2, "<meta charset=\"utf-8\">\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__12(tmp2, "<title>QueenPuzzleSolutions</title>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__13(tmp2, "</head>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__14(tmp2, "<body>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__15(tmp2, "<h1>Queen Puzzle Solutions</h1>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__16(tmp2, "<pre>\n")
  qsolve_3(tmp2, 1000000)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__17(tmp2, "</pre>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__18(tmp2, "</body>\n")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__19(tmp2, "</html>\n")
  tmpret1 = ats2pypre_PYlist_string_join(tmp2)
  return tmpret1


def qsolve_3(env0, arg0):
  tmp5 = None
  tmp6 = None
  tmp7 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_qsolve_3
  tmp7 = __patsfun_4(8)
  tmp6 = ats2pypre_stream_takeLte(tmp7, arg0)
  tmp5 = ats2pypre_stream_vt_iforeach_method(tmp6)
  tmp5[0](tmp5, __patsfun_16__closurerize(env0))
  #ATSINSfreeclo(tmp5);
  return#_void


def __patsfun_4(arg0):
  tmpret8 = None
  tmp9 = None
  tmp10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
  tmp14 = None
  tmp15 = None
  tmp16 = None
  tmp17 = None
  tmp40 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_4
  tmp9 = ats2pypre_gt_int0_int0(arg0, 0)
  if (tmp9):
    tmp15 = ats2pypre_sub_int0_int0(arg0, 1)
    tmp14 = __patsfun_4(tmp15)
    tmp16 = ats2pypre_ML_list0_make_intrange_2(0, 8)
    tmp13 = ats2pypre_cross_stream_list0(tmp14, tmp16)
    tmp17 = 0
    tmp12 = ats2pypre_stream_map_method(tmp13, tmp17)
    tmp11 = tmp12[0](tmp12, __patsfun_5__closurerize())
    tmp10 = ats2pypre_stream_filter_method(tmp11)
    tmpret8 = tmp10[0](tmp10, __patsfun_6__closurerize())
  else:
    tmp40 = None
    tmpret8 = ats2pypre_stream_make_sing__8__1(tmp40)
  #endif
  return tmpret8


def __patsfun_5(arg0):
  tmp18 = None
  tmp19 = None
  tmpret20 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_5
  tmp18 = arg0[0]
  tmp19 = arg0[1]
  tmpret20 = (tmp19, tmp18)
  return tmpret20


def __patsfun_6(arg0):
  tmpret21 = None
  tmp22 = None
  tmp23 = None
  tmp24 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_6
  if(ATSCKptrisnull(arg0)): ATSINScaseof_fail("/home/hwxi/Research/OPENSHIFT/myflask/MYCODE/QueenPuzzle.dats: 990(line=59, offs=157) -- 1007(line=59, offs=174)");
  tmp22 = arg0[0]
  tmp23 = arg0[1]
  tmp24 = ats2pypre_ML_list0_iforall_method(tmp23)
  tmpret21 = tmp24[0](tmp24, __patsfun_7__closurerize(tmp22))
  return tmpret21


def __patsfun_7(env0, arg0, arg1):
  tmpret25 = None
  tmp26 = None
  tmp27 = None
  tmp28 = None
  tmp29 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_7
  tmp26 = ats2pypre_neq_int0_int0(env0, arg1)
  if (tmp26):
    tmp28 = ats2pypre_sub_int0_int0(env0, arg1)
    tmp27 = ats2pypre_abs_int0(tmp28)
    tmp29 = ats2pypre_add_int1_int1(arg0, 1)
    tmpret25 = ats2pypre_neq_int0_int0(tmp27, tmp29)
  else:
    tmpret25 = False
  #endif
  return tmpret25


def ats2pypre_stream_make_sing__8__1(arg0):
  tmpret30__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream_make_sing
  tmpret30__1 = [0, __patsfun_9__9__1__closurerize(arg0)]
  return tmpret30__1


def __patsfun_9__9__1(env0):
  tmpret31__1 = None
  tmp32__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_9
  tmp32__1 = ats2pypre_stream_make_nil__12__1()
  tmpret31__1 = (env0, tmp32__1)
  return tmpret31__1


def ats2pypre_stream_make_nil__12__1():
  tmpret36__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream_make_nil
  tmpret36__1 = [0, __patsfun_13__13__1__closurerize()]
  return tmpret36__1


def __patsfun_13__13__1():
  tmpret37__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_13
  tmpret37__1 = None
  return tmpret37__1


def __patsfun_16(env0, arg0, arg1):
  tmp50 = None
  tmp57 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_16
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__1(env0, "Solution#")
  tmp50 = ats2pypre_add_int1_int1(arg0, 1)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__18__1(env0, tmp50)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__3(env0, ":")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__1(env0)
  tmp57 = ats2pypre_ML_list0_rforeach_method(arg1)
  tmp57[0](tmp57, __patsfun_24__closurerize(env0))
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__3(env0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__1(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__18__1(env0, arg0):
  tmp46__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp46__1 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__2(env0, tmp46__1)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__2(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__3(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__1(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__4(env0, "<br>")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__4(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def __patsfun_24(env0, arg0):
  tmp60 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_24
  tmp60 = ats2pypre_int_foreach_method(8)
  tmp60[0](tmp60, __patsfun_25__closurerize(env0, arg0))
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__2(env0)
  return#_void


def __patsfun_25(env0, env1, arg0):
  tmp63 = None
  tmp64 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab___patsfun_25
  tmp64 = ats2pypre_eq_int0_int0(arg0, env1)
  if (tmp64):
    tmp63 = " Q"
  else:
    tmp63 = " ."
  #endif
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__5(env0, tmp63)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__5(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__2(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__6(env0, "<br>")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__6(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__0__3(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__7(env0, "<br>")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__2__7(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
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

######
##
## end-of-compilation-unit
##
######
