# this is an instance for computational chemistry, result extraction
# by Yunong Wang, on Apr 12nd, 2019

import os
import re

# execute the regulation
def ContentFilter(src, key) :
	matchSrc = re.search(key, src)
	if matchSrc != None : 
		return matchSrc.group(0)
	else :
		return '(NULL)'

# walk through the directory (DFS)
def DirWalkThrough(scan_dir_path, generate_file_name, pattern_key) :
    fp_out = open(generate_file_name, 'w')
	# walk through
    for iter in os.walk(scan_dir_path) : 
        for jter in iter[2] : 
            if jter.endswith('.out') : 
                try : 
                    filePath = ''
                    if iter[0].endswith('/') : 
                        filePath = iter[0] + jter
                    else : 
                        filePath = iter[0] + '/' + jter
                    fp_in = open(filePath, 'r')
                    # use reg filter
                    szbuf = ContentFilter(fp_in.read(), pattern_key)
                    fp_out.write(filePath + '\n\n' + szbuf + '\n\n')
                    fp_in.close()
                finally : 
                    if fp_in :
                        fp_in.close()
    fp_out.close()

if __name__ == '__main__' :
	# the extract source directory
	esDir = r'./outfiles/'
	# target integrated output data file
	outputFile = r'./outfiles/pattern_out.txt'
	# regular expression for patterns
	reg_key = r'==>[ ]+Energetics([ |\S|\d|\n])+SCF energy([ |\S|\d|\n])+Total CI energy([ |\S|\d|\n])+?\n'
	DirWalkThrough(esDir, outputFile, reg_key)
