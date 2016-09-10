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
from ats2pypre_integer_cats import *
from ats2pypre_bool_cats import *
######
from ats2pypre_list_dats import *
######
######
#ATSextcode_end()
######

def ats2pypre_ML_list0_length(arg0):
  tmpret2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_length
  tmpret2 = ats2pypre_list_length(arg0)
  return tmpret2


def ats2pypre_ML_list0_last_opt(arg0):
  tmpret3 = None
  tmp7 = None
  tmp8 = None
  tmp9 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab10():
    nonlocal arg0
    nonlocal tmpret3, tmp7, tmp8, tmp9
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab13
    __atstmplab11()
    return
  def __atstmplab11():
    nonlocal arg0
    nonlocal tmpret3, tmp7, tmp8, tmp9
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret3 = None
    return
  def __atstmplab12():
    nonlocal arg0
    nonlocal tmpret3, tmp7, tmp8, tmp9
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab13()
    return
  def __atstmplab13():
    nonlocal arg0
    nonlocal tmpret3, tmp7, tmp8, tmp9
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp7 = arg0[0]
    tmp8 = arg0[1]
    tmp9 = _ats2pypre_ML_list0_loop_4(tmp7, tmp8)
    tmpret3 = (tmp9, )
    return
  mbranch_1 = { 1: __atstmplab10, 2: __atstmplab11, 3: __atstmplab12, 4: __atstmplab13 }
  #__patsflab_list0_last_opt
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret3


def _ats2pypre_ML_list0_loop_4(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret4 = None
  tmp5 = None
  tmp6 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab6():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg1)): tmplab_py = 4 ; return#__atstmplab9
    __atstmplab7()
    return
  def __atstmplab7():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret4 = arg0
    return
  def __atstmplab8():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab9()
    return
  def __atstmplab9():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp5 = arg1[0]
    tmp6 = arg1[1]
    #ATStailcalseq_beg
    apy0 = tmp5
    apy1 = tmp6
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_ML_list0_loop_4
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab6, 2: __atstmplab7, 3: __atstmplab8, 4: __atstmplab9 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_ML_list0_loop_4
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret4


