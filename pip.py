'''
PIP is a package manager for Python packages, or modules if you like.
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

To use pip function, you must have install pip on your system.

check pip version: pip --version

'''

#Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))