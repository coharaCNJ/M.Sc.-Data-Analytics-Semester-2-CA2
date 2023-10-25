#!/usr/bin/env python3

import sys
import re

tweet = None
oldKey = None
Date = None

# It will be in the format key,val
# Where key is the date, val is the tweet with all non-alpha characters removed

for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, date, thisTweet = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, ",", Date, ",", tweet)
        oldKey = thisKey;
        tweet = re.sub(r'[^\w\s]', '', thisTweet);
        Date = date;

    oldKey = thisKey
    tweet = re.sub(r'[^\w\s]', '', thisTweet)
    Date = date

if oldKey != None:
    print(oldKey, ",", Date, ",", tweet)
