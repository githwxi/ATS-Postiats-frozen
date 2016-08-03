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

#define ATS_DYNLOADFLAG 0

(* ****** ****** *)

#define :: cons

(* ****** ****** *)
//
implement
gprint_newline<>
(
// argumentless
) = gprint_string<>("<br>")
//
(* ****** ****** *)
//
extern
fun
QueenPuzzle_solve
(
// argumentless
): string = "mac#"
//
implement
QueenPuzzle_solve() = let
//
(* ****** ****** *)
//
#define N 8 // HX: N can be changed
//
(* ****** ****** *)
//
val out = PYlist_nil{string}()
//
implement
gprint_string<>
  (obj) = PYlist_append(out, obj)
//
(* ****** ****** *)
//
macdef sing = stream_make_sing
macdef intrange = list0_make_intrange
//
fun qsolve(nsol: Nat): void =
(((fix f(n: int): stream(list0(int)) => if(n > 0)then((f(n-1)*intrange(0,N)).map(TYPE{list0(int)})(lam($tup(xs,x))=>cons0(x,xs))).filter()(lam(xs)=>let val-cons0(x0,xs) = xs in xs.iforall()(lam(i, x)=>((x0)!=x)&&(abs(x0-x)!=i+1)) end)else(sing(nil0())))(N)).takeLte(nsol)).iforeach()(lam(i, xs)=>(gprintln!("Solution#", i+1, ":"); xs.rforeach()(lam(x) => ((N).foreach()(lam(i)=>(gprint_string(ifval(i=x," Q", " ."))));gprintln!()));gprintln!()))
//
val () = gprint!("<!DOCTYPE html>\n")
val () = gprint!("<html>\n")
//
val () = gprint!("<head>\n")
val () = gprint!("<meta charset=\"utf-8\">\n")
val () = gprint!("<title>QueenPuzzleSolutions</title>\n")
val () = gprint!("</head>\n")
//
val () = gprint!("<body>\n")
val () = gprint!("<h1>Queen Puzzle Solutions</h1>")
val () = gprint!("<pre>\n")
val () = qsolve(1000000)
val () = gprint!("</pre>\n")
val () = gprint!("</body>\n")
//
val () = gprint!("</html>\n")
//
in
  PYlist_string_join(out)
end // end of [QueenPuzzle_solve]
//
(* ****** ****** *)

%{^
import sys
######
from libatscc2py_all import *
from ats2pylibc_random_cats import *
from ats2pylibc_datetime_cats import *
######
sys.setrecursionlimit(1000000)
######
%} // end of [%{^]

(* ****** ****** *)

(* end of [QueenPuzzle.dats] *)
