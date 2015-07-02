---
layout: article
title: Add Spaces to a Phrase/Paragraph Without Spaces
modified:
categories: algorithm
excerpt: Write a program that breaks up a string of words with no spaces into a string with the appropriate spaces.
tags: [medium_difficulty, c++]
image:
  feature:
  teaser:
  thumb:
comments: true
date: 2015-07-02T23:11:10+08:00
---

This is a solution to a sample “tech interview” question posted in [a video in Google career](https://www.google.com/about/careers/lifeatgoogle/hangout-on-air-tech-interviewing.html). The problem is

> Write a program that breaks up a string of words with no spaces into a string with the appropriate spaces.

If you just want to download the solution, click [here](https://github.com/lwchkg/wordbreaker).

Personally I have learned a lot from the video, e.g. clarify the question, using libraries (e.g. a dictionary) and APIs, find and solve a simplified version of the problem, etc. The Google people in the video even gave a sample solution involving two words. It seems easy to use recursion to recognize three or four words.

{% highlight java %}
public static String breakIntoSpaces(String source) {
  for (int i = 1; i < source.length(); i++)
  String left = source.substring(0, i);
  String right = sourve.substring(i, source.length());
  if (DICTIONARY.contains(left) && DICTIONARY.contains(right)) {
    return left + " " + right;
  }
}
{% endhighlight %}

But there is one missing piece... a real solution of the problem. The “method” was only about how to split into two words or three words. It is not scalable to large strings because that algorithm has complexity *O*(*n<sup>k</sup>*), where *k* is the number of words in the string.

{% include toc.html %}


## Solving the problem

First of all, the problem can be into two tasks:

1. Finding the dictionary word matches in the string.
1. Put the word matches together into a solution.

### Finding the dictionary word matches in the string

For this task, we have *n* possible starting positions in the string. If we take all the possible end positions, then we need to match with complexity *O*(*n*<sup>2</sup>). It is still slow, but much better than the method before.

Wait... Can the dictionary arranged in some way that matching can be more efficient? The answer is **yes**!

Store the dictionary into a **trie**. Then all end positions can be matched with a single lookup. For example, if “chairmanzzzz” is matched against a trie, both “chair” and “chairman” can be return at the same time.

Since each dictionary word only consist of a few letters (i.e. averages to a small constant), the matching can be done in constant time no matter how long the given string is. It means the matching has only complexity *O*(*n*) now.

(Note: There is a powerful Aho-Corasick algorithm that uses a modified trie to return all dictionary matches with one single lookup. Since I just want to test the approach, I decided not to use Aho-Corasick because it adds complexity.)

### Put the word matches together into a solution

Now I have all the dictionary matches. How do we find a solution?

Now view the match “starting from position 3 with a length of 4 letters” as “a directed edge from 3 to 7”. With directed edges we have an obvious solution: **Dijkstra algorithm**.

(Bonus question: what can be stored in the weights of the edges? Is it to possible take an advantage of these weights?)

Here are the steps of Dijkstra algorithm:

1. Assign node 0 with tentative distance 0. All nodes are unvisited.
2. Find a unvisited node *k*, which has a minimum tentative distance (from node 0).
3. Find the new tentative distance of all unvisited nodes connected to node *k*.
4. Mark node *k* visited.
5. Repeat steps (2) and (4) until there are no unvisited nodes with a tentative distance.

In this problem, step 2 can be replaced by “find a minimum value *k* that node (position) *k* is a unvisited node with a tentative distance.” The proof of the validity of this modification is left to readers.


## Coding

The solution was coded using C++. A few points are noted here:

- All letters are converted into lower case, and all non-letters are removed. Spaces in the user input are also removed for easy testing.

- A word list from [SCOWL](http://wordlist.aspell.net/) is used.

- For Dijkstra algorithm, a vector of matches is stored instead of just the best one. This creates the possibility of producing multiple results later.

- What to do if the end cannot be reached from the start? Just go as far as we can, output that part of the result, and do Dijkstra algorithm again starting from the next character.

- A [high-resolution timer](http://www.songho.ca/misc/timer/timer.html) written by Song Ho Ahn (2003) is used for timing.

- To make testing results easy to read, the given string is splitted using digits as the boundaries. The blocks of digits are simply outputted as single words.


## Testing and modifications

Testing is done against simple phrases and passages in the Wikipedia. As expected, my first try does yield a result quickly.

But the splitting result is not that good. The string <tt>iamahero</tt> turns out to be <tt>i a ma hero</tt> instead of <tt>i am a hero</tt>. (Note: “ma” is a dictionary word.) 

*Solution*: Put frequently used words a higher priority. The SCOWL dictionary comes with different numerical sizes! What a coincidence! So these sizes can be simply used as weights in Dijkstra algorithm for better results.

Now there is one other problem: <tt>eyesonme</tt> becomes <tt>eye son me</tt> instead of <tt>eyes on me</tt>.

*Solution*: The “s” looks better to be put in the first word (as plurals) instead of the second word. So the weights of all words that end with “s” are subtracted by 2.


## Revised version

The revised version returns better results. So we try splitting the passage again.

The program was run in a [ZOTAC ZBOX AD-02](http://www.zotac.com/ca/products/mini-pcs/product/mini-pcs/detail/zbox-ad02-1.html) with an AMD E-350 CPU.

** Input data (spaces are removed) **

<div class="highlight"><samp class="wrapok">AnovelisalongnarrativenormallyinprosewhichdescribesfictionalcharactersandeventsusuallyintheformofasequentialstoryWhileIanWattinTheRiseoftheNovel1957suggeststhatthenovelcameintobeingintheearly18thcenturythegenrehasalsobeendescribedaspossessingacontinuousandcomprehensivehistoryofabouttwothousandyearswithhistoricalrootsinClassicalGreeceandRomemedievalearlymodernromanceandinthetraditionofthenovellaThelatteranItalianwordusedtodescribeshortstoriessuppliedthepresentgenericEnglishterminthe18thcenturyMigueldeCervantesauthorofDonQuixoteisfrequentlycitedasthefirstsignificantEuropeannovelistofthemodernerathefirstpartofDonQuixotewaspublishedin1605WhileamoreprecisedefinitionofthegenreisdifficultthemainelementsthatcriticsdiscussarehowthenarrativeandespeciallytheplotisconstructedthethemessettingsandcharacterizationhowlanguageisusedandthewaythatplotcharacterandsettingrelatetorealityTheromanceisarelatedlongprosenarrativeWalterScottdefineditasafictitiousnarrativeinproseorversetheinterestofwhichturnsuponmarvellousanduncommonincidentswhereasinthenoveltheeventsareaccommodatedtotheordinarytrainofhumaneventsandthemodernstateofsocietyHowevermanyromancesincludingthehistoricalromancesofScottEmilyBrontesWutheringHeightsandHermanMelvillesMobyDickarealsofrequentlycallednovelsandScottdescribesromanceasakindredtermRomanceasdefinedhereshouldnotbeconfusedwiththegenrefictionloveromanceorromancenovelOtherEuropeanlanguagesdonotdistinguishbetweenromanceandnovelanovelisleromanderRomanilromanzo
</samp></div>

** Output **

<div class="highlight"><samp class="wrapok">Number of words after reading words-10.txt : 4101
Number of words after reading words-20.txt : 11329
Number of words after reading words-35.txt : 43292
Number of words after reading words-40.txt : 49406
Number of words after reading words-50.txt : 87966

Time elapsed in reading dictionary: 0.956782s

Enter the string to be broken into words: [[input skipped]]

Result:
a novel is along narrative normally in prose which describes fictional characters and events usually in the form of a sequential story while i an watt in the rise of the novel 1957 suggests that the novel came into being in the early 18 th century the genre has also been described as possessing a continuous and comprehensive history of about two thousand years with historical roots in classical greece and rome medieval early modern romance and in the tradition of the novel lathe latter an italian word used to describe short stories supplied the present generic english term in the 18 th century miguel de cervantes author of don quixote is frequently cited as the first significant europe an novelist of the modern era the first part of don quixote was published in 1605 while a more precise definition of the genre is difficult the main elements that critics discuss are how the narrative and especially the plot is constructed the themes settings and characterization how language is used and the way that plot character and setting relate to reality the romance is a related long prose narrative w alter scott defined it as a fictitious narrative in prose or verse the interest of which turns upon marvellous and uncommon incidents whereas in the novel the events are accommodated to the ordinary train of human events and the modern state of society however many romances including the historical romances of scott emily brontes wu the ring heights and her man melvilles mo by dick are also frequently called novels and scott describes romance as a kind red term romance as defined here should not be confused with the genre fiction love romance or romance novel other europe an languages do not distinguish between romance and novel a novel isle rom and err o ma nil roman z o 

Time elapsed in splitting: 0.00495095s
</samp></div>


## Conclusions

- English words are almost broken up perfectly. Only a few artifact remains: “Ian”, “Herman” (names) and some latin words that is not stored in the dictionary.

- Only a few milliseconds is used for splitting, and that already includes I/O time. (<tt>cin</tt> and <tt>cout</tt> are very inefficient.)

It means that the given problem is practically solved. Of course improvements can be made, including the following:

- Separate I/O from algorithm execution for better timing.

- Improve I/O performance.

- Create a GUI program. (Use wxWidgets.)

- Tweaking the weights of words. (How to do this automatically? User votes?)

- Handling of diacitrics. (Currently letters with diacitrics are skipped. They should be converted to the corresponding letter without diacitrics instead.)

- Text encoding (for diacitrics)

- Add punctuations and capital letters. (This is even harder than this problem.)

## Download the solution

The solution can be downloaded [here](https://github.com/lwchkg/wordbreaker).