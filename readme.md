A sample code on how to use [lxml](http://lxml.de) library to generate an xml file.
Example of data, it is a list of dictionary
```python
[
        {
            'tag': 'tag_name', 'value': 'value', 'attrs': {'attribute1': 'attribute1', 'attribute2': 'attribute2'},
            'nsmap': {'ns1': 'ns1', 'ns2': 'ns2'}
        },
        {
            'tag': 'another_tag', 'value': [{'tag': 'another_tag_c', 'value': 'value1'}]
        }
]
```
## Keys meaning:
1. *tag* is the tag name (h1)
2. *value* is the value of the tag
3. *attrs* contain a dictionary of the tag's attributes
4. *nsmap* contain a dictionary of the tag's namespaces