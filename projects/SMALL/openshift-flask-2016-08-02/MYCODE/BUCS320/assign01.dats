(* ****** ****** *)

#define ATS_DYNLOADFLAG 0

(* ****** ****** *)
//
#include
"share/atspre_define.hats"
#include
"{$LIBATSCC2PY3}/staloadall.hats"
//
staload
"{$LIBATSCC2PY3}/SATS/PYLIBC/random.sats"
staload
"{$LIBATSCC2PY3}/SATS/PYLIBC/datetime.sats"
//
(* ****** ****** *)

staload UN = "prelude/SATS/unsafe.sats"

(* ****** ****** *)
//
extern
fun
assign01_create
(
// argumentless
) : string = "mac#"
//
implement
assign01_create() = let
//
val os = $extval(ptr, "os")
val cwd =
  $extmcall(string, os, "getcwd")
//
val
path = "\
app-root/repo/\
MYDATA/BUCS320/assign01.html\
" // end of [val]
//
val
opt =
fileref_open_opt(path, $UN.cast("r"))
in
//
case+ opt of
//
| ~Some_vt(filr) => page where
  {
     val page =
       fileref_get_file_string(filr)
     // end of [val]
     val ((*closed*)) = fileref_close(filr)
  }
//
| ~None_vt((*void*)) =>
  (
    "<p>" + cwd + "</p>\n" +
    "<p>IOError: [assign01.html] cannot be opened!</p>\n"
  ) (* end of [None_vt] *)
//
end // end of [assign01_create]
//
(* ****** ****** *)

%{^
######
import os
import sys
######
from libatscc2py3_all import *
from libatscc2py3_all_pylibc import *
######
sys.setrecursionlimit(1000000)
######
%} // end of [%{^]

(* ****** ****** *)

(* end of [assign01.dats] *)
