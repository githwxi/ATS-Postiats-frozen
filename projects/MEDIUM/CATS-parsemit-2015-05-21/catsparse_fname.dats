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

staload "./catsparse.sats" // opened

(* ****** ****** *)
//
datatype
filename = FNAME of (string)
//
assume filename_type = filename
//
(* ****** ****** *)

implement
filename_dummy = FNAME ("")
implement
filename_stdin = FNAME ("__STDIN__")

(* ****** ****** *)

implement
filename_make(fname) = FNAME(fname)

(* ****** ****** *)

implement
fprint_filename
  (out, fil) = let
//
val+FNAME (fname) = fil
//
in
  fprint_string (out, fname)
end // end of [fprint_filename]

(* ****** ****** *)

(* end of [catsparse_fname.dats] *)