def ats2pypre_ML_list0_get_at_opt(arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
  tmp14 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab14():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab17
    __atstmplab15()
    return
  def __atstmplab15():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret10 = None
    return
  def __atstmplab16():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab17()
    return
  def __atstmplab17():
    nonlocal arg0, arg1
    nonlocal apy0, apy1, tmpret10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp11 = arg0[0]
    tmp12 = arg0[1]
    tmp13 = ats2pypre_gt_int1_int1(arg1, 0)
    if (tmp13):
      tmp14 = ats2pypre_sub_int1_int1(arg1, 1)
      #ATStailcalseq_beg
      apy0 = tmp12
      apy1 = tmp14
      arg0 = apy0
      arg1 = apy1
      funlab_py = 1 #__patsflab_list0_get_at_opt
      #ATStailcalseq_end
    else:
      tmpret10 = (tmp11, )
    #endif
    return
  mbranch_1 = { 1: __atstmplab14, 2: __atstmplab15, 3: __atstmplab16, 4: __atstmplab17 }
  while(1):
    funlab_py = 0
    #__patsflab_list0_get_at_opt
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret10


def ats2pypre_ML_list0_make_intrange_2(arg0, arg1):
  tmpret15 = None
  tmp16 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_make_intrange_2
  tmp16 = ats2pypre_list_make_intrange_2(arg0, arg1)
  tmpret15 = tmp16
  return tmpret15


def ats2pypre_ML_list0_make_intrange_3(arg0, arg1, arg2):
  tmpret17 = None
  tmp18 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_make_intrange_3
  tmp18 = ats2pypre_list_make_intrange_3(arg0, arg1, arg2)
  tmpret17 = tmp18
  return tmpret17


def ats2pypre_ML_list0_snoc(arg0, arg1):
  tmpret30 = None
  tmp31 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_snoc
  tmp31 = ats2pypre_list_snoc(arg0, arg1)
  tmpret30 = tmp31
  return tmpret30


def ats2pypre_ML_list0_extend(arg0, arg1):
  tmpret32 = None
  tmp33 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_extend
  tmp33 = ats2pypre_list_extend(arg0, arg1)
  tmpret32 = tmp33
  return tmpret32


def ats2pypre_ML_list0_append(arg0, arg1):
  tmpret34 = None
  tmp35 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_append
  tmp35 = ats2pypre_list_append(arg0, arg1)
  tmpret34 = tmp35
  return tmpret34


def ats2pypre_ML_list0_reverse(arg0):
  tmpret36 = None
  tmp37 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_reverse
  tmp37 = ats2pypre_list_reverse(arg0)
  tmpret36 = tmp37
  return tmpret36


def ats2pypre_ML_list0_reverse_append(arg0, arg1):
  tmpret38 = None
  tmp39 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_reverse_append
  tmp39 = ats2pypre_list_reverse_append(arg0, arg1)
  tmpret38 = tmp39
  return tmpret38


def ats2pypre_ML_list0_app(arg0, arg1):
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_app
  ats2pypre_ML_list0_foreach(arg0, arg1)
  return#_void


def ats2pypre_ML_list0_foreach(arg0, arg1):
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_foreach
  ats2pypre_list_foreach(arg0, arg1)
  return#_void


def ats2pypre_ML_list0_filter(arg0, arg1):
  tmpret42 = None
  tmp43 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_filter
  tmp43 = ats2pypre_list_filter(arg0, arg1)
  tmpret42 = tmp43
  return tmpret42


def ats2pypre_ML_list0_map(arg0, arg1):
  tmpret44 = None
  tmp45 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_map
  tmp45 = ats2pypre_list_map(arg0, arg1)
  tmpret44 = tmp45
  return tmpret44


def ats2pypre_ML_list0_foldleft(arg0, arg1, arg2):
  tmpret46 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_foldleft
  tmpret46 = _ats2pypre_ML_list0_aux_23(arg2, arg1, arg0)
  return tmpret46


def _ats2pypre_ML_list0_aux_23(env0, arg0, arg1):
  apy0 = None
  apy1 = None
  tmpret47 = None
  tmp48 = None
  tmp49 = None
  tmp50 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab22():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp48, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg1)): tmplab_py = 4 ; return#__atstmplab25
    __atstmplab23()
    return
  def __atstmplab23():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp48, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret47 = arg0
    return
  def __atstmplab24():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp48, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab25()
    return
  def __atstmplab25():
    nonlocal env0, arg0, arg1
    nonlocal apy0, apy1, tmpret47, tmp48, tmp49, tmp50
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp48 = arg1[0]
    tmp49 = arg1[1]
    tmp50 = env0[0](env0, arg0, tmp48)
    #ATStailcalseq_beg
    apy0 = tmp50
    apy1 = tmp49
    arg0 = apy0
    arg1 = apy1
    funlab_py = 1 #__patsflab__ats2pypre_ML_list0_aux_23
    #ATStailcalseq_end
    return
  mbranch_1 = { 1: __atstmplab22, 2: __atstmplab23, 3: __atstmplab24, 4: __atstmplab25 }
  while(1):
    funlab_py = 0
    #__patsflab__ats2pypre_ML_list0_aux_23
    #ATScaseofseq_beg
    tmplab_py = 1
    while(1):
      mbranch_1.get(tmplab_py)()
      if (tmplab_py == 0): break
    #ATScaseofseq_end
    if (funlab_py == 0): break
  return tmpret47


def ats2pypre_ML_list0_foldright(arg0, arg1, arg2):
  tmpret51 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_list0_foldright
  tmpret51 = _ats2pypre_ML_list0_aux_25(arg1, arg2, arg0, arg2)
  return tmpret51


def _ats2pypre_ML_list0_aux_25(env0, env1, arg0, arg1):
  tmpret52 = None
  tmp53 = None
  tmp54 = None
  tmp55 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab26():
    nonlocal env0, env1, arg0, arg1
    nonlocal tmpret52, tmp53, tmp54, tmp55
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(arg0)): tmplab_py = 4 ; return#__atstmplab29
    __atstmplab27()
    return
  def __atstmplab27():
    nonlocal env0, env1, arg0, arg1
    nonlocal tmpret52, tmp53, tmp54, tmp55
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret52 = arg1
    return
  def __atstmplab28():
    nonlocal env0, env1, arg0, arg1
    nonlocal tmpret52, tmp53, tmp54, tmp55
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab29()
    return
  def __atstmplab29():
    nonlocal env0, env1, arg0, arg1
    nonlocal tmpret52, tmp53, tmp54, tmp55
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp53 = arg0[0]
    tmp54 = arg0[1]
    tmp55 = _ats2pypre_ML_list0_aux_25(env0, env1, tmp54, env1)
    tmpret52 = env0[0](env0, tmp53, tmp55)
    return
  mbranch_1 = { 1: __atstmplab26, 2: __atstmplab27, 3: __atstmplab28, 4: __atstmplab29 }
  #__patsflab__ats2pypre_ML_list0_aux_25
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret52

######
##
## end-of-compilation-unit
##
######
