---
layout: article
title: Hello Dict
categories: programs
excerpt: English dictionary build with React.
tags: []
image:
  feature:
  teaser: programs/hellodict_800.webp
  thumb:
comments: true
date: 2024-01-02T17:59:13Z
modified:
---
<aside>
<img alt="Sunrise and Sunset Calculator feature picture" src="{% link images/programs/hellodict_800.webp %}">
</aside>

Dictionary coded in React.js. Just type in the word in the box and search.

Coded with ❤️ by WC Leung.

## Demo & live app

- [Launch HelloDict](https://hellodict.netlify.app){:target="_blank"}
- [Lookup for the word ‘dictionary’](https://hellodict.netlify.app#/word/dictionary){:target="_blank"}
- [Search for pattern ‘h\*ll?’](https://hellodict.netlify.app/#/search/h*ll%3F){:target="_blank"}

## Features

- Wildcard pattern search with ‘\*’ (zero or more unknown characters) and ‘?’
  (one unknown character).
- Privacy friendly. The whole dictionary is downloaded right into your web app.
  Dictionary lookups are NOT sent online.
- Friendly to both desktop and mobile devices.
- Dark mode.
- Shareable links for your dictionary lookups. (See
  [this](https://en.wikipedia.org/wiki/URI_fragment) to know how privacy works
  with these links.)

## Tech stack

- React, TypeScript and Vite
- EsLint and Prettier for linting and formatting
- ViTest for unit testing and component testing
- Cypress for end-to-end testing
- GitHub Actions for continuous integration
- Netlify for continuous delivery

## Handling of dictionary data

The data in the app is fetched from https://github.com/lwchkg/hello-dict-data
using jsDelivr CDN, which has a size of about 10.3 MB after compression. The
whole dictionary is downloaded onto your computer when the app loads.

To save bandwidth, the same dictionary data file is never fetched again unless
your browser cache is cleared.

Considering the large size of the dictionary data, it is handled by a web worker
to avoid blocking the UI.

## Credits

Dictionary data from
[GNU Collaborative International Dictionary of English](https://gcide.gnu.org.ua/),
version 0.51.

The OneIdentity ZSTD library (https://github.com/OneIdentity/zstd-js) for their
compression library.

## To-dos

- Find similar words if there is no match.
- Add WordNet data.
- Transform the word with the WordNet algorithm (e.g. studies -> study) before
  doing the dictionary lookup.
