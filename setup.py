""""""

__author__ = 'Qunfei Wu'
__version__ = '0.1'
__date__ = '14/12/14'
__copyright__ = """Copyright (c) 2014 Qunfei Wu"""

from distutils.core import setup

setup(
    name='easyroman',
    py_modules=["easyroman"],
    version='0.1',
    package_dir={"": "src"},
    url='https://github.com/wuqunfei/easyroman',
    license='Apache Licence 2.0',
    author='Qunfei Wu',
    author_email='wu.qunfei@gmail.com',
    description='A easy Integer into Roman numerals converter',
    test_suite='unitests',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Operating System :: OS Independent'
    ]

)
