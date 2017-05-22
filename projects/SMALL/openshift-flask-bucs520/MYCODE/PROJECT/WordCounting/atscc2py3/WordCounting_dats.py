######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-9-11: 20h:50m
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

_WordCounting_statmp22 = None

_WordCounting_statmp23 = None

_WordCounting_statmp24 = None

_WordCounting_statmp25 = None

def _WordCounting_patsfun_15__15__1__closurerize():
  def _WordCounting_patsfun_15__15__1__cfun(cenv, arg0, arg1): return _WordCounting_patsfun_15__15__1(arg0, arg1)
  return (_WordCounting_patsfun_15__15__1__cfun, )

def _WordCounting_patsfun_22__closurerize():
  def _WordCounting_patsfun_22__cfun(cenv, arg0, arg1): return _WordCounting_patsfun_22(arg0, arg1)
  return (_WordCounting_patsfun_22__cfun, )

def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__theWords_get_all():
  tmpret0 = None
  tmp5 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_theWords_get_all
  tmp5 = None
  tmpret0 = _WordCounting_aux_1(tmp5)
  return tmpret0


def _WordCounting_aux_1(arg0):
  apy0 = None
  tmpret1 = None
  tmp2 = None
  tmp3 = None
  tmp4 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab__WordCounting_aux_1
    tmp2 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__word_get()
    tmp3 = ats2pypre_neq_string_string(tmp2, "")
    if (tmp3):
      tmp4 = (tmp2, arg0)
      #ATStailcalseq_beg
      apy0 = tmp4
      arg0 = apy0
      funlab_py = 1 #__patsflab__WordCounting_aux_1
      #ATStailcalseq_end
    else:
      tmpret1 = arg0
    #endif
    if (funlab_py == 0): break
  return tmpret1


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_group(arg0):
  tmpret6 = None
  tmp15 = None
  tmp16 = None
  tmp17 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab4():
    nonlocal arg0
    nonlocal tmpret6, tmp15, tmp16, tmp17
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab7
    __atstmplab5()
    return
  def __atstmplab5():
    nonlocal arg0
    nonlocal tmpret6, tmp15, tmp16, tmp17
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret6 = None
    return
  def __atstmplab6():
    nonlocal arg0
    nonlocal tmpret6, tmp15, tmp16, tmp17
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptrisnull(arg0)): ATSINScaseof_fail("/home/hwxi/Teaching/CS520/cs520-2016-fall/lectures/WordCounting/share/WordCounting_lib.dats: 822(line=59, offs=3) -- 914(line=61, offs=51)");
    __atstmplab7()
    return
  def __atstmplab7():
    nonlocal arg0
    nonlocal tmpret6, tmp15, tmp16, tmp17
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp15 = arg0[0]
    tmp16 = arg0[1]
    tmp17 = None
    tmpret6 = _WordCounting_loop_3(1, tmp15, tmp16, tmp17)
    return
  mbranch_1 = { 1: __atstmplab4, 2: __atstmplab5, 3: __atstmplab6, 4: __atstmplab7 }
  #__patsflab_mylist_group
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret6


def _WordCounting_loop_3(arg0, arg1, arg2, arg3):
  apy0 = None
  apy1 = None
  apy2 = None
  apy3 = None
  tmpret7 = None
  tmp8 = None
  tmp9 = None
  tmp10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
  tmp14 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab0():
    nonlocal arg0, arg1, arg2, arg3
    nonlocal apy0, apy1, apy2, apy3, tmpret7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg2)): tmplab_py = 4 ; return#__atstmplab3
    __atstmplab1()
    return
  def __atstmplab1():
    nonlocal arg0, arg1, arg2, arg3
    nonlocal apy0, apy1, apy2, apy3, tmpret7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp10 = (arg0, arg1)
    tmpret7 = (tmp10, arg3)
    return
  def __atstmplab2():
    nonlocal arg0, arg1, arg2, arg3
    nonlocal apy0, apy1, apy2, apy3, tmpret7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptrisnull(arg2)): ATSINScaseof_fail("/home/hwxi/Teaching/CS520/cs520-2016-fall/lectures/WordCounting/share/WordCounting_lib.dats: 487(line=41, offs=1) -- 791(line=55, offs=4)");
    __atstmplab3()
    return
  def __atstmplab3():
    nonlocal arg0, arg1, arg2, arg3
    nonlocal apy0, apy1, apy2, apy3, tmpret7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp8 = arg2[0]
    tmp9 = arg2[1]
    tmp11 = ats2pypre_eq_string_string(arg1, tmp8)
    if (tmp11):
      tmp12 = ats2pypre_add_int0_int0(arg0, 1)
      #ATStailcalseq_beg
      apy0 = tmp12
      apy1 = arg1
      apy2 = tmp9
      apy3 = arg3
      arg0 = apy0
      arg1 = apy1
      arg2 = apy2
      arg3 = apy3
      funlab_py = 1 #__patsflab__WordCounting_loop_3
      #ATStailcalseq_end
    else:
      tmp14 = (arg0, arg1)
      tmp13 = (tmp14, arg3)
      #ATStailcalseq_beg
      apy0 = 1
      apy1 = tmp8
      apy2 = tmp9
      apy3 = tmp13
      arg0 = apy0
      arg1 = apy1
      arg2 = apy2
      arg3 = apy3
      funlab_py = 1 #__patsflab__WordCounting_loop_3
      #ATStailcalseq_end
    #endif
    return
  mbranch_1 = { 1: __atstmplab0, 2: __atstmplab1, 3: __atstmplab2, 4: __atstmplab3 }
  while(1):
    funlab_py = 0
    #__patsflab__WordCounting_loop_3
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret7


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__WordCounting_main():
  tmpret18 = None
  tmp19 = None
  tmp20 = None
  tmp21 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_WordCounting_main
  tmp19 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__theWords_get_all()
  tmp20 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_sort_string(tmp19)
  tmp21 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_group(tmp20)
  tmpret18 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_sort_intstr(tmp21)
  return tmpret18


