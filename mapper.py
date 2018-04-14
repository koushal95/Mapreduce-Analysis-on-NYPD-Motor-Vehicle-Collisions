#!/usr/bin/env python
import sys
import re

header = 1
for line in sys.stdin:
        if header:
                # change header flag
                header = 0
                # skip this row as it is header
                continue
        # remove the trailing whitespaces
        line = line.strip()
        # replace the pattern with whitespaces in each line
        line = re.sub(r'".*"', ' ', line)
        # split the line string into columns/words
        columns = line.split(",")
        # select only the required columns that correspond to the vehicle types
        required_columns = columns[24:]
        # there is a row in the data with new line character in its OFF STREET NAME
        if len(required_columns) != 5:
                # skip this row
                continue
        # for each vehicle type add a count of 1
        for vehicle_type in required_columns:
                # append count of 1 only if the vechile type is not empty
                if vehicle_type:
                        # inserting the ouput to stdout for reducer to act
                        print '%s\t%s' % (vehicle_type, 1)
