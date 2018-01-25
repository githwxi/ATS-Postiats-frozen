(* ****** ****** *)
//
// CATS-parsemit
//
(* ****** ****** *)
//
// HX-2014-07-02: start
//
(* ****** ****** *)
//
#include
"share/atspre_staload.hats"
//
(* ****** ****** *)
//
staload "./catsparse.sats"
staload "./catsparse_typedef.sats"
//
(* ****** ****** *)

staload TYPEDEF =
{
//
staload "./catsparse.sats"
//
typedef
itm = tyrec
and
key = symbol
//
implement
gequal_val_val<key>
  (k1, k2) = (k1 = k2)
//
staload
"libats/SATS/hashtbl_chain.sats"
//
implement
hash_key<key>(sym) =
//
// HX:
// [gidentity] is
// called to circumvent a bug
// in tail-call optimization!!!
//
(
gidentity
(hash_key<string>
(symbol_get_name(sym)))
)
//
implement
hashtbl$recapacitize<>
  () = 1(*resizable*)
//
#define
HX_GLOBALS_targetloc
"\
$PATSHOME/contrib\
/atscntrb/atscntrb-hx-globals"
//
#define CAPACITY 1024
//
#include
"{$HX_GLOBALS}/HATS/ghashtbl_chain.hats"
//
} (* end of [staload] *)

(* ****** ****** *)

implement
typedef_insert
  (name, def) = let
(*
//
val () =
  println! ("typedef_insert")
//
*)
in
//
$TYPEDEF.insert_any (name, def)
//
end // end of [typedef_insert]

(* ****** ****** *)
//
implement
typedef_search_opt
  (name) = $TYPEDEF.search_opt (name)
//
(* ****** ****** *)

(* end of [catsparse_typedef.dats] *)
