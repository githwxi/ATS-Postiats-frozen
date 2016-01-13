implement hello (out, t, xs) = 
{
val () = htmlprint_prolog (out)
val () = htmlprint_tagname (out, "html")
val () = htmlprint_chardata (out)
val () = {
  val () = htmlprint_tagname (out, "head")
  val () = htmlprint_chardata (out)
  val () = {
    val () = htmlprint_tagname (out, "title")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Hello from HTML2PATS")

    } (* end of [title] *)
    val () = htmlprint_tagend (out, "title")
    val () = htmlprint_tagname (out, "style")
    val () = htmlprint_attrib (out, "type")
    val () = htmlprint_string (out, "text/css")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "\n      .yes { color: red; }\n      .no { color: blue; }\n    ")

    } (* end of [style] *)
    val () = htmlprint_tagend (out, "style")
  } (* end of [head] *)
  val () = htmlprint_tagend (out, "head")
  val () = htmlprint_tagname (out, "body")
  val () = htmlprint_chardata (out)
  val () = {
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "h1")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Hello from HTML2PATS!")

    } (* end of [h1] *)
    val () = htmlprint_tagend (out, "h1")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "HTML2PATS is a tool for converting HTML with embedded ATS2 code into ATS2 code")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "HTML2PATS can be used as a templating engine or as a\n    preprocessor (when memory safety & runtime efficiency are\n    highly sought after). HTML2PATS can be thought of as a tool for\n    giving a nicer syntax to a class of functions for constructing\n    HTML (fragments).\n    ")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "h2")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Basic usage")

    } (* end of [h2] *)
    val () = htmlprint_tagend (out, "h2")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "ul")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_tagname (out, "li")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "Use ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "$E")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " to expand it to the\n      expression ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "E")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, ", where ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "E")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " stands for some\n      alphanumeric identifier. For instance: the value of\n      parameter ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "$t")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " evaluates\n      to ")

        val () = htmlprint_tagname (out, "strong")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_mac (out, t)

        } (* end of [strong] *)
        val () = htmlprint_tagend (out, "strong")
        val () = htmlprint_string (out, ".")

      } (* end of [li] *)
      val () = htmlprint_tagend (out, "li")
      val () = htmlprint_string (out, "\n      ")

      val () = htmlprint_tagname (out, "li")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "Use ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "${E}")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " if ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "E")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " stands for some\n      more complex expression. For instance, the\n      expression ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "${(if t=\"\" then \"yes\" else\n      \"no\"):string}")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, ", when evaluated in the context of\n      a ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "style")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " attribute, should make ")

        val () = htmlprint_tagname (out, "span")
        val () = htmlprint_attrib (out, "class")
        val () = htmlprint_mac (out, (if
      t="" then "yes" else "no"):string)
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "this text")

        } (* end of [span] *)
        val () = htmlprint_tagend (out, "span")
        val () = htmlprint_string (out, " blue.")

      } (* end of [li] *)
      val () = htmlprint_tagend (out, "li")
      val () = htmlprint_string (out, "\n      ")

      val () = htmlprint_tagname (out, "li")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "Use a backslash ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "\\")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
        val () = htmlprint_string (out, " to escape a backslash, as\n      follows: ")

        val () = htmlprint_tagname (out, "code")
        val () = htmlprint_chardata (out)
        val () = {
          val () = htmlprint_string (out, "\\\\")

        } (* end of [code] *)
        val () = htmlprint_tagend (out, "code")
      } (* end of [li] *)
      val () = htmlprint_tagend (out, "li")
      val () = htmlprint_string (out, "\n    ")

    } (* end of [ul] *)
    val () = htmlprint_tagend (out, "ul")
    val () = htmlprint_combeg (out)
    val () = htmlprint_string (out, " this is a comment, it should be left as-is ")
    val () = htmlprint_comend (out)
    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Comments will be retained as-is.")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "The length of the passed-in list is ")
      val () = htmlprint_mac (out, length(xs))
      val () = htmlprint_string (out, " (evaluated\n      using a function\n      call: ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "${length(xs)}")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, ")")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Finally, it is possible to locally implement template\nfunctions.")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "The ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "ats-call")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, " tag is used to call a template function\n      (with specified template arguments listed in tmpargs and dynamic\n      arguments listed in dynargs). Below, ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "int;HTMLprint")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, "\n  is translated to: ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "<int><HTMLprint>")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, ".")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "The ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "ats-impl")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, " tag is used for implementing a function\ntemplate locally, only visible to the\nenclosing ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "ats-call")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, ".")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "pre")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "\n      <ats-call fun=\"list_vt_foreach_env\" tmpargs=\"int;HTMLprint\" dynargs=\"xs, out\">\n\t<ats-impl tmp=\"list_vt_foreach$fwork\"\n\t\t  tmpargs=\"int;HTMLprint\" dynargs=\"x, out\">\n\t  <li>$x</li>\n\t</ats-impl>\n      </ats-call>\n    ")

    } (* end of [pre] *)
    val () = htmlprint_tagend (out, "pre")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "For instance, the result of evaluating the above code fragment is given below:")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "ul")
    val () = htmlprint_chardata (out)
    val () = {
      val () = list_vt_foreach_env<int><HTMLprint>(xs, out) where {
        implement
        list_vt_foreach$fwork<int><HTMLprint>(x, out) = {
          val () = htmlprint_tagname (out, "li")
          val () = htmlprint_chardata (out)
          val () = {
            val () = htmlprint_mac (out, x)

          } (* end of [li] *)
          val () = htmlprint_tagend (out, "li")
          val () = htmlprint_string (out, "\n\t")

        }
      }
    } (* end of [ul] *)
    val () = htmlprint_tagend (out, "ul")
    val () = htmlprint_tagname (out, "h2")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Advanced usage")

    } (* end of [h2] *)
    val () = htmlprint_tagend (out, "h2")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "It is possible to overload the symbol ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "htmlprint")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, " in\n    ATS to provide HTML printers for user-defined data types. To be\n    covered elsewhere.")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "The API provided by the library ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "htmlprint")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, " is\n    documented elsewhere (nowhere currently, to be precise).")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "A function ")

      val () = htmlprint_tagname (out, "code")
      val () = htmlprint_chardata (out)
      val () = {
        val () = htmlprint_string (out, "htmlprint_unsafe_inject")

      } (* end of [code] *)
      val () = htmlprint_tagend (out, "code")
      val () = htmlprint_string (out, " is provided\n    that allows for injecting strings as-is, with no escaping. Use at\n      your own risk.")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "h2")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Author and license")

    } (* end of [h2] *)
    val () = htmlprint_tagend (out, "h2")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "The license is 3-clause BSD.")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n    ")

    val () = htmlprint_tagname (out, "p")
    val () = htmlprint_chardata (out)
    val () = {
      val () = htmlprint_string (out, "Author: Artyom Shalkhakov (artyom DOT shalkhakov AT gmail DOT\n    com)")

    } (* end of [p] *)
    val () = htmlprint_tagend (out, "p")
    val () = htmlprint_string (out, "\n  ")

  } (* end of [body] *)
  val () = htmlprint_tagend (out, "body")
} (* end of [html] *)
val () = htmlprint_tagend (out, "html")
} (* end of code for [DATA/hello.html] *)
