from render import render
import lxml.etree as et

elmts = [
    {
        'tag': 'tag_name', 'value': 'value', 'attrs': {'attribute1': 'attribute1', 'attribute2': 'attribute2'},
        'nsmap': {'ns1': 'ns1', 'ns2': 'ns2'}
    },
    {'tag': 'another_tag', 'value': [{'tag': 'another_tag_c', 'value': 'value1'}]}
]


def generate():
    # Create the root element
    page = et.Element('RootElement')
    # Create the element tree
    doc = et.ElementTree(page)
    # Call the render method
    render(elmts, page)
    # Open the homemade.xml file on write mode
    file = open('output.xml', 'w')
    # Write the doc content into the file
    doc.write(file, pretty_print=True)
    # Optional import os module to open the file with the default
    # application for the give file extension if there is any
    import os
    os.startfile('output.xml')


generate()
