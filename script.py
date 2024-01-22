import xml.etree.ElementTree as ET
tree = ET.parse("teste.xml")

root = tree.getroot()

print(root.tag)

for child in root:
    print(child.tag, child.attrib)


