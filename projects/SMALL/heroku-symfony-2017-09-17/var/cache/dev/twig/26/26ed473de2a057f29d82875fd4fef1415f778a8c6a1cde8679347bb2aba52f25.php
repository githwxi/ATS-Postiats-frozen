<?php

/* @WebProfiler/Collector/ajax.html.twig */
class __TwigTemplate_31ff3c1b2e2edcaf99b2a303b9b612911cca62687dbefadf32b382450409afd7 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        // line 1
        $this->parent = $this->loadTemplate("@WebProfiler/Profiler/layout.html.twig", "@WebProfiler/Collector/ajax.html.twig", 1);
        $this->blocks = array(
            'toolbar' => array($this, 'block_toolbar'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "@WebProfiler/Profiler/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_fa3ff0fc51e4aa443f397922bd25daa2eaa865e294fbcfcfdeef2776d7265917 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_fa3ff0fc51e4aa443f397922bd25daa2eaa865e294fbcfcfdeef2776d7265917->enter($__internal_fa3ff0fc51e4aa443f397922bd25daa2eaa865e294fbcfcfdeef2776d7265917_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/ajax.html.twig"));

        $__internal_701556e49851ebc0ceeb815798193f298dbeb28110ca9e5377269e1ce30cfcbf = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_701556e49851ebc0ceeb815798193f298dbeb28110ca9e5377269e1ce30cfcbf->enter($__internal_701556e49851ebc0ceeb815798193f298dbeb28110ca9e5377269e1ce30cfcbf_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/ajax.html.twig"));

        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_fa3ff0fc51e4aa443f397922bd25daa2eaa865e294fbcfcfdeef2776d7265917->leave($__internal_fa3ff0fc51e4aa443f397922bd25daa2eaa865e294fbcfcfdeef2776d7265917_prof);

        
        $__internal_701556e49851ebc0ceeb815798193f298dbeb28110ca9e5377269e1ce30cfcbf->leave($__internal_701556e49851ebc0ceeb815798193f298dbeb28110ca9e5377269e1ce30cfcbf_prof);

    }

    // line 3
    public function block_toolbar($context, array $blocks = array())
    {
        $__internal_d343a4f45d0d81fc142de915348a5a9ea9d63514bed8c53fb064c4e59faf931f = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_d343a4f45d0d81fc142de915348a5a9ea9d63514bed8c53fb064c4e59faf931f->enter($__internal_d343a4f45d0d81fc142de915348a5a9ea9d63514bed8c53fb064c4e59faf931f_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "toolbar"));

        $__internal_c25c54f09091eb0e13d484eae1b4dccaa754d4259150cf6674ed6956c8618ea0 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_c25c54f09091eb0e13d484eae1b4dccaa754d4259150cf6674ed6956c8618ea0->enter($__internal_c25c54f09091eb0e13d484eae1b4dccaa754d4259150cf6674ed6956c8618ea0_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "toolbar"));

        // line 4
        echo "    ";
        ob_start();
        // line 5
        echo "        ";
        echo twig_include($this->env, $context, "@WebProfiler/Icon/ajax.svg");
        echo "
        <span class=\"sf-toolbar-value sf-toolbar-ajax-request-counter\">0</span>
    ";
        $context["icon"] = ('' === $tmp = ob_get_clean()) ? '' : new Twig_Markup($tmp, $this->env->getCharset());
        // line 8
        echo "
    ";
        // line 9
        $context["text"] = ('' === $tmp = "        <div class=\"sf-toolbar-info-piece\">
            <b class=\"sf-toolbar-ajax-info\"></b>
        </div>
        <div class=\"sf-toolbar-info-piece\">
            <table class=\"sf-toolbar-ajax-requests\">
                <thead>
                    <tr>
                        <th>Method</th>
                        <th>Type</th>
                        <th>Status</th>
                        <th>URL</th>
                        <th>Time</th>
                        <th>Profile</th>
                    </tr>
                </thead>
                <tbody class=\"sf-toolbar-ajax-request-list\"></tbody>
            </table>
        </div>
    ") ? '' : new Twig_Markup($tmp, $this->env->getCharset());
        // line 29
        echo "
    ";
        // line 30
        echo twig_include($this->env, $context, "@WebProfiler/Profiler/toolbar_item.html.twig", array("link" => false));
        echo "
";
        
        $__internal_c25c54f09091eb0e13d484eae1b4dccaa754d4259150cf6674ed6956c8618ea0->leave($__internal_c25c54f09091eb0e13d484eae1b4dccaa754d4259150cf6674ed6956c8618ea0_prof);

        
        $__internal_d343a4f45d0d81fc142de915348a5a9ea9d63514bed8c53fb064c4e59faf931f->leave($__internal_d343a4f45d0d81fc142de915348a5a9ea9d63514bed8c53fb064c4e59faf931f_prof);

    }

    public function getTemplateName()
    {
        return "@WebProfiler/Collector/ajax.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  85 => 30,  82 => 29,  62 => 9,  59 => 8,  52 => 5,  49 => 4,  40 => 3,  11 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("{% extends '@WebProfiler/Profiler/layout.html.twig' %}

{% block toolbar %}
    {% set icon %}
        {{ include('@WebProfiler/Icon/ajax.svg') }}
        <span class=\"sf-toolbar-value sf-toolbar-ajax-request-counter\">0</span>
    {% endset %}

    {% set text %}
        <div class=\"sf-toolbar-info-piece\">
            <b class=\"sf-toolbar-ajax-info\"></b>
        </div>
        <div class=\"sf-toolbar-info-piece\">
            <table class=\"sf-toolbar-ajax-requests\">
                <thead>
                    <tr>
                        <th>Method</th>
                        <th>Type</th>
                        <th>Status</th>
                        <th>URL</th>
                        <th>Time</th>
                        <th>Profile</th>
                    </tr>
                </thead>
                <tbody class=\"sf-toolbar-ajax-request-list\"></tbody>
            </table>
        </div>
    {% endset %}

    {{ include('@WebProfiler/Profiler/toolbar_item.html.twig', { link: false }) }}
{% endblock %}
", "@WebProfiler/Collector/ajax.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/ajax.html.twig");
    }
}
