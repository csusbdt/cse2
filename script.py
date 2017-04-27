import platform

if platform.python_version_tuple()[0] < '3':
    print("This script requires Python version 3.")
    exit(1)

from pathlib import Path
import codecs

# Flowcharts
html = '<html><head></head><body><h1>CSUSB CSE Flowcharts</h1><ul>'
for pdf in Path('docs/flowcharts').glob("*.pdf"):
    html += '  <li><a href="' + pdf.stem + '.pdf">' + pdf.stem + '.pdf</li>\n'
html += '</ul></body></html>'
index = 'docs/flowcharts/index.html'
index = codecs.open(index, "w", encoding="utf-8", errors="xmlcharrefreplace")
index.write(html)

print("Done.")

