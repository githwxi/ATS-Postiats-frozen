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
######
#ATSextcode_end()
######

def _ats2pypre_stream_patsfun_1__closurerize(env0, env1):
  def _ats2pypre_stream_patsfun_1__cfun(cenv): return _ats2pypre_stream_patsfun_1(cenv[1], cenv[2])
  return (_ats2pypre_stream_patsfun_1__cfun, env0, env1)

def _ats2pypre_stream_patsfun_3__closurerize(env0, env1):
  def _ats2pypre_stream_patsfun_3__cfun(cenv): return _ats2pypre_stream_patsfun_3(cenv[1], cenv[2])
  return (_ats2pypre_stream_patsfun_3__cfun, env0, env1)

def _ats2pypre_stream_patsfun_6__closurerize(env0, env1):
  def _ats2pypre_stream_patsfun_6__cfun(cenv): return _ats2pypre_stream_patsfun_6(cenv[1], cenv[2])
  return (_ats2pypre_stream_patsfun_6__cfun, env0, env1)

def _ats2pypre_stream_patsfun_8__closurerize(env0):
  def _ats2pypre_stream_patsfun_8__cfun(cenv): return _ats2pypre_stream_patsfun_8(cenv[1])
  return (_ats2pypre_stream_patsfun_8__cfun, env0)

def _ats2pypre_stream_patsfun_10__closurerize(env0):
  def _ats2pypre_stream_patsfun_10__cfun(cenv): return _ats2pypre_stream_patsfun_10(cenv[1])
  return (_ats2pypre_stream_patsfun_10__cfun, env0)

def _ats2pypre_stream_patsfun_12__closurerize(env0, env1):
  def _ats2pypre_stream_patsfun_12__cfun(cenv): return _ats2pypre_stream_patsfun_12(cenv[1], cenv[2])
  return (_ats2pypre_stream_patsfun_12__cfun, env0, env1)

def ats2pypre_stream_map_cloref(arg0, arg1):
  tmpret0 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream_map_cloref
  tmpret0 = [0, _ats2pypre_stream_patsfun_1__closurerize(arg0, arg1)]
  return tmpret0


def _ats2pypre_stream_patsfun_1(env0, env1):
  tmpret1 = None
  tmp2 = None
  tmp3 = None
  tmp4 = None
  tmp5 = None
  tmp6 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab0():
    nonlocal env0, env1
    nonlocal tmpret1, tmp2, tmp3, tmp4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(tmp2)): tmplab_py = 4 ; return#__atstmplab3
    __atstmplab1()
    return
  def __atstmplab1():
    nonlocal env0, env1
    nonlocal tmpret1, tmp2, tmp3, tmp4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret1 = None
    return
  def __atstmplab2():
    nonlocal env0, env1
    nonlocal tmpret1, tmp2, tmp3, tmp4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab3()
    return
  def __atstmplab3():
    nonlocal env0, env1
    nonlocal tmpret1, tmp2, tmp3, tmp4, tmp5, tmp6
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp3 = tmp2[0]
    tmp4 = tmp2[1]
    tmp5 = env1[0](env1, tmp3)
    tmp6 = ats2pypre_stream_map_cloref(tmp4, env1)
    tmpret1 = (tmp5, tmp6)
    return
  mbranch_1 = { 1: __atstmplab0, 2: __atstmplab1, 3: __atstmplab2, 4: __atstmplab3 }
  #__patsflab__ats2pypre_stream_patsfun_1
  ATSPMVlazyval_eval(env0); tmp2 = env0[1]
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret1


def ats2pypre_stream_filter_cloref(arg0, arg1):
  tmpret7 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream_filter_cloref
  tmpret7 = [0, _ats2pypre_stream_patsfun_3__closurerize(arg0, arg1)]
  return tmpret7


def _ats2pypre_stream_patsfun_3(env0, env1):
  tmpret8 = None
  tmp9 = None
  tmp10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
  tmp14 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab4():
    nonlocal env0, env1
    nonlocal tmpret8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(tmp9)): tmplab_py = 4 ; return#__atstmplab7
    __atstmplab5()
    return
  def __atstmplab5():
    nonlocal env0, env1
    nonlocal tmpret8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret8 = None
    return
  def __atstmplab6():
    nonlocal env0, env1
    nonlocal tmpret8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab7()
    return
  def __atstmplab7():
    nonlocal env0, env1
    nonlocal tmpret8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp10 = tmp9[0]
    tmp11 = tmp9[1]
    tmp12 = env1[0](env1, tmp10)
    if (tmp12):
      tmp13 = ats2pypre_stream_filter_cloref(tmp11, env1)
      tmpret8 = (tmp10, tmp13)
    else:
      tmp14 = ats2pypre_stream_filter_cloref(tmp11, env1)
      ATSPMVlazyval_eval(tmp14); tmpret8 = tmp14[1]
    #endif
    return
  mbranch_1 = { 1: __atstmplab4, 2: __atstmplab5, 3: __atstmplab6, 4: __atstmplab7 }
  #__patsflab__ats2pypre_stream_patsfun_3
  ATSPMVlazyval_eval(env0); tmp9 = env0[1]
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret8


def ats2pypre_stream_tabulate_cloref(arg0):
  tmpret15 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream_tabulate_cloref
  tmpret15 = _ats2pypre_stream_aux_5(arg0, 0)
  return tmpret15


def _ats2pypre_stream_aux_5(env0, arg0):
  tmpret16 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__ats2pypre_stream_aux_5
  tmpret16 = [0, _ats2pypre_stream_patsfun_6__closurerize(env0, arg0)]
  return tmpret16


