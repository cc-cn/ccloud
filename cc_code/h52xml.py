import h5py
import sys
from xml.dom import minidom


def h52xml(anno_file, key, h, w, c, xml_file):
	impl = minidom.getDOMImplementation()
	dom = impl.createDocument(None, 'annotation', None)
	root = dom.documentElement

	img_size = dom.createElement('size')
	img_width = dom.createElement('width')
	img_width.appendChild(dom.createTextNode(str(w)))
	img_size.appendChild(img_width)

	img_height = dom.createElement('height')
	img_height.appendChild(dom.createTextNode(str(h)))
	img_size.appendChild(img_height)

	img_depth = dom.createElement('depth')
	img_depth.appendChild(dom.createTextNode(str(c)))
	img_size.appendChild(img_depth)
	root.appendChild(img_size)

	with h5py.File(anno_file, 'r') as f:
		a = []
		if key in f.keys():
			a = f[key][:]
		if len(a) != 0 and a.size != 0:
			for lst in a:
				xmin = lst[0]
				ymin = lst[1]
				xmax = lst[0] + lst[2]
				ymax = lst[1] + lst[3]
				label = key

				obj = dom.createElement('object')
				root.appendChild(obj)

				name = dom.createElement('name')
				name.appendChild(dom.createTextNode(label))
				obj.appendChild(name)

				difficult = dom.createElement('difficult')
				difficult.appendChild(dom.createTextNode('0'))
				obj.appendChild(difficult)

				bndbox = dom.createElement('bndbox')
				obj.appendChild(bndbox)
				bbxmin = dom.createElement('xmin')
				bbxmin.appendChild(dom.createTextNode(str(xmin)))
				bndbox.appendChild(bbxmin)
				bbymin = dom.createElement('ymin')
				bbymin.appendChild(dom.createTextNode(str(ymin)))
				bndbox.appendChild(bbymin)
				bbxmax = dom.createElement('xmax')
				bbxmax.appendChild(dom.createTextNode(str(xmax)))
				bndbox.appendChild(bbxmax)
				bbymax = dom.createElement('ymax')
				bbymax.appendChild(dom.createTextNode(str(ymax)))
				bndbox.appendChild(bbymax)

	xml_f = open(xml_file, 'w')
	dom.writexml(xml_f, addindent='\t', newl='\n')
	xml_f.close()
	return dom


if __name__ == '__main__':
	annofile = sys.argv[1]
	key = sys.argv[2]
	h = sys.argv[3]
	w = sys.argv[4]
	xmlfile = sys.argv[5]
	c = 3
	h52xml(annofile, key, h, w, c, xmlfile)
