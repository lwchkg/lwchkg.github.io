---
layout: archive
title: "Welcome to lwchkg’s website"
---

Welcome to lwchkg’s website. Here you can find my computer programs and notes in mathematics.

You may also find something [about me]({% link about.md %}).

# Latest posts

<div class="tiles">
{% for post in site.posts %}
	{% include post-grid.html show-categories="true" %}
{% endfor %}
</div><!-- /.tiles -->