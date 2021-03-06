(*
** For writing ATS code
** that translates into Clojure
*)

(* ****** ****** *)

#define ATS_DYNLOADFLAG 0

(* ****** ****** *)
//
// HX-2014-08:
// prefix for external names
//
#define
ATS_EXTERN_PREFIX "ats2cljpre_"
#define
ATS_STATIC_PREFIX "_ats2cljpre_list_"
//
(* ****** ****** *)
//
#include
"share/atspre_define.hats"
//
(* ****** ****** *)
//
staload
UN =
"prelude/SATS/unsafe.sats"
//
(* ****** ****** *)

staload "./../basics_clj.sats"

(* ****** ****** *)
//
staload "./../SATS/integer.sats"
//
(* ****** ****** *)
//
staload "./../SATS/list.sats"
staload "./../SATS/list_vt.sats"
//
(* ****** ****** *)
//
#include "{$LIBATSCC}/DATS/list_vt.dats"
//
(* ****** ****** *)

(* end of [list_vt.dats] *)
