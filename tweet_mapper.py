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
        if len(data) == 6:
                Num, tweetID, Date, Query, Username, Tweet = data
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 7:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 8:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 9:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 10:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8] + data[9]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 11:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8] + data[9] + data[10]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 12:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8] + data[9] + data[10]+ data[11]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) == 13:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8] + data[9] + data[10] + data[11] + data[12]
                print("{0},{1},{2}".format(Num, Date, Tweet))
        if len(data) >= 14:
                Num = data[0]
                Date = data[2]
                Tweet = data[5] + data[6] + data[7] + data[8] + data[9] + data[10] + data[11] + data[12] + data[13]
                print("{0},{1},{2}".format(Num, Date, Tweet))
