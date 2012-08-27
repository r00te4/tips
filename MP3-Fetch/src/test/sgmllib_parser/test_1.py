#!/usr/bin/env python
from sgmllib import SGMLParser
s = """
     <html>
         <head>what's in</head>
         <td> hello 
             <td> table1 blahblah </td>
             <td> table </td>
         </td>
         ok the end blah
     </html>
"""
class Parse(SGMLParser):
    def reset(self):
        self.found_td = 0
        SGMLParser.reset(self)
    def start_td(self, attrs):
        self.found_td += 1
    def end_td(self):
        self.found_td -= 1
    def handle_data(self, text):
        if self.found_td > 0:
            print 'Data: %s' % text

p = Parse()
p.feed(s)
