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
ATS_STATIC_PREFIX "_ats2cljpre_stream_vt_"
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
//
staload "./../basics_clj.sats"
//
(* ****** ****** *)
//
staload "./../SATS/bool.sats"
staload "./../SATS/integer.sats"
//
(* ****** ****** *)
//
staload "./../SATS/print.sats"
//
(* ****** ****** *)
//
staload "./../SATS/list.sats"
staload "./../SATS/reference.sats"
//
(* ****** ****** *)

staload "./../SATS/stream.sats"
staload "./../SATS/stream_vt.sats"

(* ****** ****** *)
//
#include "{$LIBATSCC}/DATS/stream_vt.dats"
//
(* ****** ****** *)

(* end of [stream_vt.dats] *)
