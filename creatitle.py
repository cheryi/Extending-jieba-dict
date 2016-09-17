#for establishing extra dict
# -*- coding: utf-8 -*-
import sys
import operator

from operator import itemgetter


file = open('titles', 'r')

out = open('extra_dict.txt','w')

for line in file.readlines():
        token = line.split()
        if(len(token)>=4):
                #print token[3].rstrip('/">').lstrip('title=/"')+" nz"
                str=token[3].lstrip('title=\"')
                str=str.rstrip('\">')
                out.write(str+" nz"+'\n')


file.close()

out.close()
