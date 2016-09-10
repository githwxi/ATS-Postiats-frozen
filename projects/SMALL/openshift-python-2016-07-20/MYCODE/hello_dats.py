######
##
## The Python3 code
## is generated from ATS source by atscc2py3
## The starting compilation time is: 2016-7-22: 16h:59m
##
######

######
#ATSextcode_beg()
######
import sys
######
from libatscc2py_all import *
from ats2pylibc_random_cats import *
from ats2pylibc_datetime_cats import *
######
sys.setrecursionlimit(1000000)
######
######
#ATSextcode_end()
######

def generate_insult_1():
  tmpret6 = None
  tmp7 = None
  tmp8 = None
  tmp9 = None
  tmp10 = None
  tmp11 = None
  tmp12 = None
  tmp13 = None
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
  tmp35 = None
  tmp42 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_generate_insult_1
  tmp12 = None
  tmp11 = ("churlish", tmp12)
  tmp10 = ("bootless", tmp11)
  tmp9 = ("beslubbering", tmp10)
  tmp8 = ("bawdy", tmp9)
  tmp7 = ("artless", tmp8)
  tmp18 = None
  tmp17 = ("boil-brained", tmp18)
  tmp16 = ("beetle-headed", tmp17)
  tmp15 = ("beef-witted", tmp16)
  tmp14 = ("bat-fowling", tmp15)
  tmp13 = ("base-court", tmp14)
  tmp24 = None
  tmp23 = ("boar-pig", tmp24)
  tmp22 = ("bladder", tmp23)
  tmp21 = ("barnacle", tmp22)
  tmp20 = ("baggage", tmp21)
  tmp19 = ("apple_join", tmp20)
  tmp28 = choice_0__0__1(tmp7)
  tmp27 = ats2pypre_string_append(tmp28, " ")
  tmp35 = choice_0__0__2(tmp13)
  tmp26 = ats2pypre_string_append(tmp27, tmp35)
  tmp25 = ats2pypre_string_append(tmp26, " ")
  tmp42 = choice_0__0__3(tmp19)
  tmpret6 = ats2pypre_string_append(tmp25, tmp42)
  return tmpret6


def choice_0__0__1(arg0):
  tmpret0__1 = None
  tmp1__1 = None
  tmp3__1 = None
  tmp4__1 = None
  tmp5__1 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_choice_0
  tmp1__1 = ats2pypre_list_length(arg0)
  tmp3__1 = ats2pypre_gt_int1_int1(tmp1__1, 0)
  ats2pypre_assert_errmsg_bool1(tmp3__1, "/home/hwxi/Research/OPENSHIFT/insultapp/MYCODE/hello.dats: 408(line=32, offs=12) -- 425(line=32, offs=29)")
  tmp5__1 = ats2pypre_sub_int1_int1(tmp1__1, 1)
  tmp4__1 = ats2pylibc_random_randint(0, tmp5__1)
  tmpret0__1 = ats2pypre_list_get_at(arg0, tmp4__1)
  return tmpret0__1


def choice_0__0__2(arg0):
  tmpret0__2 = None
  tmp1__2 = None
  tmp3__2 = None
  tmp4__2 = None
  tmp5__2 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_choice_0
  tmp1__2 = ats2pypre_list_length(arg0)
  tmp3__2 = ats2pypre_gt_int1_int1(tmp1__2, 0)
  ats2pypre_assert_errmsg_bool1(tmp3__2, "/home/hwxi/Research/OPENSHIFT/insultapp/MYCODE/hello.dats: 408(line=32, offs=12) -- 425(line=32, offs=29)")
  tmp5__2 = ats2pypre_sub_int1_int1(tmp1__2, 1)
  tmp4__2 = ats2pylibc_random_randint(0, tmp5__2)
  tmpret0__2 = ats2pypre_list_get_at(arg0, tmp4__2)
  return tmpret0__2


def choice_0__0__3(arg0):
  tmpret0__3 = None
  tmp1__3 = None
  tmp3__3 = None
  tmp4__3 = None
  tmp5__3 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_choice_0
  tmp1__3 = ats2pypre_list_length(arg0)
  tmp3__3 = ats2pypre_gt_int1_int1(tmp1__3, 0)
  ats2pypre_assert_errmsg_bool1(tmp3__3, "/home/hwxi/Research/OPENSHIFT/insultapp/MYCODE/hello.dats: 408(line=32, offs=12) -- 425(line=32, offs=29)")
  tmp5__3 = ats2pypre_sub_int1_int1(tmp1__3, 1)
  tmp4__3 = ats2pylibc_random_randint(0, tmp5__3)
  tmpret0__3 = ats2pypre_list_get_at(arg0, tmp4__3)
  return tmpret0__3


def insult_5():
  tmpret49 = None
  tmp50 = None
  tmp51 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_insult_5
  tmp51 = generate_insult_1()
  tmp50 = ats2pypre_string_append("Thou ", tmp51)
  tmpret49 = ats2pypre_string_append(tmp50, "!")
  return tmpret49


def insult_name_6(arg0):
  tmpret52 = None
  tmp53 = None
  tmp54 = None
  tmp55 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_insult_name_6
  tmp54 = ats2pypre_string_append(arg0, ", thou ")
  tmp55 = generate_insult_1()
  tmp53 = ats2pypre_string_append(tmp54, tmp55)
  tmpret52 = ats2pypre_string_append(tmp53, "!")
  return tmpret52


def hello():
  tmpret56 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_hello
  tmpret56 = insult_5()
  return tmpret56


def hello_name(arg0):
  tmpret57 = None
  funlab_py = None
  tmplab_py = None
  #__patsflab_hello_name
  tmpret57 = insult_name_6(arg0)
  return tmpret57

######
##
## end-of-compilation-unit
##
######
