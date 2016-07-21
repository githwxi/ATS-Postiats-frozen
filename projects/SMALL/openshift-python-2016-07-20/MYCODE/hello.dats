(* ****** ****** *)
//
#include
"share/atspre_define.hats"
#include
"{$LIBATSCC2PY3}/staloadall.hats"
//
(* ****** ****** *)

#define ATS_DYNLOADFLAG 0

(* ****** ****** *)
//
extern
fun hello(): string = "mac#"
//
implement
hello() = "Hello from [patsopt+atscc2py3]!"
//
(* ****** ****** *)
%{^
import sys
######
from libatscc2py_all import *
######
sys.setrecursionlimit(1000000)
######
%} // end of [%{^]

(* ****** ****** *)

(* end of [hello.dats] *)
