<?php

/* @WebProfiler/Collector/exception.html.twig */
class __TwigTemplate_a4a6e37587f790fa77bff5af918fc4d22299769037b1fff8663ac23544938d88 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        // line 1
        $this->parent = $this->loadTemplate("@WebProfiler/Profiler/layout.html.twig", "@WebProfiler/Collector/exception.html.twig", 1);
        $this->blocks = array(
            'head' => array($this, 'block_head'),
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
        $__internal_03e89779d0fb5a2ed68d05d2a493f84ca98c38c22ca643f92c5f11def387b19a = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_03e89779d0fb5a2ed68d05d2a493f84ca98c38c22ca643f92c5f11def387b19a->enter($__internal_03e89779d0fb5a2ed68d05d2a493f84ca98c38c22ca643f92c5f11def387b19a_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/exception.html.twig"));

        $__internal_97056309568f9fa1fedbbcfcc1fbc4801e85d007f2b734182f6370226af04929 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_97056309568f9fa1fedbbcfcc1fbc4801e85d007f2b734182f6370226af04929->enter($__internal_97056309568f9fa1fedbbcfcc1fbc4801e85d007f2b734182f6370226af04929_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@WebProfiler/Collector/exception.html.twig"));

        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_03e89779d0fb5a2ed68d05d2a493f84ca98c38c22ca643f92c5f11def387b19a->leave($__internal_03e89779d0fb5a2ed68d05d2a493f84ca98c38c22ca643f92c5f11def387b19a_prof);

        
        $__internal_97056309568f9fa1fedbbcfcc1fbc4801e85d007f2b734182f6370226af04929->leave($__internal_97056309568f9fa1fedbbcfcc1fbc4801e85d007f2b734182f6370226af04929_prof);

    }

    // line 3
    public function block_head($context, array $blocks = array())
    {
        $__internal_dd706a16f65698f4ea434ab52376b79b02cf900a05414ea275679077fa352b58 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_dd706a16f65698f4ea434ab52376b79b02cf900a05414ea275679077fa352b58->enter($__internal_dd706a16f65698f4ea434ab52376b79b02cf900a05414ea275679077fa352b58_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        $__internal_aaf1fe23555225a6eadc3e49b6ae28a648d999d0e11eb72d4b188fe1516af40e = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_aaf1fe23555225a6eadc3e49b6ae28a648d999d0e11eb72d4b188fe1516af40e->enter($__internal_aaf1fe23555225a6eadc3e49b6ae28a648d999d0e11eb72d4b188fe1516af40e_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        // line 4
        echo "    ";
        if (twig_get_attribute($this->env, $this->getSourceContext(), (isset($context["collector"]) || array_key_exists("collector", $context) ? $context["collector"] : (function () { throw new Twig_Error_Runtime('Variable "collector" does not exist.', 4, $this->getSourceContext()); })()), "hasexception", array())) {
            // line 5
            echo "        <style>
            ";
            // line 6
            echo $this->env->getRuntime('Symfony\Bridge\Twig\Extension\HttpKernelRuntime')->renderFragment($this->env->getExtension('Symfony\Bridge\Twig\Extension\RoutingExtension')->getPath("_profiler_exception_css", array("token" => (isset($context["token"]) || array_key_exists("token", $context) ? $context["token"] : (function () { throw new Twig_Error_Runtime('Variable "token" does not exist.', 6, $this->getSourceContext()); })()))));
            echo "
        </style>
    ";
        }
        // line 9
        echo "    ";
        $this->displayParentBlock("head", $context, $blocks);
        echo "
";
        
        $__internal_aaf1fe23555225a6eadc3e49b6ae28a648d999d0e11eb72d4b188fe1516af40e->leave($__internal_aaf1fe23555225a6eadc3e49b6ae28a648d999d0e11eb72d4b188fe1516af40e_prof);

        
        $__internal_dd706a16f65698f4ea434ab52376b79b02cf900a05414ea275679077fa352b58->leave($__internal_dd706a16f65698f4ea434ab52376b79b02cf900a05414ea275679077fa352b58_prof);

    }

    // line 12
    public function block_menu($context, array $blocks = array())
    {
        $__internal_e7f905794a5417bfe9ad99f202a57fe749824ae6687fb9eae62744c6bddd9e93 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_e7f905794a5417bfe9ad99f202a57fe749824ae6687fb9eae62744c6bddd9e93->enter($__internal_e7f905794a5417bfe9ad99f202a57fe749824ae6687fb9eae62744c6bddd9e93_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "menu"));

        $__internal_062c9a1353ee601aa0189b897248b27abf127a802be9ab54bf7345025b2bf69e = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_062c9a1353ee601aa0189b897248b27abf127a802be9ab54bf7345025b2bf69e->enter($__internal_062c9a1353ee601aa0189b897248b27abf127a802be9ab54bf7345025b2bf69e_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "menu"));

        // line 13
        echo "    <span class=\"label ";
        echo ((twig_get_attribute($this->env, $this->getSourceContext(), (isset($context["collector"]) || array_key_exists("collector", $context) ? $context["collector"] : (function () { throw new Twig_Error_Runtime('Variable "collector" does not exist.', 13, $this->getSourceContext()); })()), "hasexception", array())) ? ("label-status-error") : ("disabled"));
        echo "\">
        <span class=\"icon\">";
        // line 14
        echo twig_include($this->env, $context, "@WebProfiler/Icon/exception.svg");
        echo "</span>
        <strong>Exception</strong>
        ";
        // line 16
        if (twig_get_attribute($this->env, $this->getSourceContext(), (isset($context["collector"]) || array_key_exists("collector", $context) ? $context["collector"] : (function () { throw new Twig_Error_Runtime('Variable "collector" does not exist.', 16, $this->getSourceContext()); })()), "hasexception", array())) {
            // line 17
            echo "            <span class=\"count\">
                <span>1</span>
            </span>
        ";
        }
        // line 21
        echo "    </span>
";
        
        $__internal_062c9a1353ee601aa0189b897248b27abf127a802be9ab54bf7345025b2bf69e->leave($__internal_062c9a1353ee601aa0189b897248b27abf127a802be9ab54bf7345025b2bf69e_prof);

        
        $__internal_e7f905794a5417bfe9ad99f202a57fe749824ae6687fb9eae62744c6bddd9e93->leave($__internal_e7f905794a5417bfe9ad99f202a57fe749824ae6687fb9eae62744c6bddd9e93_prof);

    }

    // line 24
    public function block_panel($context, array $blocks = array())
    {
        $__internal_68104134a9d426b931041f6c58f765325efe2528966ce2260047c3f9a6f0e1d9 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_68104134a9d426b931041f6c58f765325efe2528966ce2260047c3f9a6f0e1d9->enter($__internal_68104134a9d426b931041f6c58f765325efe2528966ce2260047c3f9a6f0e1d9_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "panel"));

        $__internal_a29fc668651f62dcd0acefbd3015f964f6055636b529b4313a7c63e496bc7a83 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_a29fc668651f62dcd0acefbd3015f964f6055636b529b4313a7c63e496bc7a83->enter($__internal_a29fc668651f62dcd0acefbd3015f964f6055636b529b4313a7c63e496bc7a83_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "panel"));

        // line 25
        echo "    <h2>Exceptions</h2>

    ";
        // line 27
        if ( !twig_get_attribute($this->env, $this->getSourceContext(), (isset($context["collector"]) || array_key_exists("collector", $context) ? $context["collector"] : (function () { throw new Twig_Error_Runtime('Variable "collector" does not exist.', 27, $this->getSourceContext()); })()), "hasexception", array())) {
            // line 28
            echo "        <div class=\"empty\">
            <p>No exception was thrown and caught during the request.</p>
        </div>
    ";
        } else {
            // line 32
            echo "        <div class=\"sf-reset\">
            ";
            // line 33
            echo $this->env->getRuntime('Symfony\Bridge\Twig\Extension\HttpKernelRuntime')->renderFragment($this->env->getExtension('Symfony\Bridge\Twig\Extension\RoutingExtension')->getPath("_profiler_exception", array("token" => (isset($context["token"]) || array_key_exists("token", $context) ? $context["token"] : (function () { throw new Twig_Error_Runtime('Variable "token" does not exist.', 33, $this->getSourceContext()); })()))));
            echo "
        </div>
    ";
        }
        
        $__internal_a29fc668651f62dcd0acefbd3015f964f6055636b529b4313a7c63e496bc7a83->leave($__internal_a29fc668651f62dcd0acefbd3015f964f6055636b529b4313a7c63e496bc7a83_prof);

        
        $__internal_68104134a9d426b931041f6c58f765325efe2528966ce2260047c3f9a6f0e1d9->leave($__internal_68104134a9d426b931041f6c58f765325efe2528966ce2260047c3f9a6f0e1d9_prof);

    }

    public function getTemplateName()
    {
        return "@WebProfiler/Collector/exception.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  138 => 33,  135 => 32,  129 => 28,  127 => 27,  123 => 25,  114 => 24,  103 => 21,  97 => 17,  95 => 16,  90 => 14,  85 => 13,  76 => 12,  63 => 9,  57 => 6,  54 => 5,  51 => 4,  42 => 3,  11 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("{% extends '@WebProfiler/Profiler/layout.html.twig' %}

{% block head %}
    {% if collector.hasexception %}
        <style>
            {{ render(path('_profiler_exception_css', { token: token })) }}
        </style>
    {% endif %}
    {{ parent() }}
{% endblock %}

{% block menu %}
    <span class=\"label {{ collector.hasexception ? 'label-status-error' : 'disabled' }}\">
        <span class=\"icon\">{{ include('@WebProfiler/Icon/exception.svg') }}</span>
        <strong>Exception</strong>
        {% if collector.hasexception %}
            <span class=\"count\">
                <span>1</span>
            </span>
        {% endif %}
    </span>
{% endblock %}

{% block panel %}
    <h2>Exceptions</h2>

    {% if not collector.hasexception %}
        <div class=\"empty\">
            <p>No exception was thrown and caught during the request.</p>
        </div>
    {% else %}
        <div class=\"sf-reset\">
            {{ render(path('_profiler_exception', { token: token })) }}
        </div>
    {% endif %}
{% endblock %}
", "@WebProfiler/Collector/exception.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/exception.html.twig");
    }
}
