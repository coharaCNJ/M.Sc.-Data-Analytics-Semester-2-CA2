#!/usr/bin/env python3

# extract tweetID, Date and Tweet from each entry
# An axploration on the data shows that there are no queries associated with any tweet, and username is not something
# that will be analysed here, so everything except tweet Num (unique) date, and tweet, can be dropped from the raw data.

# Format of each line is:
# tweetID\Date\Query\Username\Tweet
#

import sys

for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 6:
            Num, tweetID, Date, Query, Username, Tweet = data
            print("{0},{1},{2}".format(tweetID, Date, Tweet))
        elif len(data) > 6:
            tweetID = data[1]
            Date = data[2]
            Tweet = data[5]
            for y in range(6,len(data)):
                Tweet = Tweet + " " + data[y]
            print("{0},{1},{2}".format(tweetID, Date, Tweet))
