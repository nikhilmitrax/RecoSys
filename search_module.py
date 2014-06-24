__author__ = 'nikhil'
"""
Wrapper for the pygoogle search module,
 changed to google search_module
Uses get_articles for extracting content from search_list set.
"""
import random_text
import sys
sys.path.insert(0, '../')
from google import search
import content_extractor

default_list = ["site:wikipedia.org", "site:citizendium.org", "site:britannica.com"]
def_size = 1000
def get_wiki_article(search_term, verbose=False, search_list=default_list):
    global def_size
    content_list = []
    if verbose:
        print "Begin Search Algorithm for keyword : ", search_term
    for provider in search_list:
        if provider not in ["random", "combined"]:
            search_url_generator =  search(search_term+" "+provider, stop=1)
            try:
                root_url = search_url_generator.next()
                if verbose:
                    print "Looking at Encyclopedia Article :", root_url
                term = content_extractor.get_content(root_url)
                def_size = len(term['content'])
                if verbose:
                    print term['meta'].encode('utf-8', errors='replace')
                content_list.append(term['content'])
            except:
                content_list.append("-")
        else:
            if provider == "random":
                print "Random Text generation"
                content_list.append(random_text.get_random_text(def_size))
            if provider == "combined":
                print "Merging two previous articles"
                content_list.append(content_list[-1] + content_list[-2])

    return content_list

if __name__ == "__main__":
    print get_wiki_article("Dog", verbose = True)