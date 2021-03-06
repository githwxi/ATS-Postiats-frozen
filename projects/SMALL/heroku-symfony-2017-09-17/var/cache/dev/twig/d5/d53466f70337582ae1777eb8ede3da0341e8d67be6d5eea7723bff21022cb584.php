<?php

/* @Twig/layout.html.twig */
class __TwigTemplate_088e3193ef70bb6bafbdb5b67faf1b58e27d448c89ca0ff9004d8adcb50a3518 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
            'title' => array($this, 'block_title'),
            'head' => array($this, 'block_head'),
            'body' => array($this, 'block_body'),
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $__internal_5258ef995b885af93066415414587bd9209ee3ebca35a5babf25e4adaa2a10e4 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_5258ef995b885af93066415414587bd9209ee3ebca35a5babf25e4adaa2a10e4->enter($__internal_5258ef995b885af93066415414587bd9209ee3ebca35a5babf25e4adaa2a10e4_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@Twig/layout.html.twig"));

        $__internal_a64cbc933c43935a4af9592402e895b50ed4c6b444b9022c3979b0bb4dabb54b = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_a64cbc933c43935a4af9592402e895b50ed4c6b444b9022c3979b0bb4dabb54b->enter($__internal_a64cbc933c43935a4af9592402e895b50ed4c6b444b9022c3979b0bb4dabb54b_prof = new Twig_Profiler_Profile($this->getTemplateName(), "template", "@Twig/layout.html.twig"));

        // line 1
        echo "<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"";
        // line 4
        echo twig_escape_filter($this->env, $this->env->getCharset(), "html", null, true);
        echo "\" />
        <meta name=\"robots\" content=\"noindex,nofollow\" />
        <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
        <title>";
        // line 7
        $this->displayBlock('title', $context, $blocks);
        echo "</title>
        <link rel=\"icon\" type=\"image/png\" href=\"";
        // line 8
        echo twig_include($this->env, $context, "@Twig/images/favicon.png.base64");
        echo "\">
        <style>";
        // line 9
        echo twig_include($this->env, $context, "@Twig/exception.css.twig");
        echo "</style>
        ";
        // line 10
        $this->displayBlock('head', $context, $blocks);
        // line 11
        echo "    </head>
    <body>
        <header>
            <div class=\"container\">
                <h1 class=\"logo\">";
        // line 15
        echo twig_include($this->env, $context, "@Twig/images/symfony-logo.svg");
        echo " Symfony Exception</h1>

                <div class=\"help-link\">
                    <a href=\"https://symfony.com/doc\">
                        <span class=\"icon\">";
        // line 19
        echo twig_include($this->env, $context, "@Twig/images/icon-book.svg");
        echo "</span>
                        <span class=\"hidden-xs-down\">Symfony</span> Docs
                    </a>
                </div>

                <div class=\"help-link\">
                    <a href=\"https://symfony.com/support\">
                        <span class=\"icon\">";
        // line 26
        echo twig_include($this->env, $context, "@Twig/images/icon-support.svg");
        echo "</span>
                        <span class=\"hidden-xs-down\">Symfony</span> Support
                    </a>
                </div>
            </div>
        </header>

        ";
        // line 33
        $this->displayBlock('body', $context, $blocks);
        // line 34
        echo "        ";
        echo twig_include($this->env, $context, "@Twig/base_js.html.twig");
        echo "
    </body>
</html>
";
        
        $__internal_5258ef995b885af93066415414587bd9209ee3ebca35a5babf25e4adaa2a10e4->leave($__internal_5258ef995b885af93066415414587bd9209ee3ebca35a5babf25e4adaa2a10e4_prof);

        
        $__internal_a64cbc933c43935a4af9592402e895b50ed4c6b444b9022c3979b0bb4dabb54b->leave($__internal_a64cbc933c43935a4af9592402e895b50ed4c6b444b9022c3979b0bb4dabb54b_prof);

    }

    // line 7
    public function block_title($context, array $blocks = array())
    {
        $__internal_f2979f0e649b60678d9bb2bed59d0cb01a0707f9e45eb729e9fe7234bdc0d8d7 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_f2979f0e649b60678d9bb2bed59d0cb01a0707f9e45eb729e9fe7234bdc0d8d7->enter($__internal_f2979f0e649b60678d9bb2bed59d0cb01a0707f9e45eb729e9fe7234bdc0d8d7_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        $__internal_f1180904bec2a18237639f628e97bb0ba9212215753f1822135f61d7d5614a97 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_f1180904bec2a18237639f628e97bb0ba9212215753f1822135f61d7d5614a97->enter($__internal_f1180904bec2a18237639f628e97bb0ba9212215753f1822135f61d7d5614a97_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "title"));

        
        $__internal_f1180904bec2a18237639f628e97bb0ba9212215753f1822135f61d7d5614a97->leave($__internal_f1180904bec2a18237639f628e97bb0ba9212215753f1822135f61d7d5614a97_prof);

        
        $__internal_f2979f0e649b60678d9bb2bed59d0cb01a0707f9e45eb729e9fe7234bdc0d8d7->leave($__internal_f2979f0e649b60678d9bb2bed59d0cb01a0707f9e45eb729e9fe7234bdc0d8d7_prof);

    }

    // line 10
    public function block_head($context, array $blocks = array())
    {
        $__internal_39a71f8e49c91d465410a158e8b5b7f0cdec6d903da34f73d50280400602189f = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_39a71f8e49c91d465410a158e8b5b7f0cdec6d903da34f73d50280400602189f->enter($__internal_39a71f8e49c91d465410a158e8b5b7f0cdec6d903da34f73d50280400602189f_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        $__internal_2a3e8727472afb6523b2e4dc31131431335c00146f561315802ebee80cf1fda5 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_2a3e8727472afb6523b2e4dc31131431335c00146f561315802ebee80cf1fda5->enter($__internal_2a3e8727472afb6523b2e4dc31131431335c00146f561315802ebee80cf1fda5_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "head"));

        
        $__internal_2a3e8727472afb6523b2e4dc31131431335c00146f561315802ebee80cf1fda5->leave($__internal_2a3e8727472afb6523b2e4dc31131431335c00146f561315802ebee80cf1fda5_prof);

        
        $__internal_39a71f8e49c91d465410a158e8b5b7f0cdec6d903da34f73d50280400602189f->leave($__internal_39a71f8e49c91d465410a158e8b5b7f0cdec6d903da34f73d50280400602189f_prof);

    }

    // line 33
    public function block_body($context, array $blocks = array())
    {
        $__internal_30cea208a8513c19e3067ca39c3f7b7c1574bae9a1add0980b7b02dc246857e3 = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_30cea208a8513c19e3067ca39c3f7b7c1574bae9a1add0980b7b02dc246857e3->enter($__internal_30cea208a8513c19e3067ca39c3f7b7c1574bae9a1add0980b7b02dc246857e3_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        $__internal_d04cf9600f449a903934323c8a75de4bb7a38da963518698ebc7e87aa2b28a54 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_d04cf9600f449a903934323c8a75de4bb7a38da963518698ebc7e87aa2b28a54->enter($__internal_d04cf9600f449a903934323c8a75de4bb7a38da963518698ebc7e87aa2b28a54_prof = new Twig_Profiler_Profile($this->getTemplateName(), "block", "body"));

        
        $__internal_d04cf9600f449a903934323c8a75de4bb7a38da963518698ebc7e87aa2b28a54->leave($__internal_d04cf9600f449a903934323c8a75de4bb7a38da963518698ebc7e87aa2b28a54_prof);

        
        $__internal_30cea208a8513c19e3067ca39c3f7b7c1574bae9a1add0980b7b02dc246857e3->leave($__internal_30cea208a8513c19e3067ca39c3f7b7c1574bae9a1add0980b7b02dc246857e3_prof);

    }

    public function getTemplateName()
    {
        return "@Twig/layout.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  137 => 33,  120 => 10,  103 => 7,  88 => 34,  86 => 33,  76 => 26,  66 => 19,  59 => 15,  53 => 11,  51 => 10,  47 => 9,  43 => 8,  39 => 7,  33 => 4,  28 => 1,);
    }

    public function getSourceContext()
    {
        return new Twig_Source("<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"{{ _charset }}\" />
        <meta name=\"robots\" content=\"noindex,nofollow\" />
        <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
        <title>{% block title %}{% endblock %}</title>
        <link rel=\"icon\" type=\"image/png\" href=\"{{ include('@Twig/images/favicon.png.base64') }}\">
        <style>{{ include('@Twig/exception.css.twig') }}</style>
        {% block head %}{% endblock %}
    </head>
    <body>
        <header>
            <div class=\"container\">
                <h1 class=\"logo\">{{ include('@Twig/images/symfony-logo.svg') }} Symfony Exception</h1>

                <div class=\"help-link\">
                    <a href=\"https://symfony.com/doc\">
                        <span class=\"icon\">{{ include('@Twig/images/icon-book.svg') }}</span>
                        <span class=\"hidden-xs-down\">Symfony</span> Docs
                    </a>
                </div>

                <div class=\"help-link\">
                    <a href=\"https://symfony.com/support\">
                        <span class=\"icon\">{{ include('@Twig/images/icon-support.svg') }}</span>
                        <span class=\"hidden-xs-down\">Symfony</span> Support
                    </a>
                </div>
            </div>
        </header>

        {% block body %}{% endblock %}
        {{ include('@Twig/base_js.html.twig') }}
    </body>
</html>
", "@Twig/layout.html.twig", "/home/hwxi/Research/ATS-Tutoriats/BUCS320/webpages/cs320-2017-fall/vendor/symfony/symfony/src/Symfony/Bundle/TwigBundle/Resources/views/layout.html.twig");
    }
}
