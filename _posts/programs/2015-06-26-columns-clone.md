---
layout: article
title: Columns Clone (updated)
modified:
categories: programs
excerpt: A Columns clone made in 1997 that features a “PRO” mode.
tags: []
image:
  feature:
  teaser: programs/columns_clone_400.jpg
  thumb:
comments: true
date: 2016-01-04T01:35:58+08:00
---

<aside>
<a href="{% link programs/columns-clone/columns-clone.html %}"><img alt="Columns clone screenshot" src="{% link images/programs/columns_screenshot_01.png %}"></a>
</aside>

This clone of Columns was made in 1997, just after I had my public exam. This game features a “PRO” mode, which a worst possible piece is always generated.

You may compare the “PRO” mode with [Bastet Tetris](http://fph.altervista.org/prog/bastet.html) by Federico Poloni.

The program was ported from Visual Basic for DOS / SVGAPV to FreeBasic in 2007.

## Play in browser
{:.no_toc}

[Click here]({% link programs/columns-clone/columns-clone.html %}) to play the game in the browser. A keyboard is required to play the game.

This is made possible by [em-dosbox](https://github.com/dreamlayers/em-dosbox) by Boris Gjenero, DOSBox and Emscripten.

## Download
{:.no_toc}

- [Windows version binary]({% link assets/columns/columns_win_binary.7z %})
- [Windows version source (FreeBasic)]({% link assets/columns/columns_fb_src.7z %})
- [DOS version binaries (SVGA, CGA, text mode)]({% link assets/columns/columns_dos_binary.zip %})
- [DOS version source (Visual Basic for DOS) and graphics assets]({% link assets/columns/columns_dos_src.zip %})

(Last update: 3-Jan-2016)

## Game manual
{:.no_toc}

{% include toc.html %}


## Controls

### Keys

Controls for Windows version:

* Quit Game: ESC
* Left Player: A, S, D, X
* Right Player: Left, Up/Centre, Right, Down

For the DOS version, read the file README for controls.

### Not During a Game

|             | Left Player  | Right Player |
| ----------- |:------------:|:------------:|
| Level       | A            | Left         |
| Difficulty  | D            | Up / Centre  |
| Start Game  | S            | Right        |
| High Score  | X            | Down         |

### During a Game

|             | Left Player  | Right Player |
| ----------- |:------------:|:------------:|
| Move Left   | A            | Left         |
| Move Right  | D            | Up / Centre  |
| Cycle Jewels| S            | Right        |
| Drop        | X            | Down         |

### Entering Name for High Score

|                 | Left Player  | Right Player |
| --------------- |:------------:|:------------:|
| Previous Letter | A            | Left         |
| Next Letter     | D            | Up / Centre  |
| A → B → C → ... | S            | Right        |
| C → B → A → ... | X            | Down         |

Pressing “Next Letter” at the third letter finishes high score input.

## Gameplay

### Objective

Jewels drop to the well three at a time (vertically aligned). You are going to prevent the well from filling up by making the jewels disappear.

You can move the jewels left or right, and also to cycle their positions.

When three or more jewels of the same color are connected to a straight line horizontally, vertically or diagonally, these jewels will disappear. The jewels above then settle by gravity. If this cause another three or more jewels of the same color connected to a straight line, they also disappear. This process can be repeated more than five times.

You sometimes get a white special jewel. You may drop it on another jewel, and then all jewels of that color will disappear.


### Scoring

You score each time when you drop a jewel or make jewels disappear.

 Event                 |  Score gained
-----------------------|-------------------------------------------------------
Drop jewels by Drop key (X/Down)     | Number of tiles dropped × (Level + 1)
Making lines           | 30 × No of lines made x (Level + 1) × Combo Counter
Dropping white jewels  | 10 × No of jewels disappearing (excluding white blocks)


The combo counter will start at 1 when you drop a jewel block. After jewels disappear (including the use of white block), the counter will increase by 1. If the process of disappearing continue without dropping another jewel block, the counter will then increase to 2, 3, 4, 5, and so on.

A line with 4 jewels is treated as 2 lines, 5 jewels is 3 lines, and so on.

It is possible to get a high score by starting at a high level, drop blocks by pressing X/2 frequently, and to make combos.


### Level and Difficulty

The level is about the natural dropping speed of the jewel. The higher the level, the higher the speed of dropping. The level will be increased each time you make 30 jewels disappear (excluding white jewels), to a maximum of 9.

If you start at a level higher than 0, then the level will only increase if the number of disappeared jewels reaches 30 × (Level + 1)

The difficulty will affect the game in the ways below:

Difficulty | Description
---------- | -----------
Novice | 4 colors
Middle | 5 colors
Advanced | 6 colors
Professional | 6 colors + bad surprises

This clone's speciality is the professional level. Make sure you try it.

### High Score

The top 10 scores are be kept for each difficulty. Once you have entered top 10, you need to enter your name in the high score. For the name, only 3 letters or digits are allowed.

You may consider yourself getting a really good score if your score is above:

Difficulty | Score above
---------- | -----------
Novice        | 110000
Middle        | 80000
Advanced      | 65000
Professional  | 50000

## Updates

**04-Jan-2016**

- Fixed wrong bounds calculation, which results in crashes in FreeBasic version.<br>(P.S.: I have no idea why this is not caught in VB-DOS.)
- FreeBasic version updated to allow compilation to 64-bit and DOS executable.
- Renamed variables to avoid conflict with the new keywords (i.e. True and False) in FreeBasic 1.04.
