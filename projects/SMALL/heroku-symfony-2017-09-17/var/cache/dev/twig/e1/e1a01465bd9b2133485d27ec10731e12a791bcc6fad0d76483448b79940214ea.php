<?php

/* @Twig/Exception/exception_full.html.twig */
class __TwigTemplate_b9d1b17705ac9e4847598e11da598c5bc6bfce97b7e4a4d98c2cf4c2d18c8b40 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        // line 1
        $this->parent = $this->loadTemplate("@Twig/layout.html.twig", "@Twig/Exception/exception_full.html.twig", 1);
        $this->blocks = array(
            'head' => array($this, 'block_head'),
            'title' => array($this, 'block_title'),
            'body' => array($this, 'block_body'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "@Twig/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_3c52fe0b488d1ac7cb80098d0aa76ef7f5853b49b4ad2c3ddbeebba4ae8dd4ec = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_3c52fe0b488d1ac7cb80098d0aa76ef7f5853b49b4ad2c3ddbeebba4ae8dd4ec->enter($__internal_3c52fe0b488d1ac7cb80098d0aa76ef7f5853b49b4ad2c3ddbeebba4ae8dd4ec_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@Twig/Exception/exception_full.html.twig"));

        $__internal_3c7b484c9f694dc4753d88afc8667d009486f4f3923ec7d333fc9bb589f5e055 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_3c7b484c9f694dc4753d88afc8667d009486f4f3923ec7d333fc9bb589f5e055->enter($__internal_3c7b484c9f694dc4753d88afc8667d009486f4f3923ec7d333fc9bb589f5e055_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@Twig/Exception/exception_full.html.twig"));

        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_3c52fe0b488d1ac7cb80098d0aa76ef7f5853b49b4ad2c3ddbeebba4ae8dd4ec->leave($__internal_3c52fe0b488d1ac7cb80098d0aa76ef7f5853b49b4ad2c3ddbeebba4ae8dd4ec_prof);

        
        $__internal_3c7b484c9f694dc4753d88afc8667d009486f4f3923ec7d333fc9bb589f5e055->leave($__internal_3c7b484c9f694dc4753d88afc8667d009486f4f3923ec7d333fc9bb589f5e055_prof);

    }

    // line 3
    public function block_head($context, array $blocks = array())
    {
        $__internal_cc1e9dd7073483c2ba7ea1bb2f0d3b4c3f8e0471944f85f7341c40745e54ac3f = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_cc1e9dd7073483c2ba7ea1bb2f0d3b4c3f8e0471944f85f7341c40745e54ac3f->enter($__internal_cc1e9dd7073483c2ba7ea1bb2f0d3b4c3f8e0471944f85f7341c40745e54ac3f_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        $__internal_95879fb48dc7c35748145090b238aa79eb5f0a26ecd3d348f451995b1ea81a5f = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_95879fb48dc7c35748145090b238aa79eb5f0a26ecd3d348f451995b1ea81a5f->enter($__internal_95879fb48dc7c35748145090b238aa79eb5f0a26ecd3d348f451995b1ea81a5f_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        // line 4
        echo "    <style>
        .sf-reset .traces {
            padding-bottom: 14px;
        }
        .sf-reset .traces li {
            font-size: 12px;
            color: #868686;
            padding: 5px 4px;
            list-style-type: decimal;
            margin-left: 20px;
        }
        .sf-reset #logs .traces li.error {
            font-style: normal;
            color: #AA3333;
            background: #f9ecec;
        }
        .sf-reset #logs .traces li.warning {
            font-style: normal;
            background: #ffcc00;
        }
        /* fix for Opera not liking empty <li> */
        .sf-reset .traces li:after {
            content: \"\\00A0\";
        }
        .sf-reset .trace {
            border: 1px solid #D3D3D3;
            padding: 10px;
            overflow: auto;
            margin: 10px 0 20px;
        }
        .sf-reset .block-exception {
            -moz-border-radius: 16px;
            -webkit-border-radius: 16px;
            border-radius: 16px;
            margin-bottom: 20px;
            background-color: #f6f6f6;
            border: 1px solid #dfdfdf;
            padding: 30px 28px;
            word-wrap: break-word;
            overflow: hidden;
        }
        .sf-reset .block-exception div {
            color: #313131;
            font-size: 10px;
        }
        .sf-reset .block-exception-detected .illustration-exception,
        .sf-reset .block-exception-detected .text-exception {
            float: left;
        }
        .sf-reset .block-exception-detected .illustration-exception {
            width: 152px;
        }
        .sf-reset .block-exception-detected .text-exception {
            width: 670px;
            padding: 30px 44px 24px 46px;
            position: relative;
        }
        .sf-reset .text-exception .open-quote,
        .sf-reset .text-exception .close-quote {
            font-family: Arial, Helvetica, sans-serif;
            position: absolute;
            color: #C9C9C9;
            font-size: 8em;
        }
        .sf-reset .open-quote {
            top: 0;
            left: 0;
        }
        .sf-reset .close-quote {
            bottom: -0.5em;
            right: 50px;
        }
        .sf-reset .block-exception p {
            font-family: Arial, Helvetica, sans-serif;
        }
        .sf-reset .block-exception p a,
        .sf-reset .block-exception p a:hover {
            color: #565656;
        }
        .sf-reset .logs h2 {
            float: left;
            width: 654px;
        }
        .sf-reset .error-count, .sf-reset .support {
            float: right;
            width: 170px;
            text-align: right;
        }
        .sf-reset .error-count span {
             display: inline-block;
             background-color: #aacd4e;
             -moz-border-radius: 6px;
             -webkit-border-radius: 6px;
             border-radius: 6px;
             padding: 4px;
             color: white;
             margin-right: 2px;
             font-size: 11px;
             font-weight: bold;
        }

        .sf-reset .support a {
            display: inline-block;
            -moz-border-radius: 6px;
            -webkit-border-radius: 6px;
            border-radius: 6px;
            padding: 4px;
            color: #000000;
            margin-right: 2px;
            font-size: 11px;
            font-weight: bold;
        }

        .sf-reset .toggle {
            vertical-align: middle;
        }
        .sf-reset .linked ul,
        .sf-reset .linked li {
            display: inline;
        }
        .sf-reset #output-content {
            color: #000;
            font-size: 12px;
        }
        .sf-reset #traces-text pre {
            white-space: pre;
            font-size: 12px;
            font-family: monospace;
        }
    </style>
