######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-7-21:  3h:16m
##
######

######
#ATSextcode_beg()
######
######
from ats2pypre_basics_cats import *
######
from ats2pypre_integer_cats import *
from ats2pypre_bool_cats import *
######
######
#ATSextcode_end()
######

def ats2pypre_list_make_intrange_2(arg0, arg1):
  tmpret2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_make_intrange_2
  tmpret2 = ats2pypre_list_make_intrange_3(arg0, arg1, 1)
  return tmpret2


def ats2pypre_list_make_intrange_3(arg0, arg1, arg2):
  tmpret3 = None
  tmp14 = None
  tmp15 = None
  tmp16 = None
  tmp17 = None
  tmp18 = None
  tmp19 = None
  tmp20 = None
  tmp21 = None
  tmp22 = None
  tmp23 = None
  tmp24 = None
  tmp25 = None
  tmp26 = None
  tmp27 = None
  tmp28 = None
  tmp29 = None
  tmp30 = None
  tmp31 = None
  tmp32 = None
  tmp33 = None
  tmp34 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab6():
    nonlocal arg0, arg1, arg2
    nonlocal tmpret3, tmp14, tmp15, tmp16, tmp17, tmp18, tmp19, tmp20, tmp21, tmp22, tmp23, tmp24, tmp25, tmp26, tmp27, tmp28, tmp29, tmp30, tmp31, tmp32, tmp33, tmp34
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp14 = ats2pypre_gt_int0_int0(arg2, 0)
    if not(ATSCKpat_bool(tmp14, True)): tmplab_py = 2 ; return#__atstmplab7
    tmp15 = ats2pypre_lt_int0_int0(arg0, arg1)
    if (tmp15):
      tmp19 = ats2pypre_sub_int0_int0(arg1, arg0)
      tmp18 = ats2pypre_add_int0_int0(tmp19, arg2)
      tmp17 = ats2pypre_sub_int0_int0(tmp18, 1)
      tmp16 = ats2pypre_div_int0_int0(tmp17, arg2)
      tmp22 = ats2pypre_sub_int0_int0(tmp16, 1)
      tmp21 = ats2pypre_mul_int0_int0(tmp22, arg2)
      tmp20 = ats2pypre_add_int0_int0(arg0, tmp21)
      tmp23 = None
      tmpret3 = _ats2pypre_list_loop1_4(tmp16, tmp20, arg2, tmp23)
    else:
      tmpret3 = None
    #endif
    return
  def __atstmplab7():
    nonlocal arg0, arg1, arg2
    nonlocal tmpret3, tmp14, tmp15, tmp16, tmp17, tmp18, tmp19, tmp20, tmp21, tmp22, tmp23, tmp24, tmp25, tmp26, tmp27, tmp28, tmp29, tmp30, tmp31, tmp32, tmp33, tmp34
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp24 = ats2pypre_lt_int0_int0(arg2, 0)
    if not(ATSCKpat_bool(tmp24, True)): tmplab_py = 3 ; return#__atstmplab8
    tmp25 = ats2pypre_gt_int0_int0(arg0, arg1)
    if (tmp25):
      tmp26 = ats2pypre_neg_int0(arg2)
      tmp30 = ats2pypre_sub_int0_int0(arg0, arg1)
      tmp29 = ats2pypre_add_int0_int0(tmp30, tmp26)
      tmp28 = ats2pypre_sub_int0_int0(tmp29, 1)
      tmp27 = ats2pypre_div_int0_int0(tmp28, tmp26)
      tmp33 = ats2pypre_sub_int0_int0(tmp27, 1)
      tmp32 = ats2pypre_mul_int0_int0(tmp33, tmp26)
      tmp31 = ats2pypre_sub_int0_int0(arg0, tmp32)
      tmp34 = None
      tmpret3 = _ats2pypre_list_loop2_5(tmp27, tmp31, tmp26, tmp34)
    else:
      tmpret3 = None
    #endif
    return
  def __atstmplab8():
    nonlocal arg0, arg1, arg2
    nonlocal tmpret3, tmp14, tmp15, tmp16, tmp17, tmp18, tmp19, tmp20, tmp21, tmp22, tmp23, tmp24, tmp25, tmp26, tmp27, tmp28, tmp29, tmp30, tmp31, tmp32, tmp33, tmp34
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret3 = None
    return
  mbranch_1 = { 1: __atstmplab6, 2: __atstmplab7, 3: __atstmplab8 }
  #__patsflab_list_make_intrange_3
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret3


