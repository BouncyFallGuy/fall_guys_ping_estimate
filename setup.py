import sys
from distutils.core import setup

if sys.version_info < (3, 9):
    sys.exit('Python 3.9 or higher is required')

setup(
    name='Fall Guys Ping Extimator',
    version='0.0.1',
    description='Python Distribution Utilities',
    author='@notatallshaw',
    url='https://github.com/notatallshaw/fall_guys_ping_estimate',
    install_requires=[
        'pywin32',
        'psutil'
    ],
)