<?php
/*
**
** The PHP code is generated by atscc2php
** The starting compilation time is: 2017-9-16: 23h:21m
**
*/
function
__patsfun_9__closurerize($env0, $env1)
{
  return array(function($cenv, $arg0) { return __patsfun_9($cenv[1], $cenv[2], $arg0); }, $env0, $env1);
}

function
__patsfun_10__closurerize($env0, $env1, $env2)
{
  return array(function($cenv, $arg0) { return __patsfun_10($cenv[1], $cenv[2], $cenv[3], $arg0); }, $env0, $env1, $env2);
}

function
__patsfun_11__closurerize($env0, $env1, $env2)
{
  return array(function($cenv, $arg0) { return __patsfun_11($cenv[1], $cenv[2], $cenv[3], $arg0); }, $env0, $env1, $env2);
}

function
__patsfun_12__closurerize($env0)
{
  return array(function($cenv, $arg0) { return __patsfun_12($cenv[1], $arg0); }, $env0);
}


function
dictSearch_sing($arg0)
{
//
  $tmpret0 = NULL;
  $tmp1 = NULL;
  $tmp2 = NULL;
  $tmp7 = NULL;
//
  __patsflab_dictSearch_sing:
  $tmp2 = _057_home_057_hwxi_057_Research_057_ATS_055_Postiats_057_contrib_057_libatscc2php_057_ATS2_055_0_056_3_056_2_057_SATS_057_ML_057_list0_056_sats__list0_sing__1__1($arg0);
  $tmp1 = dictSearch_list($tmp2);
  // ATScaseofseq_beg
  do {
    // ATSbranchseq_beg
    __atstmplab0:
    if(ATSCKptrisnull($tmp1)) ATSINScaseof_fail("/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/symfony-2017-fall/src/Atscc2php/DATS/utilities/dictSearch.dats: 717(line=52, offs=1) -- 795(line=56, offs=28)");
    __atstmplab1:
    $tmp7 = $tmp1[0];
    $tmpret0 = $tmp7;
    break;
    // ATSbranchseq_end
  } while(0);
  // ATScaseofseq_end
  return $tmpret0;
} // end-of-function


function
_057_home_057_hwxi_057_Research_057_ATS_055_Postiats_057_contrib_057_libatscc2php_057_ATS2_055_0_056_3_056_2_057_SATS_057_ML_057_list0_056_sats__list0_sing__1__1($arg0)
{
//
  $tmpret3__1 = NULL;
  $tmp4__1 = NULL;
//
  __patsflab_list0_sing:
  $tmp4__1 = NULL;
  $tmpret3__1 = array($arg0, $tmp4__1);
  return $tmpret3__1;
} // end-of-function


function
dictSearch_list($arg0)
{
//
  $tmpret9 = NULL;
  $tmp10 = NULL;
  $tmp11 = NULL;
//
  __patsflab_dictSearch_list:
  $tmp11 = dictSearch_list_lazy($arg0);
  $tmp10 = ats2phppre_stream2list_vt($tmp11);
  $tmpret9 = $tmp10;
  return $tmpret9;
} // end-of-function


function
dictSearch_list_lazy($arg0)
{
//
  $tmpret12 = NULL;
  $tmp50 = NULL;
//
  __patsflab_dictSearch_list_lazy:
  $tmp50 = ats2phppre_BUCS320_theWords_streamize();
  $tmpret12 = aux00_5($arg0, $tmp50);
  return $tmpret12;
} // end-of-function


function
aux00_5($arg0, $arg1)
{
//
  $tmpret13 = NULL;
//
  __patsflab_aux00_5:
  $tmpret13 = ATSPMVllazyval(__patsfun_9__closurerize($arg0, $arg1));
  return $tmpret13;
} // end-of-function


function
aux01_6($arg0, $arg1, $arg2)
{
//
  $tmpret20 = NULL;
//
  __patsflab_aux01_6:
  $tmpret20 = ATSPMVllazyval(__patsfun_10__closurerize($arg0, $arg1, $arg2));
  return $tmpret20;
} // end-of-function


function
aux10_7($arg0, $arg1, $arg2)
{
//
  $tmpret32 = NULL;
//
  __patsflab_aux10_7:
  $tmpret32 = ATSPMVllazyval(__patsfun_11__closurerize($arg0, $arg1, $arg2));
  return $tmpret32;
} // end-of-function


function
auxend_8($arg0)
{
//
  $tmpret45 = NULL;
//
  __patsflab_auxend_8:
  $tmpret45 = ATSPMVllazyval(__patsfun_12__closurerize($arg0));
  return $tmpret45;
} // end-of-function


function
__patsfun_9($env0, $env1, $arg0)
{
//
  $tmpret14 = NULL;
  $tmp15 = NULL;
  $tmp16 = NULL;
  $tmp18 = NULL;
//
  __patsflab___patsfun_9:
  if($arg0) {
    // ATScaseofseq_beg
    do {
      // ATSbranchseq_beg
      __atstmplab2:
      if(ATSCKptriscons($env0)) goto __atstmplab5;
      __atstmplab3:
      atspre_lazy_vt_free($env1);
      $tmpret14 = NULL;
      break;
      // ATSbranchseq_end
      // ATSbranchseq_beg
      __atstmplab4:
      __atstmplab5:
      $tmp15 = $env0[0];
      $tmp16 = $env0[1];
      $tmp18 = aux10_7($tmp15, $tmp16, $env1);
      $tmpret14 = ATSPMVllazyval_eval($tmp18);
      break;
      // ATSbranchseq_end
    } while(0);
    // ATScaseofseq_end
  } else {
    atspre_lazy_vt_free($env1);
  } // endif
  return $tmpret14;
} // end-of-function


