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
extern
fun
luckNumberHtml
(
n0: int
) : string = "mac#"
//
implement
luckNumberHtml(n0) = let
//
val out =
PHParref_nil
  {string}((*void*))
//
implement
gprint_string<>
  (str) = PHParref_extend(out, str)
//
implement
gprint_int<>
  (int) = gprint_string<>(strval(int))
implement
gprint_newline<>
  ((*void*)) = PHParref_extend(out, "\n")
//
val () =
gprintln!
("<!DOCTYPE html>")
val () =
gprintln!("<html>")
val () =
gprintln!("<body>")
val () =
gprintln!("<center>")
val () =
gprintln!("<h1>Your randomly generated lucky number(s):</h1>")
val () =
gprintln!("</center>")
val () =
gprintln!("<hr></hr>")
val () =
gprintln!("<ul>")
//
fun
myrand(): int =
$extfcall(int, "rand", 0, 100)
val () =
(n0).foreach()
(lam i => gprintln!("<li>Lucky number: ", myrand(), "</li>"))
//
val () =
gprintln!("</ul>")
val () =
gprintln!("<hr></hr>")
val () =
gprintln!("</body>")
val () =
gprintln!("</html>")
//
in
  PHParref_join(out)
end // end of [luckNumberHtml]

(* ****** ****** *)

(* end of [luckyNumber.dats] *)
