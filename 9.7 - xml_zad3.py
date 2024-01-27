from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())
# <?xml version="1.0" ?><znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x1046f69f0>]
print(cNodes[0])  # <DOM Element: znajomi at 0x104d5a9f0>
znajomi = cNodes[0]
print(znajomi.getElementsByTagName("osoba"))
persons = znajomi.getElementsByTagName("osoba")
# [<DOM Element: osoba at 0x1048d2b10>, <DOM Element: osoba at 0x1048d2cc0>]
print(persons[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(persons[1].toxml())
# <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
