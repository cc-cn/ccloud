import xmltodict
with open(xml_f, 'r') as f:
        d = xmltodict.parse(f.read())
        anno = d['annotation']
        width = anno['size']['width']
        height = anno['size']['height']
        objs = anno['object']


#http://blog.csdn.net/shomy_liu/article/details/37929181

import  xml.dom.minidom as xdm
dom = xdm.parse('/home/chencheng/data/deepv_car_person_voc_style/20161230/Annotations/10.209.34.9-0-161212_045923.xml')
root = dom.documentElement
objects = root.getElementsByTagName("object")
num = 0
for node in objects:
	name = node.getElementsByTagName("name")[0]
	type = name.childNodes[0].nodeValue
	print(type)