def _ats2pypre_list_loop1_4(arg0, arg1, arg2, arg3):
  apy0 = None
  apy1 = None
  apy2 = None
  apy3 = None
  tmpret4 = None
  tmp5 = None
  tmp6 = None
  tmp7 = None
  tmp8 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_loop1_4
    tmp5 = ats2pypre_gt_int0_int0(arg0, 0)
    if (tmp5):
      tmp6 = ats2pypre_sub_int0_int0(arg0, 1)
      tmp7 = ats2pypre_sub_int0_int0(arg1, arg2)
      tmp8 = (arg1, arg3)
      #ATStailcalseq_beg
      apy0 = tmp6
      apy1 = tmp7
      apy2 = arg2
      apy3 = tmp8
      arg0 = apy0
      arg1 = apy1
      arg2 = apy2
      arg3 = apy3
      funlab_py = 1 #__patsflab__ats2pypre_list_loop1_4
      #ATStailcalseq_end
    else:
      tmpret4 = arg3
    #endif
    if (funlab_py == 0): break
  return tmpret4


def _ats2pypre_list_loop2_5(arg0, arg1, arg2, arg3):
  apy0 = None
  apy1 = None
  apy2 = None
  apy3 = None
  tmpret9 = None
  tmp10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_loop2_5
    tmp10 = ats2pypre_gt_int0_int0(arg0, 0)
    if (tmp10):
      tmp11 = ats2pypre_sub_int0_int0(arg0, 1)
      tmp12 = ats2pypre_add_int0_int0(arg1, arg2)
      tmp13 = (arg1, arg3)
      #ATStailcalseq_beg
      apy0 = tmp11
      apy1 = tmp12
      apy2 = arg2
      apy3 = tmp13
      arg0 = apy0
      arg1 = apy1
      arg2 = apy2
      arg3 = apy3
      funlab_py = 1 #__patsflab__ats2pypre_list_loop2_5
      #ATStailcalseq_end
    else:
      tmpret9 = arg3
    #endif
    if (funlab_py == 0): break
  return tmpret9


def ats2pypre_list_length(arg0):
  tmpret46 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_length
  tmpret46 = _ats2pypre_list_loop_12(arg0, 0)
  return tmpret46


def _ats2pypre_list_loop_12(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret47 = None
  tmp49 = None
  tmp50 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab13():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab16
    __atstmplab14()
    return
  def __atstmplab14():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret47 = arg1
    return
  def __atstmplab15():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab16()
    return
  def __atstmplab16():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp49 = arg0[1]
    tmp50 = ats2pypre_add_int1_int1(arg1, 1)
    #ATStailcalseq_beg
    apy0 = tmp49
    apy1 = tmp50
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_list_loop_12
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab13, 2: __atstmplab14, 3: __atstmplab15, 4: __atstmplab16 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_loop_12
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret47


def ats2pypre_list_last(arg0):
  apy0 = None
  tmpret51 = None
  tmp52 = None
  tmp53 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab17():
    nonlocal arg0
    nonlocal apy0, tmpret51, tmp52, tmp53
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(tmp53)): tmplab_py = 4 ; return#__atstmplab20
    __atstmplab18()
    return
  def __atstmplab18():
    nonlocal arg0
    nonlocal apy0, tmpret51, tmp52, tmp53
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret51 = tmp52
    return
  def __atstmplab19():
    nonlocal arg0
    nonlocal apy0, tmpret51, tmp52, tmp53
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab20()
    return
  def __atstmplab20():
    nonlocal arg0
    nonlocal apy0, tmpret51, tmp52, tmp53
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    #ATStailcalseq_beg
    apy0 = tmp53
    arg0 = apy0
    funlab_py = 1 #__patsflab_list_last
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab17, 2: __atstmplab18, 3: __atstmplab19, 4: __atstmplab20 }
  while(1):
    funlab_py = 0
    #__patsflab_list_last
    tmp52 = arg0[0]
    tmp53 = arg0[1]
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret51


