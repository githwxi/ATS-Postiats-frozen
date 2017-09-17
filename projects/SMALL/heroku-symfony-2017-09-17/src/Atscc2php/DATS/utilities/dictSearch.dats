(* ****** ****** *)
(*
##myatsccdef=\
patsopt -d $1 | \
atscc2php -i - > $fname($1)_$fname_ext($1).php
*)
(* ****** ****** *)
//
#define
ATS_DYNLOADFLAG 0
//
(* ****** ****** *)
//
#define
LIBATSCC2PHP_targetloc
"$PATSHOME\
/contrib/libatscc2php/ATS2-0.3.2"
#include
"{$LIBATSCC2PHP}/staloadall.hats"
//
(* ****** ****** *)
//
#staload
"{$LIBATSCC2PHP}/SATS/BUCS320/words.sats"
//
(* ****** ****** *)
//
typedef word = string
//
(* ****** ****** *)
//
extern
fun
dictSearch_sing(w0: word): bool = "mac#"
extern
fun
dictSearch_list
  (ws: list0(word)): list0(bool) = "mac#"
extern
fun
dictSearch_list_lazy
  (ws: list0(word)): stream_vt(bool) = "mac#"
//
(* ****** ****** *)
//
implement
dictSearch_sing
(
  w0
) =
(
case-
dictSearch_list
(list0_sing(w0))
of // case+
| list0_cons(ans, _) => ans
)
//
(* ****** ****** *)
//
implement
dictSearch_list
(
  ws
) =
list0_of_list_vt
(stream2list_vt(dictSearch_list_lazy(ws)))
//
(* ****** ****** *)

implement
dictSearch_list_lazy
(
  ws
) =
  aux00(ws, xs) where
{
//
fun
aux00
(
ws: list0(word),
xs: stream_vt(word)
) : stream_vt(bool) = $ldelay
(
case+ ws of
| list0_nil() =>
  (lazy_vt_free(xs); stream_vt_nil())
| list0_cons(w0, ws) => !(aux10(w0, ws, xs))
, (lazy_vt_free(xs)) // called when freed
)
//
and
aux01
(
x0: word,
ws: list0(word),
xs: stream_vt(word)
) : stream_vt(bool) = $ldelay
(
case+ ws of
| list0_nil() =>
  (lazy_vt_free(xs);
   stream_vt_nil(*void*))
| list0_cons(w0, ws) => let
    val
    sgn = compare(w0, x0)
  in
    ifcase
    | sgn > 0 =>
      !(aux10(w0, ws, xs))
    | sgn < 0 =>
      stream_vt_cons
        (false, aux01(x0, ws, xs))
      // end of [sgn < 0]
    | _ (* sgn = 0 *) =>
      stream_vt_cons(true, aux01(x0, ws, xs))
  end // end of [list0_cons]
, (lazy_vt_free(xs)) // called when freed
)
//
and
aux10
(
w0: word,
ws: list0(word),
xs: stream_vt(word)
) : stream_vt(bool) = $ldelay
(
case+ !xs of
| ~stream_vt_nil() =>
  stream_vt_cons
    (false, auxend(ws))
  // stream_vt_cons
| ~stream_vt_cons(x0, xs) => let
    val sgn = compare(w0, x0)
  in
    ifcase
    | sgn > 0 =>
      !(aux10(w0, ws, xs))
    | sgn < 0 =>
      stream_vt_cons
        (false, aux01(x0, ws, xs))
      // end of [sgn < 0]
    | _ (* sgn = 0 *) =>
      stream_vt_cons(true, aux01(x0, ws, xs))
  end // end of [stream_vt_cons]
, (lazy_vt_free(xs)) // called when freed
)
//
and
auxend
(
ws: list0(word)
) : stream_vt(bool) = $ldelay
(
case+ ws of
| list0_nil() => stream_vt_nil()
| list0_cons(_, ws) => stream_vt_cons(false, auxend(ws))
)
//
val xs = theWords_streamize()
//
} (* end of [dictSearch_stream_vt] *)

(* ****** ****** *)

(* end of [dictSearch.dats] *)
