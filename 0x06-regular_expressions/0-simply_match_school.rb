#!/usr/bin/env ruby

# define the regular expression
regex = /School/

# get the input string from the command line argument
input_string = ARGV[0]

# Use the `=~` operator to match the input string against the regex
if input_string =~ regex
  puts "The input string '#{input_string}' matches the pattern 'School'"
else
  puts "The input string '#{input_string}' does not match the pattern 'School'"
puts ARGV[0].scan(/School/).join
