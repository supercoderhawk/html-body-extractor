# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

class BodyExtractor():
    def __init__(self,html):
        self.html = html
        self.content = ''
        self.THRESHOLD = 50  # 骤升点阈值


    def _preprocess(self):
        regex = re.compile(
            r'(?:<!DOCTYPE.*?>)|'  # doctype
            r'(?:<head[\S\s]*?>[\S\s]*?</head>)|'
            r'(?:<!--[\S\s]*?-->)|'  # comment
            r'(?:<script[\S\s]*?>[\S\s]*?</script>)|'  # js...
            r'(?:<style[\S\s]*?>[\S\s]*?</style>)', re.IGNORECASE)  # css
        filteredHtml = regex.sub('', self.html.decode('utf-8'))
        soup = BeautifulSoup(filteredHtml, 'html5lib')

    def _start(self):
        pass

    def _end(self):
        pass