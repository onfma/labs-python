# The build_xml_element function receives the following parameters: 
# tag, content, and key-value elements given as name-parameters. 
# Build and return a string that represents the corresponding XML element. 
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", 
# _class =" my-link ", id= " someid ") returns  the string = "<a href=\"http://python.org \ 
# "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, **kwargs):
    # Construct the opening tag with attributes
    attributes = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()])
    opening_tag = f"<{tag} {attributes}>" if attributes else f"<{tag}>"
    
    # Construct the closing tag
    closing_tag = f"</{tag}>"
    
    # Combine the opening tag, content, and closing tag to form the XML element
    xml_element = f"{opening_tag}{content}{closing_tag}"
    
    return xml_element

# Example usage:
tag = "a"
content = "Hello there"
attributes = {
    "href": "http://python.org",
    "_class": "my-link",
    "id": "someid"
}
result = build_xml_element(tag, content, **attributes)

print(result)
