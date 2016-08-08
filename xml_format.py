import lxml.etree as etree

x = etree.parse("response.xml")
print etree.tostring(x, pretty_print = True)