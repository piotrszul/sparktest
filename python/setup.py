import os
import re
from setuptools import setup

HERE = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
TEMP_PATH = "target"

in_src = os.path.isfile(os.path.join(ROOT_DIR, "pom.xml"))

if in_src:
    pom_file = os.path.join(ROOT_DIR, 'pom.xml')
    with open(pom_file) as pomf:
        pom = pomf.read()
    version_match = re.search('<version>([\d\.]+)(?:-(\w+))?(?:-([\d]+)-SNAPSHOT)?</version>', pom)
    version = "".join(
        [vc if i != 2 else ".dev%s" % vc for i, vc in enumerate(version_match.groups())])
    print("Version from: %s is: %s" % (pom_file, version))
    print("Writing version file in: %s" % os.path.abspath("."))
    with open("pyrander/version.py", "w") as vf:
        vf.write("__version__='%s'\n" % version)

with open('pyrander/version.py') as vf:
    exec(vf.read())

setup(
    name='pyrander',
    packages=['pyrander'],  # this must be the same as the name above
    version=__version__,
    description='A random test lib',
    author='Piotr Szul',
    author_email='piotr.szul@csiro.au',
    url='https://github.com/piotrszul/pyrander',
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
    classifiers=[],
    extras_require={
        'test': [
            'pyspark==2.1.2',
        ],
        'dev': ['twine'],
    },
    license="MIT",
)
