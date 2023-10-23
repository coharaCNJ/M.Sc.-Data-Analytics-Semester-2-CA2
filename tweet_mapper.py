#!/usr/bin/env python3

# extract Date and Tweet from each entry
# An axploration on the data shows that there are no queries associated with any tweet, and username is not something
# that will be analysed here, so everything except date and tweet can be dropped from the raw data.

# Format of each line is:
# tweetID\Date\Query\Username\Tweet
#

import sys

for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 5:
                # These are names of the columns/ attributes given to the data file
                tweetID, Date, Query, Username, Tweet = data
                print("{0}\t{1}".format(Date, Tweet))