def _WordCounting_isalpha_5(arg0):
  tmpret26 = None
  tmp27 = None
  tmp28 = None
  tmp29 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_isalpha_5
  tmp28 = ats2pypre_gte_int0_int0(arg0, _WordCounting_statmp22)
  if (tmp28):
    tmp27 = ats2pypre_lte_int0_int0(arg0, _WordCounting_statmp23)
  else:
    tmp27 = False
  #endif
  if (tmp27):
    tmpret26 = True
  else:
    tmp29 = ats2pypre_gte_int0_int0(arg0, _WordCounting_statmp24)
    if (tmp29):
      tmpret26 = ats2pypre_lte_int0_int0(arg0, _WordCounting_statmp25)
    else:
      tmpret26 = False
    #endif
  #endif
  return tmpret26


def _WordCounting_tolower_6(arg0):
  tmpret30 = None
  tmp31 = None
  tmp32 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_tolower_6
  tmp32 = ats2pypre_gte_int0_int0(arg0, _WordCounting_statmp24)
  if (tmp32):
    tmp31 = ats2pypre_lte_int0_int0(arg0, _WordCounting_statmp25)
  else:
    tmp31 = False
  #endif
  if (tmp31):
    tmpret30 = ats2pypre_add_int0_int0(arg0, 32)
  else:
    tmpret30 = arg0
  #endif
  return tmpret30


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__word_get():
  tmpret33 = None
  tmp43 = None
  tmp44 = None
  tmp45 = None
  tmp46 = None
  tmp47 = None
  tmp48 = None
  tmp49 = None
  tmp50 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_word_get
  tmp43 = _WordCounting_skip_8()
  tmp44 = ats2pypre_gte_int0_int0(tmp43, 0)
  if (tmp44):
    tmp46 = _WordCounting_tolower_6(tmp43)
    tmp47 = None
    tmp45 = (tmp46, tmp47)
    tmp49 = _WordCounting_get2_9(tmp45)
    tmp48 = ats2pypre_PYlist_oflist_rev(tmp49)
    tmp50 = ats2pypre_PYlist_map(tmp48, _WordCounting_patsfun_10)
    tmpret33 = ats2pypre_PYlist_string_join(tmp50)
  else:
    tmpret33 = ""
  #endif
  return tmpret33


def _WordCounting_skip_8():
  tmpret34 = None
  tmp35 = None
  tmp36 = None
  tmp37 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab__WordCounting_skip_8
    tmp35 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__char_get()
    tmp36 = ats2pypre_gte_int0_int0(tmp35, 0)
    if (tmp36):
      tmp37 = _WordCounting_isalpha_5(tmp35)
      if (tmp37):
        tmpret34 = tmp35
      else:
        #ATStailcalseq_beg
        funlab_py = 1 #__patsflab__WordCounting_skip_8
        #ATStailcalseq_end
      #endif
    else:
      tmpret34 = ats2pypre_neg_int0(1)
    #endif
    if (funlab_py == 0): break
  return tmpret34


