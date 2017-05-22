(*
** Assign0: Ex3
*)

(* ****** ****** *)

%{^
######
import sys
######
from libatscc2py3_all import *
######
sys.setrecursionlimit(1000000)
######
%} // end of [%{^]

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
fun
count1 : int -> int
//
extern
fun
assign0_ex3_2_test : (int, int) -> bool = "mac#"
//
(* ****** ****** *)
//
implement
count1
  (n) =
(
  if n > 0 then count1(n/2) + n%2 else 0
)
//
(* ****** ****** *)
//
extern
fun
binrev :
{n:nat} int(n) -> int = "mac#binrev"
//
//
extern
fun
assign0_ex3_3_test : (int, int) -> bool = "mac#"
//
(* ****** ****** *)

implement
binrev(n) =
aux(n, 0) where
{
//
fun
aux
{n:nat} .<n>.
(
  n: int(n), res: int
) : int =
(
if (n > 0) then aux(n/2, 2*res + n%2) else res
) (* end of [if] *)
//
} (* end of [binrev] *)

(* ****** ****** *)

implement
assign0_ex3_2_test
  (arg, retval) = let
//
val arg = g1ofg0(arg)
//
in
  if arg >= 0 then (count1(arg) = retval) else false
end // end of [assign0_ex3_2_test]

(* ****** ****** *)

implement
assign0_ex3_3_test
  (arg, retval) = let
//
val arg = g1ofg0(arg)
//
in
  if arg >= 0 then (binrev(arg) = retval) else false
end // end of [assign0_ex3_3_test]

(* ****** ****** *)

(* end of [assign0_ex3_3.dats] *)
