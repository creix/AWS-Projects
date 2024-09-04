# README #

## Report

### Task 2.1

This task was pretty straightforward since it was easily reproducible with the code provided in the assigment without the need to modify anything.

After importing the nltk package and the english tokenizer without any problem we can use the code to analyze the `FirstContactWithTensorFlow.txt` file.

### Task 2.1.1: Word count 1

This is the result of the first tokenization of the file:
```
10 most common words
=====
'the' — 1343
',' — 1251
'.' — 808
')' — 638
'(' — 637
'of' — 586
'to' — 491
'a' — 470
':' — 454
'in' — 417

=====
Total number of words: 25185
```

### Task 2.1.2: Remove punctuation
In this second part of the task we proceed to remove all the punctuation from our tokenization result, in order to get a more significant results of the words that are mostly present in the text.

This is the result of this second task:

```
10 most common words without punktuation
=====
'the' — 1445
'of' — 587
'to' — 532
'in' — 509
'a' — 496
'and' — 347
'tf' — 304
'is' — 289
'we' — 283
'that' — 276

=====
Total number of words: 21661
```

### Task 2.1.3: Stop Words

As we can see from the results of the last task the 10 most common words are not that significant, the majority of it are the so-called "stop words", that are a set of words commonly used in a language, for instance words like "the", "of", "to", "and".

In order to get a better language analysis of the text provided we need to remove these words as they are not relevant for our tasks.
Using the code provided we can do so and this is the final result:

```
10 most common words without punktuation and stop words
=====
'tf' — 304
'tensorflow' — 241
'0' — 241
'1' — 154
'data' — 121
'tensor' — 101
'code' — 90
'learning' — 86
'dimension' — 84
'2' — 80

=====
Total number of words: 13146
```

We can see that from the first result the total number of words has almost halved, but finally we have a useful analysis of the most common word in the book. As it was expected, the two most common words are correlated to tensorflow, in particular the most common one it "tf", that is the usual abbreviation used to refer to tensorflow in the code and the second one is actually "tensorflow". 

### Task 2.4

Since the new update of the Twitter API no longer provide free access to fetching the tweets we instead used the API
provided by a similar social media called _Counter Social_.

The API are public and do not need an account for the basic functions such as fetching public timelines and public
accounts.

Because of that we can directly write in our python script _counterSocial1.py_ the code needed to fetch a public
timeline.