def ats2pypre_list_get_at(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret54 = None
  tmp55 = None
  tmp56 = None
  tmp57 = None
  tmp58 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab_list_get_at
    tmp55 = ats2pypre_eq_int1_int1(arg1, 0)
    if (tmp55):
      tmp56 = arg0[0]
      tmpret54 = tmp56
    else:
      tmp57 = arg0[1]
      tmp58 = ats2pypre_sub_int1_int1(arg1, 1)
      #ATStailcalseq_beg
      apy0 = tmp57
      apy1 = tmp58
      arg0 = apy0
      arg1 = apy1
      funlab_py = 1 #__patsflab_list_get_at
      #ATStailcalseq_end
    #endif
    if (funlab_py == 0): break
  return tmpret54


def ats2pypre_list_snoc(arg0, arg1):
  tmpret59 = None
  tmp60 = None
  tmp61 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_snoc
  tmp61 = None
  tmp60 = (arg1, tmp61)
  tmpret59 = ats2pypre_list_append(arg0, tmp60)
  return tmpret59


def ats2pypre_list_extend(arg0, arg1):
  tmpret62 = None
  tmp63 = None
  tmp64 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_extend
  tmp64 = None
  tmp63 = (arg1, tmp64)
  tmpret62 = ats2pypre_list_append(arg0, tmp63)
  return tmpret62


def ats2pypre_list_append(arg0, arg1):
  tmpret65 = None
  tmp66 = None
  tmp67 = None
  tmp68 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab21():
    nonlocal arg0, arg1
    nonlocal tmpret65, tmp66, tmp67, tmp68
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab24
    __atstmplab22()
    return
  def __atstmplab22():
    nonlocal arg0, arg1
    nonlocal tmpret65, tmp66, tmp67, tmp68
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret65 = arg1
    return
  def __atstmplab23():
    nonlocal arg0, arg1
    nonlocal tmpret65, tmp66, tmp67, tmp68
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab24()
    return
  def __atstmplab24():
    nonlocal arg0, arg1
    nonlocal tmpret65, tmp66, tmp67, tmp68
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp66 = arg0[0]
    tmp67 = arg0[1]
    tmp68 = ats2pypre_list_append(tmp67, arg1)
    tmpret65 = (tmp66, tmp68)
    return
  mbranch_1 = { 1: __atstmplab21, 2: __atstmplab22, 3: __atstmplab23, 4: __atstmplab24 }
  #__patsflab_list_append
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret65


def ats2pypre_list_reverse(arg0):
  tmpret69 = None
  tmp70 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_reverse
  tmp70 = None
  tmpret69 = ats2pypre_list_reverse_append(arg0, tmp70)
  return tmpret69


def ats2pypre_list_reverse_append(arg0, arg1):
  tmpret71 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_reverse_append
  tmpret71 = _ats2pypre_list_loop_20(arg0, arg1)
  return tmpret71


def _ats2pypre_list_loop_20(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret72 = None
  tmp73 = None
  tmp74 = None
  tmp75 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab25():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret72, tmp73, tmp74, tmp75
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab28
    __atstmplab26()
    return
  def __atstmplab26():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret72, tmp73, tmp74, tmp75
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret72 = arg1
    return
  def __atstmplab27():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret72, tmp73, tmp74, tmp75
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab28()
    return
  def __atstmplab28():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret72, tmp73, tmp74, tmp75
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp73 = arg0[0]
    tmp74 = arg0[1]
    tmp75 = (tmp73, arg1)
    #ATStailcalseq_beg
    apy0 = tmp74
    apy1 = tmp75
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_list_loop_20
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab25, 2: __atstmplab26, 3: __atstmplab27, 4: __atstmplab28 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_loop_20
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret72


def ats2pypre_list_take(arg0, arg1):
  tmpret76 = None
  tmp77 = None
  tmp78 = None
  tmp79 = None
  tmp80 = None
  tmp81 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_take
  tmp77 = ats2pypre_gt_int1_int1(arg1, 0)
  if (tmp77):
    tmp78 = arg0[0]
    tmp79 = arg0[1]
    tmp81 = ats2pypre_sub_int1_int1(arg1, 1)
    tmp80 = ats2pypre_list_take(tmp79, tmp81)
    tmpret76 = (tmp78, tmp80)
  else:
    tmpret76 = None
  #endif
  return tmpret76


def ats2pypre_list_drop(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret82 = None
  tmp83 = None
  tmp84 = None
  tmp85 = None
  funlab_py = None
  tmplab_py = None
  while(1):
    funlab_py = 0
    #__patsflab_list_drop
    tmp83 = ats2pypre_gt_int1_int1(arg1, 0)
    if (tmp83):
      tmp84 = arg0[1]
      tmp85 = ats2pypre_sub_int1_int1(arg1, 1)
      #ATStailcalseq_beg
      apy0 = tmp84
      apy1 = tmp85
      arg0 = apy0
      arg1 = apy1
      funlab_py = 1 #__patsflab_list_drop
      #ATStailcalseq_end
    else:
      tmpret82 = arg0
    #endif
    if (funlab_py == 0): break
  return tmpret82


def ats2pypre_list_split_at(arg0, arg1):
  tmpret86 = None
  tmp87 = None
  tmp88 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_split_at
  tmp87 = ats2pypre_list_take(arg0, arg1)
  tmp88 = ats2pypre_list_drop(arg0, arg1)
  tmpret86 = (tmp87, tmp88)
  return tmpret86


def ats2pypre_list_insert_at(arg0, arg1, arg2):
  tmpret89 = None
  tmp90 = None
  tmp91 = None
  tmp92 = None
  tmp93 = None
  tmp94 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_insert_at
  tmp90 = ats2pypre_gt_int1_int1(arg1, 0)
  if (tmp90):
    tmp91 = arg0[0]
    tmp92 = arg0[1]
    tmp94 = ats2pypre_sub_int1_int1(arg1, 1)
    tmp93 = ats2pypre_list_insert_at(tmp92, tmp94, arg2)
    tmpret89 = (tmp91, tmp93)
  else:
    tmpret89 = (arg2, arg0)
  #endif
  return tmpret89


def ats2pypre_list_remove_at(arg0, arg1):
  tmpret95 = None
  tmp96 = None
  tmp97 = None
  tmp98 = None
  tmp99 = None
  tmp100 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_remove_at
  tmp96 = arg0[0]
  tmp97 = arg0[1]
  tmp98 = ats2pypre_gt_int1_int1(arg1, 0)
  if (tmp98):
    tmp100 = ats2pypre_sub_int1_int1(arg1, 1)
    tmp99 = ats2pypre_list_remove_at(tmp97, tmp100)
    tmpret95 = (tmp96, tmp99)
  else:
    tmpret95 = tmp97
  #endif
  return tmpret95


def ats2pypre_list_takeout_at(arg0, arg1):
  tmpret101 = None
  tmp102 = None
  tmp103 = None
  tmp104 = None
  tmp105 = None
  tmp106 = None
  tmp107 = None
  tmp108 = None
  tmp109 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_takeout_at
  tmp102 = arg0[0]
  tmp103 = arg0[1]
  tmp104 = ats2pypre_gt_int1_int1(arg1, 0)
  if (tmp104):
    tmp106 = ats2pypre_sub_int1_int1(arg1, 1)
    tmp105 = ats2pypre_list_takeout_at(tmp103, tmp106)
    tmp107 = tmp105[0]
    tmp108 = tmp105[1]
    tmp109 = (tmp102, tmp108)
    tmpret101 = (tmp107, tmp109)
  else:
    tmpret101 = (tmp102, tmp103)
  #endif
  return tmpret101


def ats2pypre_list_app(arg0, arg1):
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_app
  ats2pypre_list_foreach(arg0, arg1)
  return#_void


def ats2pypre_list_foreach(arg0, arg1):
  apy0 = None
  apy1 = None
  tmp112 = None
  tmp113 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab29():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmp112, tmp113
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab32
    __atstmplab30()
    return
  def __atstmplab30():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmp112, tmp113
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    None#ATSINSmove_void
    return
  def __atstmplab31():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmp112, tmp113
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab32()
    return
  def __atstmplab32():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmp112, tmp113
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp112 = arg0[0]
    tmp113 = arg0[1]
    arg1[0](arg1, tmp112)
    #ATStailcalseq_beg
    apy0 = tmp113
    apy1 = arg1
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab_list_foreach
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab29, 2: __atstmplab30, 3: __atstmplab31, 4: __atstmplab32 }
  while(1):
    funlab_py = 0
    #__patsflab_list_foreach
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return#_void


def ats2pypre_list_iforeach(arg0, arg1):
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_iforeach
  _ats2pypre_list_aux_30(arg1, 0, arg0)
  return#_void


def _ats2pypre_list_aux_30(env0, arg0, arg1):
  apy0 = None
  apy1 = None
  tmp117 = None
  tmp118 = None
  tmp120 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab33():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp117, tmp118, tmp120
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg1)): tmplab_py = 4 ; return#__atstmplab36
    __atstmplab34()
    return
  def __atstmplab34():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp117, tmp118, tmp120
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    None#ATSINSmove_void
    return
  def __atstmplab35():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp117, tmp118, tmp120
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab36()
    return
  def __atstmplab36():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmp117, tmp118, tmp120
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp117 = arg1[0]
    tmp118 = arg1[1]
    env0[0](env0, arg0, tmp117)
    tmp120 = ats2pypre_add_int0_int0(arg0, 1)
    #ATStailcalseq_beg
    apy0 = tmp120
    apy1 = tmp118
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_list_aux_30
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab33, 2: __atstmplab34, 3: __atstmplab35, 4: __atstmplab36 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_aux_30
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return#_void


