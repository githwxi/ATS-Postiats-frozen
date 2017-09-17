<?php

/* base.html.twig */
class __TwigTemplate_33be6c8e5f7a4389dca3ebff338ccae7177f681b991500a44cfde90a719ce42a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
            'title' => array($this, 'block_title'),
            'stylesheets' => array($this, 'block_stylesheets'),
            'body' => array($this, 'block_body'),
            'javascripts' => array($this, 'block_javascripts'),
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_65576a160659ba6480b5f9f0361ee4b5f7d05c9955f5c5518fe97bcd54a6df64 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_65576a160659ba6480b5f9f0361ee4b5f7d05c9955f5c5518fe97bcd54a6df64->enter($__internal_65576a160659ba6480b5f9f0361ee4b5f7d05c9955f5c5518fe97bcd54a6df64_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "base.html.twig"));

        $__internal_479ab8aff8c1ad57a13009ef0655264633256e1cbb3c1cb87d33747c05ab91a2 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_479ab8aff8c1ad57a13009ef0655264633256e1cbb3c1cb87d33747c05ab91a2->enter($__internal_479ab8aff8c1ad57a13009ef0655264633256e1cbb3c1cb87d33747c05ab91a2_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "base.html.twig"));

        // line 1
        echo "<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"UTF-8\" />
        <title>";
        // line 5
        $this->displayBlock('title', $context, $blocks);
        echo "</title>
        ";
        // line 6
        $this->displayBlock('stylesheets', $context, $blocks);
        // line 7
        echo "        <link rel=\"icon\" type=\"image/x-icon\" href=\"";
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\AssetExtension')->getAssetUrl("favicon.ico"), "html", null, true);
        echo "\" />
    </head>
    <body>
        ";
        // line 10
        $this->displayBlock('body', $context, $blocks);
        // line 11
        echo "        ";
        $this->displayBlock('javascripts', $context, $blocks);
        // line 12
        echo "    </body>
