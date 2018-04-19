from lxml import etree as et


def render(elements, parent):
    """
    :param elements: dict
    ex. [
        {
            'tag': 'tag_name', 'value': 'value', 'attrs': {'attribute1': 'attribute1', 'attribute2': 'attribute2'},
            'nsmap': {'ns1': 'ns1', 'ns2': 'ns2'}
        },
        {
            'tag': 'another_tag', 'value': [{'tag': 'another_tag_c', 'value': 'value1'}]
        }
        ]
    :param parent:
    :return:
    """
    for elt in elements:

        tag = elt['tag']
        value = elt['value']
        attrs = elt.get('attrs')
        nsmap = elt.get('nsmap')

        sub_elt = et.SubElement(parent, tag, attrib=attrs, nsmap=nsmap)
        if isinstance(value, str):
            print value
            if value not in ('', 'False'):
                sub_elt.text = value
        else:
            render(value, sub_elt)