def _WordCounting_get2_9(arg0):
  apy0 = None
  tmpret38 = None
  tmp39 = None
  tmp40 = None
  tmp41 = None
  tmp42 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab__WordCounting_get2_9
    tmp39 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__char_get()
    tmp40 = _WordCounting_isalpha_5(tmp39)
    if (tmp40):
      tmp42 = _WordCounting_tolower_6(tmp39)
      tmp41 = (tmp42, arg0)
      #ATStailcalseq_beg
      apy0 = tmp41
      arg0 = apy0
      funlab_py = 1 #__patsflab__WordCounting_get2_9
      #ATStailcalseq_end
    else:
      tmpret38 = arg0
    #endif
    if (funlab_py == 0): break
  return tmpret38


def _WordCounting_patsfun_10(arg0):
  tmpret51 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_patsfun_10
  tmpret51 = chr(arg0)
  return tmpret51


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_sort_string(arg0):
  tmpret52 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mylist_sort_string
  tmpret52 = ats2pypre_ML_list0_sort_1__12__1(arg0)
  return tmpret52


def ats2pypre_ML_list0_sort_1__12__1(arg0):
  tmpret53__1 = None
  tmp54__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_sort_1
  tmp54__1 = ats2pypre_list_sort_1__14__1(arg0)
  tmpret53__1 = tmp54__1
  return tmpret53__1


def ats2pypre_list_sort_1__14__1(arg0):
  tmpret57__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_sort_1
  tmpret57__1 = ats2pypre_list_sort_2(arg0, _WordCounting_patsfun_15__15__1__closurerize())
  return tmpret57__1


def _WordCounting_patsfun_15__15__1(arg0, arg1):
  tmpret58__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_patsfun_15
  tmpret58__1 = ATSLIB_056_prelude__gcompare_val_val__18__1(arg0, arg1)
  return tmpret58__1


def ATSLIB_056_prelude__gcompare_val_val__18__1(arg0, arg1):
  tmpret61__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gcompare_val_val
  tmpret61__1 = ats2pypre_compare_string_string(arg0, arg1)
  return tmpret61__1


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__mylist_sort_intstr(arg0):
  tmpret63 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_mylist_sort_intstr
  tmpret63 = ats2pypre_ML_list0_sort_2(arg0, _WordCounting_patsfun_22__closurerize())
  return tmpret63


def _WordCounting_mycmp_21(arg0, arg1):
  tmpret64 = None
  tmp65 = None
  tmp66 = None
  tmp67 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_mycmp_21
  tmp66 = ats2pypre_compare_int0_int0(arg0[0], arg1[0])
  tmp65 = ats2pypre_neg_int0(tmp66)
  tmp67 = ats2pypre_neq_int0_int0(tmp65, 0)
  if (tmp67):
    tmpret64 = tmp65
  else:
    tmpret64 = ats2pypre_compare_string_string(arg0[1], arg1[1])
  #endif
  return tmpret64


def _WordCounting_patsfun_22(arg0, arg1):
  tmpret68 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__WordCounting_patsfun_22
  tmpret68 = _WordCounting_mycmp_21(arg0, arg1)
  return tmpret68


def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__char_get():
  tmpret69 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_char_get
  tmpret69 = char_get()
  return tmpret69


