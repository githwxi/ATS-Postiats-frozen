<?php

/* @WebProfiler/Collector/router.html.twig */
class __TwigTemplate_b2dcc25782919c673c591183009effac821ddcbf244228cc2124c03d91ab46c8 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        // line 1
        $this->parent = $this->loadTemplate("@WebProfiler/Profiler/layout.html.twig", "@WebProfiler/Collector/router.html.twig", 1);
        $this->blocks = array(
            'toolbar' => array($this, 'block_toolbar'),
            'menu' => array($this, 'block_menu'),
            'panel' => array($this, 'block_panel'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "@WebProfiler/Profiler/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_f86390530cd0076368547d615e27eb5929eb102c023a81fb13d6d242005f8efe = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_f86390530cd0076368547d615e27eb5929eb102c023a81fb13d6d242005f8efe->enter($__internal_f86390530cd0076368547d615e27eb5929eb102c023a81fb13d6d242005f8efe_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/router.html.twig"));

        $__internal_3b7761243f321c67a08e435f58e34178f413c85d490d36003c55e1b8c4c01ca1 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_3b7761243f321c67a08e435f58e34178f413c85d490d36003c55e1b8c4c01ca1->enter($__internal_3b7761243f321c67a08e435f58e34178f413c85d490d36003c55e1b8c4c01ca1_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/router.html.twig"));

        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_f86390530cd0076368547d615e27eb5929eb102c023a81fb13d6d242005f8efe->leave($__internal_f86390530cd0076368547d615e27eb5929eb102c023a81fb13d6d242005f8efe_prof);

        
        $__internal_3b7761243f321c67a08e435f58e34178f413c85d490d36003c55e1b8c4c01ca1->leave($__internal_3b7761243f321c67a08e435f58e34178f413c85d490d36003c55e1b8c4c01ca1_prof);

    }

    // line 3
    public function block_toolbar($context, array $blocks = array())
    {
        $__internal_1b84e59266c603810a008e39a66cc2712811301e9285a0744f59d0d48737eab1 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_1b84e59266c603810a008e39a66cc2712811301e9285a0744f59d0d48737eab1->enter($__internal_1b84e59266c603810a008e39a66cc2712811301e9285a0744f59d0d48737eab1_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "toolbar"));

        $__internal_b68005799633b22c8a4366356b1bceae3bf6992fcec7d40d1fca1a925661e2e6 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_b68005799633b22c8a4366356b1bceae3bf6992fcec7d40d1fca1a925661e2e6->enter($__internal_b68005799633b22c8a4366356b1bceae3bf6992fcec7d40d1fca1a925661e2e6_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "toolbar"));

        
        $__internal_b68005799633b22c8a4366356b1bceae3bf6992fcec7d40d1fca1a925661e2e6->leave($__internal_b68005799633b22c8a4366356b1bceae3bf6992fcec7d40d1fca1a925661e2e6_prof);

        
        $__internal_1b84e59266c603810a008e39a66cc2712811301e9285a0744f59d0d48737eab1->leave($__internal_1b84e59266c603810a008e39a66cc2712811301e9285a0744f59d0d48737eab1_prof);

    }

    // line 5
    public function block_menu($context, array $blocks = array())
    {
        $__internal_405c3023b2a3f79e9407e5455924866ab828697a7b0fc10f9e28f7aef79d9a3e = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_405c3023b2a3f79e9407e5455924866ab828697a7b0fc10f9e28f7aef79d9a3e->enter($__internal_405c3023b2a3f79e9407e5455924866ab828697a7b0fc10f9e28f7aef79d9a3e_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "menu"));

        $__internal_c3187905a99af57fcc46e54df79fd76eb0a7cd773af6eb0d51da46aeee8e53e9 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_c3187905a99af57fcc46e54df79fd76eb0a7cd773af6eb0d51da46aeee8e53e9->enter($__internal_c3187905a99af57fcc46e54df79fd76eb0a7cd773af6eb0d51da46aeee8e53e9_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "menu"));

        // line 6
        echo "<span class=\"label\">
    <span class=\"icon\">";
        // line 7
        echo twig_include($this->env, $context, "@WebProfiler/Icon/router.svg");
        echo "</span>
    <strong>Routing</strong>
</span>
";
        
        $__internal_c3187905a99af57fcc46e54df79fd76eb0a7cd773af6eb0d51da46aeee8e53e9->leave($__internal_c3187905a99af57fcc46e54df79fd76eb0a7cd773af6eb0d51da46aeee8e53e9_prof);

        
        $__internal_405c3023b2a3f79e9407e5455924866ab828697a7b0fc10f9e28f7aef79d9a3e->leave($__internal_405c3023b2a3f79e9407e5455924866ab828697a7b0fc10f9e28f7aef79d9a3e_prof);

    }

    // line 12
    public function block_panel($context, array $blocks = array())
    {
        $__internal_d7fd96fd18ef5555e506dd53f4e760fa3f884e9fd510cbd51f6af8bbc6d0ed83 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_d7fd96fd18ef5555e506dd53f4e760fa3f884e9fd510cbd51f6af8bbc6d0ed83->enter($__internal_d7fd96fd18ef5555e506dd53f4e760fa3f884e9fd510cbd51f6af8bbc6d0ed83_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "panel"));

        $__internal_6a1da676881550ca0c82354f0966dde61d30a03cd5e1edea9edb88b669334b52 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_6a1da676881550ca0c82354f0966dde61d30a03cd5e1edea9edb88b669334b52->enter($__internal_6a1da676881550ca0c82354f0966dde61d30a03cd5e1edea9edb88b669334b52_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "panel"));

        // line 13
        echo "    ";
        echo $this->env->getRuntime('Symfony\Bridge\Twig\Extension\HttpKernelRuntime')->renderFragment($this->env->getExtension('Symfony\Bridge\Twig\Extension\RoutingExtension')->getPath("_profiler_router", array("token" => (isset($context["token"]) || array_key_exists("token", $context) ? $context["token"] : (function () { throw new Twig_Error_Runtime('Variable "token" does not exist.', 13, $this->getSourceContext()); })()))));
        echo "
";
        
        $__internal_6a1da676881550ca0c82354f0966dde61d30a03cd5e1edea9edb88b669334b52->leave($__internal_6a1da676881550ca0c82354f0966dde61d30a03cd5e1edea9edb88b669334b52_prof);

        
        $__internal_d7fd96fd18ef5555e506dd53f4e760fa3f884e9fd510cbd51f6af8bbc6d0ed83->leave($__internal_d7fd96fd18ef5555e506dd53f4e760fa3f884e9fd510cbd51f6af8bbc6d0ed83_prof);

    }

    public function getTemplateName()
    {
        return "@WebProfiler/Collector/router.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  94 => 13,  85 => 12,  71 => 7,  68 => 6,  59 => 5,  42 => 3,  11 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("{% extends '@WebProfiler/Profiler/layout.html.twig' %}

{% block toolbar %}{% endblock %}

{% block menu %}
<span class=\"label\">
    <span class=\"icon\">{{ include('@WebProfiler/Icon/router.svg') }}</span>
    <strong>Routing</strong>
</span>
{% endblock %}

{% block panel %}
    {{ render(path('_profiler_router', { token: token })) }}
{% endblock %}
", "@WebProfiler/Collector/router.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/router.html.twig");
    }
}
