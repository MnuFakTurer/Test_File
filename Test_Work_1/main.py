with open('README.md', 'w') as file:
    text_write = (
    "\n Todo-List:"
    "\n # - "
    "\n # - ")
    file.write(text_write)

with open('README.md') as file:
    content = file.read()
    print(content)