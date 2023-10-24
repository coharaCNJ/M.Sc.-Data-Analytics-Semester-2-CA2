#!/usr/bin/env python3

import sys
import re

tweet = None
oldKey = None

# It will be in the format key,val
# Where key is the date, val is the tweet with all non-alpha characters removed

for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisTweet = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, ",", tweet)
        oldKey = thisKey;
        tweet = re.sub(r'[^\w\s]', '', thisTweet)

    oldKey = thisKey
    tweet = re.sub(r'[^\w\s]', '', thisTweet)

if oldKey != None:
    print(oldKey, ",", tweet)
