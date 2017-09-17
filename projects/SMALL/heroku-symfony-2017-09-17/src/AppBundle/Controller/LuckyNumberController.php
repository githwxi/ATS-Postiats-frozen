<?php
//
namespace AppBundle\Controller;
//
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
//
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
//
$ATSCC2PHP = __DIR__."/../../Atscc2php";
//
require_once $ATSCC2PHP . "/libatscc2php_all.php";
require_once $ATSCC2PHP . "/DATS/tests/luckyNumber_dats.php";
//
class LuckyNumberController extends Controller
{
    /**
     * @Route("/lucky/number/{count}", name="lucky_number", defaults={"count":"10"})
     */
    public
    function
    luckyNumberAction($count)
    {
      $n0 = max(0, min(1000, intval($count)));
      return new Response(luckNumberHtml($n0));
    }
}