def ats2pypre_list_rforeach(arg0, arg1):
  tmp122 = None
  tmp123 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab37():
    nonlocal arg0, arg1
    nonlocal tmp122, tmp123
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab40
    __atstmplab38()
    return
  def __atstmplab38():
    nonlocal arg0, arg1
    nonlocal tmp122, tmp123
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    None#ATSINSmove_void
    return
  def __atstmplab39():
    nonlocal arg0, arg1
    nonlocal tmp122, tmp123
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab40()
    return
  def __atstmplab40():
    nonlocal arg0, arg1
    nonlocal tmp122, tmp123
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp122 = arg0[0]
    tmp123 = arg0[1]
    ats2pypre_list_rforeach(tmp123, arg1)
    arg1[0](arg1, tmp122)
    return
  mbranch_1 = { 1: __atstmplab37, 2: __atstmplab38, 3: __atstmplab39, 4: __atstmplab40 }
  #__patsflab_list_rforeach
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return#_void


def ats2pypre_list_filter(arg0, arg1):
  tmpret125 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_filter
  tmpret125 = _ats2pypre_list_aux_33(arg1, arg0)
  return tmpret125


def _ats2pypre_list_aux_33(env0, arg0):
  apy0 = None
  tmpret126 = None
  tmp127 = None
  tmp128 = None
  tmp129 = None
  tmp130 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab41():
    nonlocal env0, arg0
    nonlocal apy0, tmpret126, tmp127, tmp128, tmp129, tmp130
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab44
    __atstmplab42()
    return
  def __atstmplab42():
    nonlocal env0, arg0
    nonlocal apy0, tmpret126, tmp127, tmp128, tmp129, tmp130
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret126 = None
    return
  def __atstmplab43():
    nonlocal env0, arg0
    nonlocal apy0, tmpret126, tmp127, tmp128, tmp129, tmp130
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab44()
    return
  def __atstmplab44():
    nonlocal env0, arg0
    nonlocal apy0, tmpret126, tmp127, tmp128, tmp129, tmp130
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp127 = arg0[0]
    tmp128 = arg0[1]
    tmp129 = env0[0](env0, tmp127)
    if (tmp129):
      tmp130 = _ats2pypre_list_aux_33(env0, tmp128)
      tmpret126 = (tmp127, tmp130)
    else:
      #ATStailcalseq_beg
      apy0 = tmp128
      arg0 = apy0
      funlab_py = 1 #__patsflab__ats2pypre_list_aux_33
      #ATStailcalseq_end
    #endif
    return
  mbranch_1 = { 1: __atstmplab41, 2: __atstmplab42, 3: __atstmplab43, 4: __atstmplab44 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_aux_33
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret126


def ats2pypre_list_map(arg0, arg1):
  tmpret131 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_map
  tmpret131 = _ats2pypre_list_aux_35(arg1, arg0)
  return tmpret131


def _ats2pypre_list_aux_35(env0, arg0):
  tmpret132 = None
  tmp133 = None
  tmp134 = None
  tmp135 = None
  tmp136 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab45():
    nonlocal env0, arg0
    nonlocal tmpret132, tmp133, tmp134, tmp135, tmp136
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab48
    __atstmplab46()
    return
  def __atstmplab46():
    nonlocal env0, arg0
    nonlocal tmpret132, tmp133, tmp134, tmp135, tmp136
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret132 = None
    return
  def __atstmplab47():
    nonlocal env0, arg0
    nonlocal tmpret132, tmp133, tmp134, tmp135, tmp136
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab48()
    return
  def __atstmplab48():
    nonlocal env0, arg0
    nonlocal tmpret132, tmp133, tmp134, tmp135, tmp136
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp133 = arg0[0]
    tmp134 = arg0[1]
    tmp135 = env0[0](env0, tmp133)
    tmp136 = _ats2pypre_list_aux_35(env0, tmp134)
    tmpret132 = (tmp135, tmp136)
    return
  mbranch_1 = { 1: __atstmplab45, 2: __atstmplab46, 3: __atstmplab47, 4: __atstmplab48 }
  #__patsflab__ats2pypre_list_aux_35
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret132


def ats2pypre_list_foldleft(arg0, arg1, arg2):
  tmpret137 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_foldleft
  tmpret137 = _ats2pypre_list_loop_37(arg2, arg1, arg0)
  return tmpret137


def _ats2pypre_list_loop_37(env0, arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret138 = None
  tmp139 = None
  tmp140 = None
  tmp141 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab49():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret138, tmp139, tmp140, tmp141
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg1)): tmplab_py = 4 ; return#__atstmplab52
    __atstmplab50()
    return
  def __atstmplab50():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret138, tmp139, tmp140, tmp141
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret138 = arg0
    return
  def __atstmplab51():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret138, tmp139, tmp140, tmp141
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab52()
    return
  def __atstmplab52():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret138, tmp139, tmp140, tmp141
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp139 = arg1[0]
    tmp140 = arg1[1]
    tmp141 = env0[0](env0, arg0, tmp139)
    #ATStailcalseq_beg
    apy0 = tmp141
    apy1 = tmp140
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_list_loop_37
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab49, 2: __atstmplab50, 3: __atstmplab51, 4: __atstmplab52 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_list_loop_37
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret138


