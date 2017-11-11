#!/usr/bin/env python # coding: utf-8
from xml.etree.ElementTree import ElementTree
from urllib import urlopen
from re import match

def parse_rss(url):
    """
    RSS 2.0をパース
    """
    rss=ElementTree(file=urlopen(url))
    root=rss.getroot()
    rsslist=[]
    # RSSの要素だけ抜き出す
    for item in [x for x in root.getiterator()
                 if match('.*item$',x.tag)]:
        rssdict={}
        for elem in item.getiterator():
            for k in ['link', 'title', 'description',
                      'auther', 'pubDate']:
                if k in elem.tag:
                    rssdict[k]=elem.text
                else:
                    rssdict[k]=rssdict.get(k, "N/A")
        rsslist.append(rssdict)
    return rsslist