</html>
";
        
        $__internal_65576a160659ba6480b5f9f0361ee4b5f7d05c9955f5c5518fe97bcd54a6df64->leave($__internal_65576a160659ba6480b5f9f0361ee4b5f7d05c9955f5c5518fe97bcd54a6df64_prof);

        
        $__internal_479ab8aff8c1ad57a13009ef0655264633256e1cbb3c1cb87d33747c05ab91a2->leave($__internal_479ab8aff8c1ad57a13009ef0655264633256e1cbb3c1cb87d33747c05ab91a2_prof);

    }

    // line 5
    public function block_title($context, array $blocks = array())
    {
        $__internal_47163dde55d0ceabbb37f11856660c2aa30c12ee2b720c06aa2e97da07599d1e = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_47163dde55d0ceabbb37f11856660c2aa30c12ee2b720c06aa2e97da07599d1e->enter($__internal_47163dde55d0ceabbb37f11856660c2aa30c12ee2b720c06aa2e97da07599d1e_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        $__internal_26a8397999783adc093067c68ea4eaa40c06db8daa2a930f8718049e0ba476c7 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_26a8397999783adc093067c68ea4eaa40c06db8daa2a930f8718049e0ba476c7->enter($__internal_26a8397999783adc093067c68ea4eaa40c06db8daa2a930f8718049e0ba476c7_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        echo "Welcome!";
        
        $__internal_26a8397999783adc093067c68ea4eaa40c06db8daa2a930f8718049e0ba476c7->leave($__internal_26a8397999783adc093067c68ea4eaa40c06db8daa2a930f8718049e0ba476c7_prof);

        
        $__internal_47163dde55d0ceabbb37f11856660c2aa30c12ee2b720c06aa2e97da07599d1e->leave($__internal_47163dde55d0ceabbb37f11856660c2aa30c12ee2b720c06aa2e97da07599d1e_prof);

    }

    // line 6
    public function block_stylesheets($context, array $blocks = array())
    {
        $__internal_49266a9f987c972e6c6ec9b1d1cff6e21df90372c0530324d00fafb8795d9eb4 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_49266a9f987c972e6c6ec9b1d1cff6e21df90372c0530324d00fafb8795d9eb4->enter($__internal_49266a9f987c972e6c6ec9b1d1cff6e21df90372c0530324d00fafb8795d9eb4_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "stylesheets"));

        $__internal_8707b922746f08b5258979723ab68d11ceae438ab695b31502e64c9aecdf89d1 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_8707b922746f08b5258979723ab68d11ceae438ab695b31502e64c9aecdf89d1->enter($__internal_8707b922746f08b5258979723ab68d11ceae438ab695b31502e64c9aecdf89d1_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "stylesheets"));

        
        $__internal_8707b922746f08b5258979723ab68d11ceae438ab695b31502e64c9aecdf89d1->leave($__internal_8707b922746f08b5258979723ab68d11ceae438ab695b31502e64c9aecdf89d1_prof);

        
        $__internal_49266a9f987c972e6c6ec9b1d1cff6e21df90372c0530324d00fafb8795d9eb4->leave($__internal_49266a9f987c972e6c6ec9b1d1cff6e21df90372c0530324d00fafb8795d9eb4_prof);

    }

    // line 10
    public function block_body($context, array $blocks = array())
    {
        $__internal_7b6ec7bf7b1627bc9d245f41fedbb58c15982224db0c035d617df8735e687484 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_7b6ec7bf7b1627bc9d245f41fedbb58c15982224db0c035d617df8735e687484->enter($__internal_7b6ec7bf7b1627bc9d245f41fedbb58c15982224db0c035d617df8735e687484_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        $__internal_2cd244df094c8e70b99d8301b77d9fcae5fc20a4772a923c1351dba3e08d4176 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_2cd244df094c8e70b99d8301b77d9fcae5fc20a4772a923c1351dba3e08d4176->enter($__internal_2cd244df094c8e70b99d8301b77d9fcae5fc20a4772a923c1351dba3e08d4176_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        
        $__internal_2cd244df094c8e70b99d8301b77d9fcae5fc20a4772a923c1351dba3e08d4176->leave($__internal_2cd244df094c8e70b99d8301b77d9fcae5fc20a4772a923c1351dba3e08d4176_prof);

        
        $__internal_7b6ec7bf7b1627bc9d245f41fedbb58c15982224db0c035d617df8735e687484->leave($__internal_7b6ec7bf7b1627bc9d245f41fedbb58c15982224db0c035d617df8735e687484_prof);

    }

    // line 11
    public function block_javascripts($context, array $blocks = array())
    {
        $__internal_7f3b8acba9128c72ece6c0a44b47c76615e7281f0fff39ac684fb956e502875c = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_7f3b8acba9128c72ece6c0a44b47c76615e7281f0fff39ac684fb956e502875c->enter($__internal_7f3b8acba9128c72ece6c0a44b47c76615e7281f0fff39ac684fb956e502875c_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "javascripts"));

        $__internal_f0cb41ee9c1350318979cb5d5d9a3d361e962ca6766d0e2889d9d2c4887771f4 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_f0cb41ee9c1350318979cb5d5d9a3d361e962ca6766d0e2889d9d2c4887771f4->enter($__internal_f0cb41ee9c1350318979cb5d5d9a3d361e962ca6766d0e2889d9d2c4887771f4_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "javascripts"));

        
        $__internal_f0cb41ee9c1350318979cb5d5d9a3d361e962ca6766d0e2889d9d2c4887771f4->leave($__internal_f0cb41ee9c1350318979cb5d5d9a3d361e962ca6766d0e2889d9d2c4887771f4_prof);

        
        $__internal_7f3b8acba9128c72ece6c0a44b47c76615e7281f0fff39ac684fb956e502875c->leave($__internal_7f3b8acba9128c72ece6c0a44b47c76615e7281f0fff39ac684fb956e502875c_prof);

    }

    public function getTemplateName()
    {
        return "base.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  117 => 11,  100 => 10,  83 => 6,  65 => 5,  53 => 12,  50 => 11,  48 => 10,  41 => 7,  39 => 6,  35 => 5,  29 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"UTF-8\" />
        <title>{% block title %}Welcome!{% endblock %}</title>
        {% block stylesheets %}{% endblock %}
        <link rel=\"icon\" type=\"image/x-icon\" href=\"{{ asset('favicon.ico') }}\" />
    </head>
    <body>
        {% block body %}{% endblock %}
        {% block javascripts %}{% endblock %}
    </body>
</html>
", "base.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/app/Resources/views/base.html.twig");
    }
}
