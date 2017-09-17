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
//
require_once $ATSCC2PHP . "/DATS/utilities/dictSearch_dats.php";
//
require_once $ATSCC2PHP . "/libatscc2php_bucs320_words_dats.php";
//
class DictSearchController extends Controller
{
    /**
     * @Route("/api/dict/{word}", name="dict_search")
     */
    public
    function
    apiDictSearchAction($word)
    {
      BUCS320_words_dynload();
      return new JsonResponse(array(dictSearch_sing($word)));
    }
}
