(* ****** ****** *)
(*
** Sieve
*)
(* ****** ****** *)
(*
##myatsccdef=\
patsopt -d $1 | \
atscc2js -o $fname($1)_dats.js -i -
*)
(* ****** ****** *)
//
#define
ATS_DYNLOADFLAG 0
//
#define
ATS_STATIC_PREFIX "Sieve__"
//
(* ****** ****** *)
//
// HX: for accessing LIBATSCC2JS 
//
#define
LIBATSCC2JS_targetloc
"$PATSHOME/contrib\
/libatscc2js/ATS2-0.3.2" // latest stable release
//
#include
"{$LIBATSCC2JS}/staloadall.hats" // for prelude stuff
#staload
"{$LIBATSCC2JS}/SATS/print.sats" // for print into a store
//
(* ****** ****** *)
//
extern
fun
sieve
(
xs: stream(int)
) : stream(int) = "mac#"
//
(* ****** ****** *)

implement
sieve(xs) = $delay
let
//
val-
stream_cons(x0, xs) = !xs
//
in
  stream_cons(x0, sieve((xs).filter()(lam(x) => x % x0 > 0)))
end // end of [sieve]

(* ****** ****** *)
//
extern
fun
thePrime_fnext
(
// argumentless
)
:
(() -> int) = "mac#"
//
implement
thePrime_fnext
  ((*void*)) = let
//
val
ps =
sieve(from(2)) where
{
fun
from
(
n : int
) : stream(int) =
(
$delay
(stream_cons(n, from(n+1)))
)
} (* end of [val] *)
//
val r0 = ref{stream(int)}(ps)
//
fun
next() = p0 where
{
  val ps = r0[]
  val-
  stream_cons(p0, ps) = !ps
  val ((*void*)) = r0[] := ps
}
//
in
  cloref2fun0(lam() => next((*void*)))
end // end of [thePrime_next]
//
(* ****** ****** *)

%{$
//
export {thePrime_fnext};
//
%} // end of [%{$]

(* ****** ****** *)

(* end of [sieve.dats] *)
