<?php

/* @WebProfiler/Profiler/header.html.twig */
class __TwigTemplate_8f1975f35d87036b4117eb35d1de407e0cfe7965c20985fd4165471d1e42fc3e extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_9a8958ed806d544d902dccc58c5385e9a5b605d4348868ee4d05e991c6231ed7 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_9a8958ed806d544d902dccc58c5385e9a5b605d4348868ee4d05e991c6231ed7->enter($__internal_9a8958ed806d544d902dccc58c5385e9a5b605d4348868ee4d05e991c6231ed7_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Profiler/header.html.twig"));

        $__internal_62f4ed02d3969e7d83cef7a377999fe9c24cdb8078f27f1ce061ed86103f8613 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_62f4ed02d3969e7d83cef7a377999fe9c24cdb8078f27f1ce061ed86103f8613->enter($__internal_62f4ed02d3969e7d83cef7a377999fe9c24cdb8078f27f1ce061ed86103f8613_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Profiler/header.html.twig"));

        // line 1
        echo "<div id=\"header\">
    <div class=\"container\">
        <h1>";
        // line 3
        echo twig_include($this->env, $context, "@WebProfiler/Icon/symfony.svg");
        echo " Symfony <span>Profiler</span></h1>

        <div class=\"search\">
            <form method=\"get\" action=\"https://symfony.com/search\" target=\"_blank\">
                <div class=\"form-row\">
                    <input name=\"q\" id=\"search-id\" type=\"search\" placeholder=\"search on symfony.com\">
                    <button type=\"submit\" class=\"btn\">Search</button>
                </div>
           </form>
        </div>
    </div>
</div>
";
        
        $__internal_9a8958ed806d544d902dccc58c5385e9a5b605d4348868ee4d05e991c6231ed7->leave($__internal_9a8958ed806d544d902dccc58c5385e9a5b605d4348868ee4d05e991c6231ed7_prof);

        
        $__internal_62f4ed02d3969e7d83cef7a377999fe9c24cdb8078f27f1ce061ed86103f8613->leave($__internal_62f4ed02d3969e7d83cef7a377999fe9c24cdb8078f27f1ce061ed86103f8613_prof);

    }

    public function getTemplateName()
    {
        return "@WebProfiler/Profiler/header.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  29 => 3,  25 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("<div id=\"header\">
    <div class=\"container\">
        <h1>{{ include('@WebProfiler/Icon/symfony.svg') }} Symfony <span>Profiler</span></h1>

        <div class=\"search\">
            <form method=\"get\" action=\"https://symfony.com/search\" target=\"_blank\">
                <div class=\"form-row\">
                    <input name=\"q\" id=\"search-id\" type=\"search\" placeholder=\"search on symfony.com\">
                    <button type=\"submit\" class=\"btn\">Search</button>
                </div>
           </form>
        </div>
    </div>
</div>
", "@WebProfiler/Profiler/header.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/symfony-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/WebProfilerBundle/Resources/views/Profiler/header.html.twig");
    }
}
