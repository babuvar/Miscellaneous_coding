from __future__ import print_function

import httplib, urllib, re, json


class NgramScraper(object):
    """
    Web scraper that queries Google's Ngram Viewer for the given word,
    and the scrapes out the frequencies.
    """

    def __init__(self):
        self._year_start = 2014
        self._year_end = 2015
        self._regexp = re.compile('var data = (.+?);')

    @property
    def year_start(self):
        return self._year_start

    @property
    def year_end(self):
        return self._year_end

    @year_start.setter
    def year_start(self, start):
        self._year_start = start

    @year_end.setter
    def year_end(self, end):
        self._year_end = end

    def query(self, ngram):
        # Build the request url
        url = '/ngrams/graph?content='
        url = url + urllib.quote_plus(ngram)
        url = url + '&year_start=' + str(self._year_start)
        url = url + '&year_end=' + str(self._year_end)
        url = url + '&direct_url=' + urllib.quote_plus('t1;,' + ngram + ';,c0')
        conn = httplib.HTTPSConnection('books.google.com')
        conn.request('GET', url)
        resp = conn.getresponse()
        html = resp.read()
        if "ngrams.data = []" in html:
            return 0
        else:
            match = self._regexp.search(html)
            before, key, after = html.partition("timeseries\": [")
            before2, key2, after2 = after.partition("]}];")
            before2 = list(before2.split(", "))
            return before2[0]

    def query_most_recent_freq(self, ngram):
        data = self.query(ngram)
        return data['timeseries'][-1] if data else None

if __name__ == '__main__':
    import json
    import sys
    s = NgramScraper()
    result = s.query("self-reliant")
    print(result)