function
__patsfun_10($env0, $env1, $env2, $arg0)
{
//
  $tmpret21 = NULL;
  $tmp22 = NULL;
  $tmp23 = NULL;
  $tmp25 = NULL;
  $tmp26 = NULL;
  $tmp27 = NULL;
  $tmp28 = NULL;
  $tmp29 = NULL;
  $tmp30 = NULL;
//
  __patsflab___patsfun_10:
  if($arg0) {
    // ATScaseofseq_beg
    do {
      // ATSbranchseq_beg
      __atstmplab6:
      if(ATSCKptriscons($env1)) goto __atstmplab9;
      __atstmplab7:
      atspre_lazy_vt_free($env2);
      $tmpret21 = NULL;
      break;
      // ATSbranchseq_end
      // ATSbranchseq_beg
      __atstmplab8:
      __atstmplab9:
      $tmp22 = $env1[0];
      $tmp23 = $env1[1];
      $tmp25 = ats2phppre_compare_string_string($tmp22, $env0);
      $tmp26 = ats2phppre_gt_int1_int1($tmp25, 0);
      if($tmp26) {
        $tmp27 = aux10_7($tmp22, $tmp23, $env2);
        $tmpret21 = ATSPMVllazyval_eval($tmp27);
      } else {
        $tmp28 = ats2phppre_lt_int1_int1($tmp25, 0);
        if($tmp28) {
          $tmp29 = aux01_6($env0, $tmp23, $env2);
          $tmpret21 = array(false, $tmp29);
        } else {
          $tmp30 = aux01_6($env0, $tmp23, $env2);
          $tmpret21 = array(true, $tmp30);
        } // endif
      } // endif
      break;
      // ATSbranchseq_end
    } while(0);
    // ATScaseofseq_end
  } else {
    atspre_lazy_vt_free($env2);
  } // endif
  return $tmpret21;
} // end-of-function


function
__patsfun_11($env0, $env1, $env2, $arg0)
{
//
  $tmpret33 = NULL;
  $tmp34 = NULL;
  $tmp35 = NULL;
  $tmp36 = NULL;
  $tmp37 = NULL;
  $tmp38 = NULL;
  $tmp39 = NULL;
  $tmp40 = NULL;
  $tmp41 = NULL;
  $tmp42 = NULL;
  $tmp43 = NULL;
//
  __patsflab___patsfun_11:
  if($arg0) {
    $tmp34 = ATSPMVllazyval_eval($env2);
    // ATScaseofseq_beg
    do {
      // ATSbranchseq_beg
      __atstmplab10:
      if(ATSCKptriscons($tmp34)) goto __atstmplab13;
      __atstmplab11:
      $tmp37 = auxend_8($env1);
      $tmpret33 = array(false, $tmp37);
      break;
      // ATSbranchseq_end
      // ATSbranchseq_beg
      __atstmplab12:
      __atstmplab13:
      $tmp35 = $tmp34[0];
      $tmp36 = $tmp34[1];
      // ATSINSfreecon($tmp34);
      $tmp38 = ats2phppre_compare_string_string($env0, $tmp35);
      $tmp39 = ats2phppre_gt_int1_int1($tmp38, 0);
      if($tmp39) {
        $tmp40 = aux10_7($env0, $env1, $tmp36);
        $tmpret33 = ATSPMVllazyval_eval($tmp40);
      } else {
        $tmp41 = ats2phppre_lt_int1_int1($tmp38, 0);
        if($tmp41) {
          $tmp42 = aux01_6($tmp35, $env1, $tmp36);
          $tmpret33 = array(false, $tmp42);
        } else {
          $tmp43 = aux01_6($tmp35, $env1, $tmp36);
          $tmpret33 = array(true, $tmp43);
        } // endif
      } // endif
      break;
      // ATSbranchseq_end
    } while(0);
    // ATScaseofseq_end
  } else {
    atspre_lazy_vt_free($env2);
  } // endif
  return $tmpret33;
} // end-of-function


function
__patsfun_12($env0, $arg0)
{
//
  $tmpret46 = NULL;
  $tmp48 = NULL;
  $tmp49 = NULL;
//
  __patsflab___patsfun_12:
  if($arg0) {
    // ATScaseofseq_beg
    do {
      // ATSbranchseq_beg
      __atstmplab14:
      if(ATSCKptriscons($env0)) goto __atstmplab17;
      __atstmplab15:
      $tmpret46 = NULL;
      break;
      // ATSbranchseq_end
      // ATSbranchseq_beg
      __atstmplab16:
      __atstmplab17:
      $tmp48 = $env0[1];
      $tmp49 = auxend_8($tmp48);
      $tmpret46 = array(false, $tmp49);
      break;
      // ATSbranchseq_end
    } while(0);
    // ATScaseofseq_end
  } else {
  } // endif
  return $tmpret46;
} // end-of-function

/* ****** ****** */

/* end-of-compilation-unit */
?>
