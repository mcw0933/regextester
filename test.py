import re
hits = [re.findall(

    r'^  (?: .*$|(?P<code>[a-z0-9]+) +(?P<message>[\w" ]{29}) +(?P<line>\d+))'

    , line)
        for line in open('file.txt')]
print(hits)