The API returns by default 20 item that can be limited inserting at the end of the URL the string `?limit=2`, where 2
can be substituted by any number. Analyzing the items we can see that there are two main sections, one with all the
information regarding the post itself, such as the content, the URL, the number of replies and favourites and the other
regarding the information about the account that posted it. Moreover are present also other information for the display
of the content, for instance when it's present a Youtube link or a media attached. A complete list of all the parameter
can be found on [this doc](https://counter.social/apidocs/entities/status/index.html).

To gain access also to information that are not publicly available we need to have an access token for our application.
Following the docs provided, using the script _counterSocial2.py_ we can firstly obtain our `client_id`
and `client_secret`:

```json
{
  "id": "27461",
  "name": "CCBDAApplication",
  "website": "http://localhost",
  "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
  "client_id": "937c51173b3756cc6a13d8434e8c4b0652165c4f3b96e7fe7284061582d12a20",
  "client_secret": "f9ad13b76163f78ddbb017e020debf9cf4acdf5339edac3699012b161ca0902a",
  "vapid_key": "BHeigrRLUSb-scdV4VhYu5Nt_jE5lUsk5ymF6lSo5Q2QqkUQhuDPGuMXJCtMIfWvB6c5mnRDxncXX6KXJ3jw9Ww="
}
```

Then using these two information we can finally obtain the access token for our application that we will use for the
future requests:

```json
{
  "access_token": "14e1a78efd2db4ae90c3cf8d647150062c13f59b2619ff3439316323ddbc84b6",
  "token_type": "Bearer",
  "scope": "read",
  "created_at": 1709215324
}
```

To verify that our access token is valid we can call the API endpoint `verify_credentials` that differently from what is
state on the assigment documentation does not return the same response as before, but instead return an Application
entity:

```json
{
  "name": "CCBDAApplication",
  "website": "http://localhost",
  "vapid_key": "BHeigrRLUSb-scdV4VhYu5Nt_jE5lUsk5ymF6lSo5Q2QqkUQhuDPGuMXJCtMIfWvB6c5mnRDxncXX6KXJ3jw9Ww="
}
```

Finally, using our access token we can finally get the list of follower of the first user that we have retrieved from
the public timeline using part of the script inside _counterSocial1.py_. This is part of the response that we got:

```json
{
  "id": "678247",
  "username": "LowEndMuse",
  "acct": "LowEndMuse",
  "display_name": "\u2638\ufe0fTK\u00b2\u2638\ufe0f\ud83c\uddfa\ud83c\udde6\ud83c\udf39\ud83d\udd6f\ufe0f29K\ud83d\udd6f\ufe0f",
  "locked": false,
  "bot": false,
  "created_at": "2024-01-29T02:13:54.941Z",
  "note": "<p>I Stand with innocent civilians in Gaza, as well as with the hostages and their families in Israel.<br />Married, 1 son, 5 dogs, 1 cat.<br />Buddhist,  {DSA\ud83c\udf39}  Musician</p>",
  "url": "https://counter.social/@LowEndMuse",
  "avatar": "https://counter.social/system/accounts/avatars/000/678/247/original/7800c45a783a0e81.png?1709073389",
  "avatar_static": "https://counter.social/system/accounts/avatars/000/678/247/original/7800c45a783a0e81.png?1709073389",
  "header": "https://counter.social/system/accounts/headers/000/678/247/original/8d6eeec34100fa4f.png?1706494967",
  "header_static": "https://counter.social/system/accounts/headers/000/678/247/original/8d6eeec34100fa4f.png?1706494967",
  "followers_count": 158,
  "following_count": 187,
  "status_count": 866,
  "emojis": [],
  "fields": []
}
{
  "id": "111329",
  "username": "Kinniska",
  "acct": "Kinniska",
  "display_name": "Kinniska",
  "locked": false,
  "bot": false,
  "created_at": "2022-04-26T20:42:47.268Z",
  "note": "<p>Hoping this will be more like early twitter\u2026 \ud83c\udfbc\ud83c\udfb5\ud83c\udfb6hope springs eternal? Now, where\u2019s my blowtorch\u2026?</p>",
  "url": "https://counter.social/@Kinniska",
  "avatar": "https://counter.social/system/accounts/avatars/000/111/329/original/e8380f44f8779244.jpeg?1651006395",
  "avatar_static": "https://counter.social/system/accounts/avatars/000/111/329/original/e8380f44f8779244.jpeg?1651006395",
  "header": "https://counter.social/system/accounts/headers/000/111/329/original/76f80bf5dcd83409.jpeg?1651006395",
  "header_static": "https://counter.social/system/accounts/headers/000/111/329/original/76f80bf5dcd83409.jpeg?1651006395",
  "followers_count": 133,
  "following_count": 182,
  "status_count": 1549,
  "emojis": [],
  "fields": [
    {
      "name": "Avocation",
      "value": "Artist, my process resembles Zen Hard Practice whether I intended that or not",
      "verified_at": null
    },
    {
      "name": "Misc interests",
      "value": "History, archaeology, music, fiber/ textiles, travel, epidemiology",
      "verified_at": null
    }
  ]
}
...
```

### Task 2.3

Since we were not able to use the Twitter API, we tried to apply the same pre-processing method to the status taken from Counter Social.

We firstly have created a script called _Tweet_Tokenizer.py_ that contains the code and the regex necessary to tokenize correctly the tweets taken from [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/).

Then we created another script called _counterSocial3.py_ to make an analysis of the token similar to the one of the Task 2.1. 
Here we first fetch the most recent status published on the public timeline as we have seen in the script _counterSocial1.py_, then we tokenize them using the preprocessing function declared in _Tweet_Tokenizer.py_.

```
[('.', 33), ('<p>', 28), ('</p>', 28), ('</span>', 18), ('/', 18), ('a', 17), ('to', 15), ('</a>', 13), (',', 13), ('!', 11), (';', 10), ('<span class="invisible">', 10), ('"', 10), ('and', 9), ('&', 9), ('#', 8), ('<span>', 8), ('I', 8), ('the', 7), ('it', 7)]
```

We can already see a problem with the content of the status used in Counter Social, in fact it is an HTML string and this makes a lot more difficult tokenizing effectively the strings.

After the tokenization we can remove all the stop words, punctuation and the most repeating HTML tags present inside the content. At this point we can print the most common words used inside the 20 most recent status.

This is the result after these preprocessing steps:
```
[('<span class="invisible">', 10), ('I', 8), ('make', 5), ('class', 5), ('ellipsis', 5), ('com', 4), ('2024', 4), ('https://</span><span', 4), ('Israel', 4), ('Gaza', 4), ('03', 3), ('U', 3), ('S', 3), ('framework', 3), ('cease-fire', 3), ('Hamas', 3), ('apnews', 3), ('article', 3), ('531593', 3), ('…', 2)]
```

As we can see there are still problem with HTML tags and other special words that cannot be removed with a regex and need to eventually be added manually to the "exclusion list".

#### Yodapp

As for the practice with external APIs, we have created the `yodapp.py`, which uses [Yoda Translator API](https://rapidapi.com/orthosie/api/yoda-translator). The interaction with the app is very fun and trivial: the app asks user to input the text to be translated to Yoda'ish, after the input it prints out the translated text. App asks for the input endlessly in the app run-loop unless user enters `0`. 

It is worth mentioning that since the repository is private we did not remove the API key from the published file in order to let professor validate the app by running it. We will terminate the key anyway in a week or so.

The implementation did not take more time than one hour. Not difficulties were spotted during the app creation.

### Conclusion

This laboratory took us about 4/5 hours each, unfortunately we couldn't do the real tweet analysis because of the change in the APIs rules and this lead to a more challenging analysis made with the status of Counter Social that differently from the tweets are provided in th form of an HTML string. This caused the major problem in our laboratory, because the tokenization was considering also part of HTML that are not relevant for the type of analysis that we want to do. 
We tried to search on the web for an effective way to remove the HTML tags with regex, but none of the methods found were working properly and some tags were always left out. 
We partially resolved this issue by adding the most common tags found in the structure of the status to the exclusion list, this improved in some way the analysis but still the problem was not completely removed.


## Contact ##

- Danila Kokin <danila.kokin@estudiantat.upc.edu>
- Christian Biffi <christian.biffi@estudiantat.upc.edu>