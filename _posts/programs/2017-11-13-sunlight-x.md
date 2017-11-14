---
layout: article
title: sunlight-x syntax highlighter
modified:
categories: programs
excerpt: “Intelligent” syntax highlighter developed originally by Tommy Montgomery. Now ported to node.js.
tags: []
image:
  feature:
  teaser: programs/sunlight-x_400.png
  thumb:
comments: true
date: 2017-11-13T23:42:51+08:00
---

<aside>
<a href="https://raw.githack.com/lwchkg/sunlight-x/master/test/output/integration-expected.html"><img alt="sunlight-x sample rendering" src="{% link images/programs/sunlight-x_400.png %}"></a>
</aside>

Sunlight-x is a syntax highlighter for node.js.
[Here](https://raw.githack.com/lwchkg/sunlight-x/master/test/output/integration-expected.html) is the demo of sunlight-x.
For details, check the [GitHub repo](https://github.com/lwchkg/sunlight-x).

## Why sunlight-x is created

Sunlight-x is a fork of [Sunlight](http://sunlightjs.com/) by Tommy Montgomery.
Tommy's brilliant design makes Sunlight highlight better then common javascript highlighters like [highlight.js](https://highlightjs.org/), and it can highlight almost 30 languages.

The original Sunlight is meant to be included into the browser. With some work, I was able to wrap the original Sunlight in a GitBook plugin, and it was used to render my books that teaches VB.NET.
(Free soft copy of the books are available upon request.)

Unfortunately, the original code was hard to maintain because of the use of past Javascript patterns, e.g. self-invoking functions, putting everything in a single file, outdated build tools, etc.
To make things worse, the original author, Tommy Montgomery, is also out of my reach, so I am unable to contribute to the original Sunlight.

That's why sunlight-x is born.


## My contributions

- Divided the single-file code into modules.

- Code is annotated with Flow, and tests are runned with Jest.

- The CSS is made easier to customize. Also, multiple themes can be shown simultaneously in the same page.

- Extra tests are made to make sure that every change in the source code is tested. The most important of these extra tests is the demo, which is itself an integration test.

- Some refactoring was done to improve the maintainablity of the source code. (Note: more refactors are planned to improve the APIs.)


## Getting sunlight-x

Check the [GitHub repo](https://github.com/lwchkg/sunlight-x) for downloads and installation instructions.
