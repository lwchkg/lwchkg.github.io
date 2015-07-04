---
layout: article
title: VB.NET Utilities for Teachers
modified: 2015-07-04T22:25:45+08:00
categories: programs
excerpt: A collection of VB.NET utilities created when I was teaching VB.NET in a secondary school.
tags: []
image:
  feature:
  teaser: programs/vbnetutil_400.jpg
  thumb:
comments: true
date: 2015-06-29T16:32:45+08:00
---

This is a collection of VB.NET utilities I have created when I was teaching VB.NET in a secondary school. The programs include a MsgBox and a InputBox demonstration, an expression evaluator and a code snippet runner.

## Download
{:.no_toc}

- [Binary]({{ site_url }}/assets/vb.net-util.7z) (Compiled with VB 2010 with .NET Framework 4)

- [Source](https://github.com/lwchkg/vb.net-util)

## About the utilities
{:.no_toc}

{% include toc.html %}

### MsgBox Demo / InputBox Demo

As their name implies, they are used to demonstrate the capabilities of MsgBox and InputBox statements.

<figure class="half">
<img alt="MsgBox Demo Screenshot" src="{{ site_url }}/images/programs/vbnetutil_screenshot_01.png">
<br><br>
<img alt="InputBox Demo Screenshot" src="{{ site_url }}/images/programs/vbnetutil_screenshot_02.png">
<figcaption>Screenshots of MsgBox Demo and InputBox Demo</figcaption>
</figure>

These two programs have two functions, namely

- To show the required MsgBox / InputBox.
- Generate VB.NET code for the said MsgBox / InputBox and copy the code to the clipboard.

The programs are used myself to create the teacher’s version of VB.NET worksheet or exam papers. To take high quality screenshots, I recommend [Greenshot](http://getgreenshot.org/).




### Expression Evaluator

This program finds out the values of multiple VB.NET expressions. Enter one expression in a line, and this program outputs the result in the corresponding line. The main use of the program is to create worksheets which ask students to evaluate VB.NET expressions. (Manual calculations are prone to errors, so automation is necessary.)

<figure class="full">
<img alt="Expression Evaluator Screenshot" src="{{ site_url }}/images/programs/vbnetutil_screenshot_03.png">
<figcaption>Screenshot of Expression Evaluator</figcaption>
</figure>

For example, you want to calculate the answers for the following:

| VB expression                                              | Result            |
|------------------------------------------------------------|-------------------|
| `Strings.Right("polar", 2) & Strings.Left("ease", 3)`      | `"areas"`         |
| `Len("--Computer Literacy--")`                             | `21 `             |
| `"S." & Strings.Left("2A", 1)`                             | `"S.2"`           |
| `Mid("dictionary", 5, 3)`                                  | `"ion"`           |
| `UCase(LCase("Hello!"))`                                   | `"HELLO!"`        |
| `LCase(Trim("   Mr. Wood "))`                              | `"mr.   wood"`    |
| `Dim s As String = "Testing"`<br>`s = Mid(s, Len(s) - 2, 2)` | `"in"`            |

The input of the program looks like this: (you need to remove `s =` in the last line.)

{% highlight vbnet %}
Strings.Right("polar", 2) & Strings.Left("ease", 3)
Len("--Computer Literacy--")
"S." & Strings.Left("2A", 1)
Mid("dictionary", 5, 3)
UCase(LCase("Hello!"))
LCase(Trim("   Mr. Wood "))
Dim s As String = "Testing"
Mid(s, Len(s) - 2, 2)
{% endhighlight %}

### Snippet Runner

This program runs a VB.NET code snippet. The Console and Debug/Trace outputs are shown when you run the code snippet.

The Console input can be specified when you execute the program. The input can be dumped to the Console output, so it appears to be entered by a real user.

Subroutines (i.e. `Sub` and `Function`) are not supported.

<figure class="full">
<img alt="Snippet Runner Screenshot" src="{{ site_url }}/images/programs/vbnetutil_screenshot_04.png">
<figcaption>Screenshot of Snippet Runner</figcaption>
</figure>