def WordCounting_main_(arg0, arg1):
  tmpret71 = None
  tmp72 = None
  tmp75 = None
  tmp76 = None
  tmp77 = None
  tmp78 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_WordCounting_main_
  tmp72 = ats2pypre_PYlist_nil()
  theSource_initize(arg1)
  tmp75 = _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_sats__WordCounting_main()
  tmp78 = ats2pypre_list_length(tmp75)
  tmp77 = ats2pypre_lte_int1_int1(tmp78, 250)
  if (tmp77):
    tmp76 = tmp75
  else:
    tmp76 = ats2pypre_list_take(tmp75, 250)
  #endif
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__9(tmp72, "<html>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__2(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__11(tmp72, "<head>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__3(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__13(tmp72, "</head>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__4(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__15(tmp72, "<body>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__5(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__17(tmp72, "<h1>WordCounting(result)</h1>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__6(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__19(tmp72, "<pre>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__7(tmp72)
  _WordCounting_loop_27(tmp72, 1, tmp76)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__21(tmp72, "</pre>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__8(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__23(tmp72, "<h1>WordCounting(source)</h1>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__9(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__25(tmp72, "<pre>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__26(tmp72, arg1)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__27(tmp72, "</pre>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__10(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__29(tmp72, "</body>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__11(tmp72)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__31(tmp72, "</html>")
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__12(tmp72)
  tmpret71 = ats2pypre_PYlist_string_join(tmp72)
  return tmpret71


def _WordCounting_loop_27(env0, arg0, arg1):
  apy0 = None
  apy1 = None
  tmp80 = None
  tmp81 = None
  tmp105 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab8():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp80, tmp81, tmp105
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg1)): tmplab_py = 4 ; return#__atstmplab11
    __atstmplab9()
    return
  def __atstmplab9():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp80, tmp81, tmp105
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    None#ATSINSmove_void
    return
  def __atstmplab10():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp80, tmp81, tmp105
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab11()
    return
  def __atstmplab11():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp80, tmp81, tmp105
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp80 = arg1[0]
    tmp81 = arg1[1]
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__28__1(env0, arg0)
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__2(env0, ": ")
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__3(env0, tmp80[1])
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__4(env0, "(")
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__28__2(env0, tmp80[0])
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__6(env0, ")")
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__7(env0, "<br>")
    _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__1(env0)
    tmp105 = ats2pypre_add_int0_int0(arg0, 1)
    #ATStailcalseq_beg
    apy0 = tmp105
    apy1 = tmp81
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__WordCounting_loop_27
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab8, 2: __atstmplab9, 3: __atstmplab10, 4: __atstmplab11 }
  while(1):
    funlab_py = 0
    #__patsflab__WordCounting_loop_27
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__28__1(env0, arg0):
  tmp84__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp84__1 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__1(env0, tmp84__1)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__1(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__2(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__3(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__4(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_int__28__2(env0, arg0):
  tmp84__2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_int
  tmp84__2 = ats2pypre_tostring(arg0)
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__5(env0, tmp84__2)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__5(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__6(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__7(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__1(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__8(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__8(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__9(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__2(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__10(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__10(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__11(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__3(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__12(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__12(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__13(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__4(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__14(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__14(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__15(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__5(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__16(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__16(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__17(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__6(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__18(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__18(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__19(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__7(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__20(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__20(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__21(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__8(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__22(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__22(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__23(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__9(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__24(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__24(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__25(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__26(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__27(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__10(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__28(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__28(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__29(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__11(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__30(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__30(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__31(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_newline__24__12(env0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_newline
  _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__32(env0, "\n")
  return#_void


def _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_055_contrib_057_contrib_057_libatscc_057_libatscc2py3_057_SATS_057_gprint_056_sats__gprint_string__26__32(env0, arg0):
  funlab_py = None
  tmplab_py = None
  #__patsflab_gprint_string
  ats2pypre_PYlist_append(env0, arg0)
  return#_void


_057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynloadflag = 0

def _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynload():
  funlab_py = None
  tmplab_py = None
  #ATSdynload()
  global _WordCounting_statmp22
  global _WordCounting_statmp23
  global _WordCounting_statmp24
  global _WordCounting_statmp25
  #ATSdynloadflag_sta
  global _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynloadflag
  if (ATSCKiseqz(_057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynloadflag)):
    #ATSdynloadset
    _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynloadflag = 1
    _WordCounting_statmp22 = ord("a")
    _WordCounting_statmp23 = ord("z")
    _WordCounting_statmp24 = ord("A")
    _WordCounting_statmp25 = ord("Z")
  #endif
  return#_void


def WordCounting_dynload():
  funlab_py = None
  tmplab_py = None
  _057_home_057_hwxi_057_Teaching_057_CS520_057_cs520_055_2016_055_fall_057_lectures_057_WordCounting_057_atscc2py3_057_WordCounting_056_dats__dynload()
  return#_void


######
#ATSextcode_beg()
######

################################################

import urllib.error
import urllib.request

################################################

def WordCounting_main_url(url):
  data = ""
  status = -1
  try:
    resp = urllib.request.urlopen(url)
    data = resp.read().decode('utf-8')
    status = resp.status
  except ValueError as resp_exn:
    data = str(resp_exn)
  except urllib.error.URLError as resp_exn:
    data = str(resp_exn)
  WordCounting_dynload()
  return WordCounting_main_(status, data)

################################################

theSource = {
  'data': '', 'pos': 0, 'tot': 0
} ##end-of-theSource

def char_get():
  pos = theSource['pos']
  if (pos < theSource['tot']):
    res = theSource['data'][pos]
    theSource['pos'] = pos+1; return ord(res)
  else:
    return -1
  

################################################

def theSource_initize(data):
  theSource['data'] = data; theSource['pos'] = 0; theSource['tot'] = len(data); return

################################################

#
# Moby Dick:
# http:||www.gutenberg.org/files/2701/2701.txt
#

if __name__ == '__main__':
  if len(sys.argv) <= 1:
    data = sys.__stdin__.read(-1);
    WordCounting_dynload()
    print(WordCounting_main_(0, data))
  
  if len(sys.argv) >= 2:
    print(WordCounting_main_url(sys.argv[1]))
  


################################################

######
#ATSextcode_end()
######
######
##
## end-of-compilation-unit
##
######
