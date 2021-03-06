(*
** Co-lists
*)

(* ****** ****** *)
//
staload
UN =
"prelude/SATS/unsafe.sats"
//
(* ****** ****** *)
//
staload "./basis_chan0.dats"
//
staload "./../SATS/co-list.sats"
//
(* ****** ****** *)

implement
{}(*tmp*)
chanpos_list
  (chpos) = let
//
vtypedef
chan0 = channel0(ptr)
//
val chan0 =
  $UN.castvwtp0{chan0}(chpos)
//
val tag = channel0_recv_val (chan0)
//
in
//
if
iseqz(tag)
then let
//
prval () =
  $UN.castview2void(chan0) in chanpos_list_nil(chan0)
// end of [prval]
end // end of [then]
else let
prval () =
  $UN.castview2void(chan0) in chanpos_list_cons(chan0)
// end of [prval]
end // end of [else]
//
end // end of [chanpos_list]

(* ****** ****** *)

implement
{}(*tmp*)
channeg_list_nil
  (chneg) = () where
{
//
vtypedef
chan0 = channel0(ptr)
//
val
chan0 =
$UN.castvwtp1{chan0}(chneg)
//
val () = 
channel0_send (chan0, $UN.int2ptr(0))
//
prval () = $UN.cast2void(chan0)
//
prval () = $UN.castview2void(chneg)
//
} (* end of [channeg_list_nil] *)

(* ****** ****** *)

implement
{}(*tmp*)
channeg_list_cons
  (chneg) = () where
{
//
vtypedef
chan0 = channel0(ptr)
//
val chan0 =
  $UN.castvwtp1{chan0}(chneg)
//
val ((*void*)) =
  channel0_send (chan0, $UN.int2ptr(1))
//
prval () = $UN.cast2void(chan0)
//
prval () = $UN.castview2void(chneg)
//
} (* end of [channeg_list_cons] *)

(* ****** ****** *)

(* end of [co-list.dats] *)
