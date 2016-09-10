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

local

fun
{a:t@ype}
choice
(
  xs: List0(a)
) : a = let
  val n0 = length(xs)
  val () = assertloc(n0 > 0)
in
  list_get_at(xs, randint(0, n0-1))
end // end of [choice]

fun
generate_insult
(
// argless
) : string = let
//
val
first_adjs =
"artless"::
"bawdy"::
"beslubbering"::
"bootless"::
"churlish"::nil{string}()
val
second_adjs =
"base-court"::
"bat-fowling"::
"beef-witted"::
"beetle-headed"::
"boil-brained"::nil{string}()
//
val
nouns =
"apple_join"::
"baggage"::
"barnacle"::
"bladder"::
"boar-pig"::nil{string}()
//
in
  choice(first_adjs) + " " + choice(second_adjs) + " " + choice(nouns)
end // end of [generate_insult]

in (* in-of-local *)

fun
insult() = "Thou " + generate_insult() + "!"
and
insult_name(name: string) = 
  name + ", thou " + generate_insult() + "!"

end // end of [local]

(* ****** ****** *)
//
extern
fun
hello(): string = "mac#"
//
implement hello() = insult()
//
extern
fun
hello_name(string): string = "mac#"
//
implement hello_name(name) = insult_name(name)
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

(* end of [hello.dats] *)
