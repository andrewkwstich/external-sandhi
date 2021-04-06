# Introduction

## What is External Sandhi?
'Sandhi' is a technical term coined by Indian grammarians thousands of years ago. Though originally used to describe a phenomenon in Sanskrit phonetics, it has lately been adopted by modern linguists to describe similar phenomena in a variety of languages. It refers to any case where the pronunciation of one sound is affected by the presence of nearby sounds. An example from English is the pronunciation of the word 'the': like 'thee' before a word starting with a vowel, like 'tha' before a word starting with a consonant. This kind of sandhi is called 'external' sandhi, because the rule applies between, not within, words.

In Sanskrit, external sandhi is governed by a rich set of rules. Unlike with 'the', the rules do not refer to specific words; rather, they refer to sequences of sounds. Sometimes the changes effected by the rules are so significant that the 'underlying' words are difficult to make out. For example, the following half-verse (from Bhagavad Gita, chapter 1, verse 13),

<b> sahasaivābhyahanyanta sa śabdas tumulo 'bhavat, </b>

consists of the following underlying words before external sandhi is applied:

<b> sahasā eva abhyahanyanta sa śabdaḥ tumulaḥ abhavat. </b>

## What is this Project for?
This program allows the user to experiment with external sandhi rules in Sanskrit: it transforms an input string of underlying words (with no limit on string length) into an output string in which all the rules have been applied. It is most useful as an aid in writing Sanskrit, but can also be used to test possible underlying strings when a difficult passage (such as the one quoted above) is encountered.

## What are the Rules of External Sandhi?
Tables from a Sanskrit handbook, depicting the outputs of external sandhi, have been uploaded to OneDrive:

https://1drv.ms/b/s!AqxA_RfLr2tCiGwg5r7Xq73AZUvA?e=HpYhfa

From: Coulson, M., Gombrich, R. F., & Benson, J. W. (2006). Teach Yourself Sanskrit. McGraw-Hill.

Each value in the tables represents the output given a pair of words.*** The first table gives the outputs for when the first word ends with a consonant. The second table gives the outputs for when the first word ends with a vowel and the second word begins with a vowel. 'Final' refers to the last sound(s) of the first word, 'initial' to the first sound of the second word.

You will notice regularities in these outputs. In the first table, the alternation between 'k' and 'g' tracks the alternation between 'ṭ' and 'ḍ'. That is because the second sound in each pair is pronounced identically to the first, except with concurrent use of the voice; voicing is added in the same contexts for both 'k' and 'ṭ'. To capture these regularities, `sounds.py` contains a dictionary associating sounds with their features. The rules in `rules.py` frequently refer to features rather than to individual sounds.

***Except in the first table, where under 'Initial letters' the value is 'zero'; in that case the rules apply to the end of a single word.

# Usage

## Input/Output Options
When executing the code, the user will be prompted to select a transliteration option, which will apply to both input and output. Two options are available. The first is the International Alphabet of Sanskrit Transliteration (IAST), which is used in the above passage. The second is non-standard but does not require any special characters. In it, the following IAST characters/digraphs are substituted as indicated:

ā becomes A\
ḍ becomes D\
ḥ becomes H\
ī becomes I\
ṃ becomes M\
ṇ becomes N\
ñ becomes J\
ṅ becomes G\
ṛ becomes R\
ṝ becomes RR\
ṣ becomes S\
ś becomes z\
ṭ becomes T\
ū becomes U\
ḍh becomes Dh\
ṭh becomes Th

Except when using non-standard transliteration and inputting characters that are capitalized in the above list of IAST equivalents, input should all be in lower case.

## How to Execute the Code
In the Python terminal, run `main.py`. After choosing an input method (IAST or non-standard), you will see the following prompt: 
```
Please enter some Sanskrit text: 
```
When the text is submitted, the transformed string will be printed. Entering a sequence of characters that is impermissible in Sanskrit, such as a pair of words where the second word begins with 'H', may result in an error.

## How to Do External Sandhi Programmatically

```
from main import do_external_sandhi
from transliteration import IAST

do_external_sandhi('samavetāḥ yuyutsavaḥ', IAST)  # Should output 'samavetā yuyutsavaḥ'
```
The default transliteration option is set to non-standard. Thus:

```
from main import do_external_sandhi

do_external_sandhi('samavetAH yuyutsavaH')  # Should output 'samavetA yuyutsavaH'
```

## How to Test the Code
In the Python terminal, run `tests.py`. You can create your own unit tests by consulting the pdf linked above. If all unit tests are successful,
```
All unit tests successful
```
will be printed.

When testing functions of the form

```
assert RULE.applies_to(...)
```
, use non-standard input.

# Requirements
This program has been tested in Python 3.8. Note that the inclusion of IAST characters may cause some environments to throw an encoding error.