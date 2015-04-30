# log-apache-reader
Converting Apache's log access files into another format.

My first Python project :-)

Python script that converts an Apache log file into another format.

Available parameters
--input DIR: defines the apache log file path
--output DIR: defines the output file path
--format OPT: log format to be translated. Accepts 'common', 'combined'.
  If empty, default for 'common' log.
--convert OPT: file type for conversion. Accepts 'csv'
  If empty, default for 'csv'
