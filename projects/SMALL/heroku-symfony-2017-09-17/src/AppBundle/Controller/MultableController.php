<?php
//
namespace AppBundle\Controller;
//
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
//
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
//
$ATSCC2PHP = __DIR__."/../../Atscc2php";
/*
define("ATSCC2PHP", __DIR__."/../../Atscc2php");
*/
//
require_once $ATSCC2PHP . "/libatscc2php_all.php";
include_once $ATSCC2PHP . "/DATS/lectures/02/multable_dats.php";
//
class
MultableController extends Controller
{
    /**
     * @Route("/multable", name="multable")
     */
    public
    function multableAction()
    {
      return new Response(multable_main());
    }
}
