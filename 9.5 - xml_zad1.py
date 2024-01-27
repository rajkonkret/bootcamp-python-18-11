# Pliki xml, język tagów
# <note>
# <to>Tove</to>
# <from>Jani</from>
# <heading>Reminder</heading>
# <body>Don't forget me this weekend!</body>
# </note>
from xml.dom import minidom

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)  # <root></root>

productChild = root.createElement('product')
# <product></product>
productChild.setAttribute('name', 'Geeks-for-Geeks')
# <product name="Geeks-for-Geeks"/>
# dodajemy ten tag do dokumentu
xml.appendChild(productChild)
print(root)  # <xml.dom.minidom.Document object at 0x104597a70>
xml_str = root.toprettyxml()  # zamieniamy na strinfg odpowiadający xml

print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Geeks-for-Geeks"/>
# </root>
save_path = 'gfg.xml'

with open(save_path, "w") as f:
    f.write(xml_str)