";
        
        $__internal_95879fb48dc7c35748145090b238aa79eb5f0a26ecd3d348f451995b1ea81a5f->leave($__internal_95879fb48dc7c35748145090b238aa79eb5f0a26ecd3d348f451995b1ea81a5f_prof);

        
        $__internal_cc1e9dd7073483c2ba7ea1bb2f0d3b4c3f8e0471944f85f7341c40745e54ac3f->leave($__internal_cc1e9dd7073483c2ba7ea1bb2f0d3b4c3f8e0471944f85f7341c40745e54ac3f_prof);

    }

    // line 136
    public function block_title($context, array $blocks = array())
    {
        $__internal_af66d1f44a2349badd764eba78068c5ce4a581eebb82c017611352e7e8bb3d0a = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_af66d1f44a2349badd764eba78068c5ce4a581eebb82c017611352e7e8bb3d0a->enter($__internal_af66d1f44a2349badd764eba78068c5ce4a581eebb82c017611352e7e8bb3d0a_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        $__internal_fed66ab75a9d2e43aa08b5388889cd645c9a2293f557d1d3c5c90290cb81b6d0 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_fed66ab75a9d2e43aa08b5388889cd645c9a2293f557d1d3c5c90290cb81b6d0->enter($__internal_fed66ab75a9d2e43aa08b5388889cd645c9a2293f557d1d3c5c90290cb81b6d0_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        // line 137
        echo "    ";
        echo twig_escape_filter($this->env, twig_get_attribute($this->env, $this->getSourceContext(), (isset($context["exception"]) || array_key_exists("exception", $context) ? $context["exception"] : (function () { throw new Twig_Error_Runtime('Variable "exception" does not exist.', 137, $this->getSourceContext()); })()), "message", array()), "html", null, true);
        echo " (";
        echo twig_escape_filter($this->env, (isset($context["status_code"]) || array_key_exists("status_code", $context) ? $context["status_code"] : (function () { throw new Twig_Error_Runtime('Variable "status_code" does not exist.', 137, $this->getSourceContext()); })()), "html", null, true);
        echo " ";
        echo twig_escape_filter($this->env, (isset($context["status_text"]) || array_key_exists("status_text", $context) ? $context["status_text"] : (function () { throw new Twig_Error_Runtime('Variable "status_text" does not exist.', 137, $this->getSourceContext()); })()), "html", null, true);
        echo ")
";
        
        $__internal_fed66ab75a9d2e43aa08b5388889cd645c9a2293f557d1d3c5c90290cb81b6d0->leave($__internal_fed66ab75a9d2e43aa08b5388889cd645c9a2293f557d1d3c5c90290cb81b6d0_prof);

        
        $__internal_af66d1f44a2349badd764eba78068c5ce4a581eebb82c017611352e7e8bb3d0a->leave($__internal_af66d1f44a2349badd764eba78068c5ce4a581eebb82c017611352e7e8bb3d0a_prof);

    }

    // line 140
    public function block_body($context, array $blocks = array())
    {
        $__internal_fa5a63e20e2719652e2c62b2abfb6d237eef018e6efbae02a41e580e8eca3689 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_fa5a63e20e2719652e2c62b2abfb6d237eef018e6efbae02a41e580e8eca3689->enter($__internal_fa5a63e20e2719652e2c62b2abfb6d237eef018e6efbae02a41e580e8eca3689_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        $__internal_41b0c34c58a490883cfc963c8add7b7768e6b05cd8713b80dc9ee05b9c6a586c = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_41b0c34c58a490883cfc963c8add7b7768e6b05cd8713b80dc9ee05b9c6a586c->enter($__internal_41b0c34c58a490883cfc963c8add7b7768e6b05cd8713b80dc9ee05b9c6a586c_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        // line 141
        echo "    ";
        $this->loadTemplate("@Twig/Exception/exception.html.twig", "@Twig/Exception/exception_full.html.twig", 141)->display($context);
        
        $__internal_41b0c34c58a490883cfc963c8add7b7768e6b05cd8713b80dc9ee05b9c6a586c->leave($__internal_41b0c34c58a490883cfc963c8add7b7768e6b05cd8713b80dc9ee05b9c6a586c_prof);

        
        $__internal_fa5a63e20e2719652e2c62b2abfb6d237eef018e6efbae02a41e580e8eca3689->leave($__internal_fa5a63e20e2719652e2c62b2abfb6d237eef018e6efbae02a41e580e8eca3689_prof);

    }

    public function getTemplateName()
    {
        return "@Twig/Exception/exception_full.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  226 => 141,  217 => 140,  200 => 137,  191 => 136,  51 => 4,  42 => 3,  11 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("{% extends '@Twig/layout.html.twig' %}

{% block head %}
    <style>
        .sf-reset .traces {
            padding-bottom: 14px;
        }
        .sf-reset .traces li {
            font-size: 12px;
            color: #868686;
            padding: 5px 4px;
            list-style-type: decimal;
            margin-left: 20px;
        }
        .sf-reset #logs .traces li.error {
            font-style: normal;
            color: #AA3333;
            background: #f9ecec;
        }
        .sf-reset #logs .traces li.warning {
            font-style: normal;
            background: #ffcc00;
        }
        /* fix for Opera not liking empty <li> */
        .sf-reset .traces li:after {
            content: \"\\00A0\";
        }
        .sf-reset .trace {
            border: 1px solid #D3D3D3;
            padding: 10px;
            overflow: auto;
            margin: 10px 0 20px;
        }
        .sf-reset .block-exception {
            -moz-border-radius: 16px;
            -webkit-border-radius: 16px;
            border-radius: 16px;
            margin-bottom: 20px;
            background-color: #f6f6f6;
            border: 1px solid #dfdfdf;
            padding: 30px 28px;
            word-wrap: break-word;
            overflow: hidden;
        }
        .sf-reset .block-exception div {
            color: #313131;
            font-size: 10px;
        }
        .sf-reset .block-exception-detected .illustration-exception,
        .sf-reset .block-exception-detected .text-exception {
            float: left;
        }
        .sf-reset .block-exception-detected .illustration-exception {
            width: 152px;
        }
        .sf-reset .block-exception-detected .text-exception {
            width: 670px;
            padding: 30px 44px 24px 46px;
            position: relative;
        }
        .sf-reset .text-exception .open-quote,
        .sf-reset .text-exception .close-quote {
            font-family: Arial, Helvetica, sans-serif;
            position: absolute;
            color: #C9C9C9;
            font-size: 8em;
        }
        .sf-reset .open-quote {
            top: 0;
            left: 0;
        }
        .sf-reset .close-quote {
            bottom: -0.5em;
            right: 50px;
        }
        .sf-reset .block-exception p {
            font-family: Arial, Helvetica, sans-serif;
        }
        .sf-reset .block-exception p a,
        .sf-reset .block-exception p a:hover {
            color: #565656;
        }
        .sf-reset .logs h2 {
            float: left;
            width: 654px;
        }
        .sf-reset .error-count, .sf-reset .support {
            float: right;
            width: 170px;
            text-align: right;
        }
        .sf-reset .error-count span {
             display: inline-block;
             background-color: #aacd4e;
             -moz-border-radius: 6px;
             -webkit-border-radius: 6px;
             border-radius: 6px;
             padding: 4px;
             color: white;
             margin-right: 2px;
             font-size: 11px;
             font-weight: bold;
        }

        .sf-reset .support a {
            display: inline-block;
            -moz-border-radius: 6px;
            -webkit-border-radius: 6px;
            border-radius: 6px;
            padding: 4px;
            color: #000000;
            margin-right: 2px;
            font-size: 11px;
            font-weight: bold;
        }

        .sf-reset .toggle {
            vertical-align: middle;
        }
        .sf-reset .linked ul,
        .sf-reset .linked li {
            display: inline;
        }
        .sf-reset #output-content {
            color: #000;
            font-size: 12px;
        }
        .sf-reset #traces-text pre {
            white-space: pre;
            font-size: 12px;
            font-family: monospace;
        }
    </style>
{% endblock %}

{% block title %}
    {{ exception.message }} ({{ status_code }} {{ status_text }})
{% endblock %}

{% block body %}
    {% include '@Twig/Exception/exception.html.twig' %}
{% endblock %}
", "@Twig/Exception/exception_full.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/TwigBundle/Resources/views/Exception/exception_full.html.twig");
    }
}
