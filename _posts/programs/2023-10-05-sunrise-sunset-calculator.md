---
layout: article
title: Sunrise and Sunset Times App
categories: programs
excerpt: An app that shows sunrise and sunset times, built with Flutter.
tags: []
image:
  feature:
  teaser: programs/sunrise_sunset_calculator_800.webp
  thumb:
comments: true
date: 2023-10-05T18:34:25Z
modified:
---
<aside>
<img alt="Sunrise and Sunset Calculator feature picture" src="{% link images/programs/sunrise_sunset_calculator_800.webp %}">
</aside>

The main feature of this app is to show the sunrise and sunset times in the next 7 days, or in a specific month.

I wanted to have an app that tell when will the sun rise and set, so I can plan my outdoor time.
So this app is created as my first try with Flutter - a cross platform app development kit.

## How to use

1. [Open the browser app](https://lwchkg.github.io/sunrise_sunset_calculator/){:target="_blank"}.
   (Note: the app will be available in Android soon.)
2. Allow the use of your location.
3. **If you care more about sunlight than actual sunrise and sunset (which I
   do), check the civil twilight times.**
4. Scroll down to view the sunrise and sunset times for the next 7 days.
5. For other days click “More days...”.

## Accuracy of sunrise and sunset times algorithm

The algorithm in
[NOAA Sunrise/Sunset and Solar Position Calculators](https://gml.noaa.gov/grad/solcalc/calcdetails.html){:target="_blank"}
is used in this app. According to its web site, “sunrise and sunset results are
theoretically accurate to within a minute for locations between +/- 72°
latitude, and within 10 minutes outside of those latitudes. However, due to
variations in atmospheric composition, temperature, pressure and conditions,
observed values may vary from calculations.”

## More information

- [User documentation (Wiki)](https://www.github.com/lwchkg/sunrise_sunset_calculator/wiki/){:target="_blank"}
- [Source code](https://www.github.com/lwchkg/sunrise_sunset_calculator){:target="_blank"}

## Screenshots

<figure class="half">
<img alt="Home screen" src="{% link images/programs/sunrise_sunset_calculator_screenshot_01.webp %}">
<img alt="Monthly info" src="{% link images/programs/sunrise_sunset_calculator_screenshot_02.webp %}">
</figure>

## Similar calculators

[US Naval Observatory](https://aa.usno.navy.mil/data/RS_OneDay){:target="_blank"} - might be more
accurate than this app, especially if you live in the arctic circle.

[Stonekick Sun Position App](https://stonekick.com/sunposition.html){:target="_blank"} - more
information, but only the information of the current day is free.
