#!/usr/bin/env python3
html_body="""
<html><body>
foo= %s
</body></html>
"""
import cgi
form=cgi.FieldStorage()
foo=form.getvalue("foo", "N/A")
print("Content-type: text/html\n")
print(html_body % foo)
