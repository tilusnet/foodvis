#!/usr/bin/python

fr = open('countries.csv','r')
fw = open('c2.csv','w')

for line in fr:
	txt = line.strip('\n')
	fw.write(txt + ",#DD7777\n")

fr.close
fw.close
