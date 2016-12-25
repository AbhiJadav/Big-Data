#!/usr/bin/env python
import sys

prev_key          = "  "                #initialize previous word  to blank string

line_cnt           = 0  #count input lines
viewer_cnt         = 0  #count viewers
abc_found          = False #boolean to check if we have reached channel ABC or not

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    #note: for simple debugging use print statements, ie:  
    key_in  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if key_in != prev_key and line_cnt>1:
        if abc_found == True:
	    print('{0}\t{1}'.format(prev_key,viewer_cnt))
	prev_key = key_in
	viewer_cnt = 0
	abc_found=False
	if value_in == "ABC":
	    abc_found = True
	else:
	    viewer_cnt = viewer_cnt + int(value_in)
    else:
	if value_in == "ABC":
	    abc_found = True
	else:
	    viewer_cnt = viewer_cnt + int(value_in)

if prev_key == key_in:
    print '%s\t%s' % (key_in, viewer_cnt)