def ats2pypre_list_foldright(arg0, arg1, arg2):
  tmpret142 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list_foldright
  tmpret142 = _ats2pypre_list_aux_39(arg1, arg0, arg2)
  return tmpret142


def _ats2pypre_list_aux_39(env0, arg0, arg1):
  tmpret143 = None
  tmp144 = None
  tmp145 = None
  tmp146 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab53():
    nonlocal env0, arg0, arg1
    nonlocal tmpret143, tmp144, tmp145, tmp146
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab56
    __atstmplab54()
    return
  def __atstmplab54():
    nonlocal env0, arg0, arg1
    nonlocal tmpret143, tmp144, tmp145, tmp146
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret143 = arg1
    return
  def __atstmplab55():
    nonlocal env0, arg0, arg1
    nonlocal tmpret143, tmp144, tmp145, tmp146
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab56()
    return
  def __atstmplab56():
    nonlocal env0, arg0, arg1
    nonlocal tmpret143, tmp144, tmp145, tmp146
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp144 = arg0[0]
    tmp145 = arg0[1]
    tmp146 = _ats2pypre_list_aux_39(env0, tmp145, arg1)
    tmpret143 = env0[0](env0, tmp144, tmp146)
    return
  mbranch_1 = { 1: __atstmplab53, 2: __atstmplab54, 3: __atstmplab55, 4: __atstmplab56 }
  #__patsflab__ats2pypre_list_aux_39
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret143

######
##
## end-of-compilation-unit
##
######
