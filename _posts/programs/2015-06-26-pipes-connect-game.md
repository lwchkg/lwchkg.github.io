---
layout: article
title: Pipes Connect Game
modified:
categories: programs
excerpt: Connect the pipes into a single fully connected network, without loops and free ends.
tags: []
image:
  feature:
  teaser: programs/pipes_400.png
  thumb:
comments: true
date: 2015-06-26T11:12:14+08:00
modified: 2023-10-05T14:51:59Z
---

You are given a grid of pipes of different shapes. The aim of the game is to connect all the pipes together, without loops and free ends. [Play the game now](https://lwchkg.github.io/pipesgame/pipes.html){:target="_blank"}.

You may connect the pipes by rotating the pieces only. See the pictures below to see what a new game and its finished state look like.

<figure class="half">
	<img alt="start" src="{% link images/programs/pipes_intro1.png %}">
	<img alt="finish" src="{% link images/programs/pipes_intro2.png %}">
</figure>

## Playing the game

[Play the game now](https://lwchkg.github.io/pipesgame/pipes.html){:target="_blank"}. Currently the game works well only for desktop computers with a mouse.


## Board size

The images above have a board size of 8 × 8. If you think that it is too easy, you can increase the board size. The board size can be as large as 100 × 100.


## Known issues

1. The board does not show if video memory is not enough. A workaround is to reduce the tile size (e.g. from “Large (64×64)” to “Small (32×32)”).
2. The game is not handling touch events properly. (Therefore it cannot be played with a touch screen.)

(Note: A work-in-progress is being created to address the problems. Currently it is too early to release anything.)


## Source files

[Click here](https://github.com/lwchkg/pipesgame){:target="_blank"} to see the source.


## Inspired from

- [Pipes (J2ME)](https://www.michaelkerley.net/pipes-j2me.html){:target="_blank"}
  (This is the version I played with my Nokia phone daily until the phone is replaced.)

- Another less advanced HTML + JavaScript version the same game. I am unable to find the link at the time of writing. (Disappeared from the internet?)

## Similar games

- [Net from Simon Tatham Puzzle Collection](http://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/net.html){:target="_blank"}
  (A similar game without the cross tile (more difficult), with less attractive graphics)

- [Android port of Simon Tatham Puzzle](https://play.google.com/store/apps/details?id=name.boyle.chris.sgtpuzzles){:target="_blank"}
  (A professionally created port of the above collection for Android. Created by [Chris Boyle](https://chris.boyle.name/projects/android-puzzles/). This is one of my must-install game in my mobile phone.)

- [Hexagon](https://play.google.com/store/apps/details?id=com.fmcstudio.hexagon){:target="_blank"}
  (A similar Android game with hexagonal tiles. Note: game progress may be lost if the phone is asleep.)