def _ats2pypre_stream_patsfun_6(env0, env1):
  tmpret17 = None
  tmp18 = None
  tmp19 = None
  tmp20 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__ats2pypre_stream_patsfun_6
  tmp18 = env0[0](env0, env1)
  tmp20 = ats2pypre_add_int1_int1(env1, 1)
  tmp19 = _ats2pypre_stream_aux_5(env0, tmp20)
  tmpret17 = (tmp18, tmp19)
  return tmpret17


def ats2pypre_stream2cloref_exn(arg0):
  tmpret21 = None
  tmp22 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream2cloref_exn
  tmp22 = ats2pypre_ref(arg0)
  tmpret21 = _ats2pypre_stream_patsfun_8__closurerize(tmp22)
  return tmpret21


def _ats2pypre_stream_patsfun_8(env0):
  tmpret23 = None
  tmp24 = None
  tmp25 = None
  tmp26 = None
  tmp27 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab__ats2pypre_stream_patsfun_8
  tmp24 = ats2pypre_ref_get_elt(env0)
  ATSPMVlazyval_eval(tmp24); tmp25 = tmp24[1]
  if(ATSCKptrisnull(tmp25)): ATSINScaseof_fail("/home/hwxi/Research/ATS-Postiats-contrib/contrib/libatscc/DATS/stream.dats: 1532(line=114, offs=5) -- 1556(line=114, offs=29)");
  tmp26 = tmp25[0]
  tmp27 = tmp25[1]
  ats2pypre_ref_set_elt(env0, tmp27)
  tmpret23 = tmp26
  return tmpret23


def ats2pypre_stream2cloref_opt(arg0):
  tmpret29 = None
  tmp30 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream2cloref_opt
  tmp30 = ats2pypre_ref(arg0)
  tmpret29 = _ats2pypre_stream_patsfun_10__closurerize(tmp30)
  return tmpret29


def _ats2pypre_stream_patsfun_10(env0):
  tmpret31 = None
  tmp32 = None
  tmp33 = None
  tmp34 = None
  tmp35 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab8():
    nonlocal env0
    nonlocal tmpret31, tmp32, tmp33, tmp34, tmp35
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(tmp33)): tmplab_py = 4 ; return#__atstmplab11
    __atstmplab9()
    return
  def __atstmplab9():
    nonlocal env0
    nonlocal tmpret31, tmp32, tmp33, tmp34, tmp35
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret31 = None
    return
  def __atstmplab10():
    nonlocal env0
    nonlocal tmpret31, tmp32, tmp33, tmp34, tmp35
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab11()
    return
  def __atstmplab11():
    nonlocal env0
    nonlocal tmpret31, tmp32, tmp33, tmp34, tmp35
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp34 = tmp33[0]
    tmp35 = tmp33[1]
    ats2pypre_ref_set_elt(env0, tmp35)
    tmpret31 = (tmp34, )
    return
  mbranch_1 = { 1: __atstmplab8, 2: __atstmplab9, 3: __atstmplab10, 4: __atstmplab11 }
  #__patsflab__ats2pypre_stream_patsfun_10
  tmp32 = ats2pypre_ref_get_elt(env0)
  ATSPMVlazyval_eval(tmp32); tmp33 = tmp32[1]
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret31


def ats2pypre_stream2cloref_last(arg0, arg1):
  tmpret37 = None
  tmp38 = None
  tmp39 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_stream2cloref_last
  tmp38 = ats2pypre_ref(arg0)
  tmp39 = ats2pypre_ref(arg1)
  tmpret37 = _ats2pypre_stream_patsfun_12__closurerize(tmp38, tmp39)
  return tmpret37


def _ats2pypre_stream_patsfun_12(env0, env1):
  tmpret40 = None
  tmp41 = None
  tmp42 = None
  tmp43 = None
  tmp44 = None
  funlab_py = None
  tmplab_py = None
  mbranch_1 = None
  def __atstmplab12():
    nonlocal env0, env1
    nonlocal tmpret40, tmp41, tmp42, tmp43, tmp44
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    if(ATSCKptriscons(tmp42)): tmplab_py = 4 ; return#__atstmplab15
    __atstmplab13()
    return
  def __atstmplab13():
    nonlocal env0, env1
    nonlocal tmpret40, tmp41, tmp42, tmp43, tmp44
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmpret40 = ats2pypre_ref_get_elt(env1)
    return
  def __atstmplab14():
    nonlocal env0, env1
    nonlocal tmpret40, tmp41, tmp42, tmp43, tmp44
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    __atstmplab15()
    return
  def __atstmplab15():
    nonlocal env0, env1
    nonlocal tmpret40, tmp41, tmp42, tmp43, tmp44
    nonlocal funlab_py, tmplab_py
    nonlocal mbranch_1
    tmplab_py = 0
    tmp43 = tmp42[0]
    tmp44 = tmp42[1]
    ats2pypre_ref_set_elt(env0, tmp44)
    ats2pypre_ref_set_elt(env1, tmp43)
    tmpret40 = tmp43
    return
  mbranch_1 = { 1: __atstmplab12, 2: __atstmplab13, 3: __atstmplab14, 4: __atstmplab15 }
  #__patsflab__ats2pypre_stream_patsfun_12
  tmp41 = ats2pypre_ref_get_elt(env0)
  ATSPMVlazyval_eval(tmp41); tmp42 = tmp41[1]
  #ATScaseofseq_beg
  tmplab_py = 1
  while(1):
    mbranch_1.get(tmplab_py)()
    if (tmplab_py == 0): break
  #ATScaseofseq_end
  return tmpret40

######
##
## end-of-compilation-unit
##
######
