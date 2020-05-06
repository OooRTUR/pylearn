import xml.etree.cElementTree as ET

def parseXML(xml_file):
    pass

def createXML(filename):
    root = ET.Element("data")
    obj1 = ET.SubElement(root, "obj")

    ET.SubElement(root, "field1", name="blah").text = "some value1"
    ET.SubElement(root, "field2", name="aaaa").text = "some value2"
    tree = ET.ElementTree(root)
    tree.write(filename)

if __name__ == "__main__":
    createXML("data.xml")