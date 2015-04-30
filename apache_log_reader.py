# -*- coding: utf-8 -*-
# !/usr/bin/python
# Converting Apache's log access files into csv file.
# Matheus Cesario <mts.cesario@gmail.com>

# A typical configuration for the access log might look as follows.
# LogFormat "%h %l %u %t \"%r\" %>s %b" common
# CustomLog logs/access_log common

# Available parameters
# --input DIR: defines the apache log file path
# --output DIR: defines the output file path
# --format OPT: log format to be translated. Accepts 'common', 'combined'.
#   If empty, default for 'common' log.
# --convert OPT: file type for conversion. Accepts 'csv'
#   If empty, default for 'csv'

import sys

# Variables
available_parameters = ['--input', '--output', '--format']
input_dir = "/var/log/apache2/access.log"
output_dir = "access.csv"
format_option = "common"

# Defining parameters
for i in range(1, len(sys.argv)):

    # Getting argument
    arg = sys.argv[i]

    # Getting parameter's values
    if arg == '--input':
        i += 1
        input_dir = sys.argv[i]
    elif arg == '--output':
        i += 1
        output_dir = sys.argv[i]
    elif arg == '--format':
        i += 1
        format_option = sys.argv[i]

# Displaying options
print("""
    Defined parameters:
    input:  %s
    output: %s
    format: %s
""" % (input_dir, output_dir, format_option))

# Opening input_dir
input_file = open(input_dir, 'r')

# Choosing format mode (pattern)
p = '([^\s]+)\s([^\s]+)\s([^\s]+)\s\[(.*)\]\s\"(.*)\"\s([0-9]*)\s([0-9]*)'

# Other formats
# if format_option == 'combined':

# for line in input_file:
#    print(line.encode("utf-8"))
