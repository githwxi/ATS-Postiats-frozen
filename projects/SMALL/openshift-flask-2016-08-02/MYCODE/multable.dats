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
//
implement
gprint_newline<>
(
// argmentless
) = gprint_string<>("<br>")
//
(* ****** ****** *)
//
extern
fun
multable_create(): string = "mac#"
//
implement
multable_create() = let
//
val out = PYlist_nil{string}()
//
implement
gprint_string<>(x) = PYlist_append(out, x)
//
fun
genall
(
  i: int
) : void =
(
if (i > 1)
  then (genall(i-1); gprint_newline(); genone(i, 1))
  else genone(1, 1)
) (* end of [if] *)
//
and
genone
(
  i: int, j: int
) : void =
if
i >= j
then
(
  if j > 1 then gprint(" | ");
  gprint!(j, " x ", i, " = ");
  if(j*i < 10) then gprint("0"); gprint(j*i); genone(i, j+1)
) (* end of [then] *)
//
val () = gprint!("<!DOCTYPE html>\n")
val () = gprint!("<html>\n")
//
val () = gprint!("<head>\n")
val () = gprint!("<meta charset=\"utf-8\">\n")
val () = gprint!("<title>MultiplicationTable</title>\n")
val () = gprint!("</head>\n")
//
val () = gprint!("<body>\n")
val () = gprint!("<h1>Multiplication Table</h1>")
val () = gprint!("<pre>\n")
val () = genall(9)
val () = gprint!("</pre>\n")
val () = gprint!("</body>\n")
//
val () = gprint!("</html>\n")
//
in
  PYlist_string_join(out)
end // end of [multable_create]
//
(* ****** ****** *)

%{^
import sys
######
sys.setrecursionlimit(1000000)
######
from libatscc2py3_all import *
from libatscc2py3_all_pylibc import *
######
%} // end of [%{^]

(* ****** ****** *)

(* end of [multable.dats] *)
