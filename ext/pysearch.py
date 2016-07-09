#!/usr/bin/env python

# 10/07/2016
# Hades.y2k (github.com/Hadesy2k)
# official.hadesy2k@protonmail.com
# GNU GPL <3.0>

import sys
from google import search


class main:
    """ This class used to search vulnerable website
        by searching on Google with SQLi dork given from user
    """

    def __init__(self):
        print "\nEnter SQLi Dork without 'inurl:'"
        query = raw_input("Dork: ")
        query = "inurl:" + query
        pages = input("Enter number of pages: ")
        print  # printing empty new line
        filename = "sites.txt"  # file will save as 'sites.txt'

        if query != '' and pages != '':
            self.dork(query, pages, filename)

    def dork(self, query, pages, filename):
        print "[+] Googling for %s " % query
        urlList = []

        for url in search(query, stop=pages):
            urlList.append(url)

        if len(urlList) != 0:
            print "Result: %i" % len(urlList)
            output = file(filename, "w")
            for url in urlList:
                output.write(url + "\n")
            output.close()
        else:
            print "No result found"
            sys.exit()

if __name__ == "__main__":
    main()
