zfrom setuptools import setup

setup(
    name='reza',
    version='1.0.3',
    author='Fernando Marcos Wittmann',
    #author_email='fernando.wittmann[at]gmail[dot]com',
    description='A Python tool to rank Google Scholar publications by citations.',
    url='https://github.com/rezanematpour/lbb',
    py_modules=['reza'],  # Assuming your script is named reza.py
    install_requires=[
        # your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'reza=reza:main',  # This line sets up the command line tool
        ],
    },
    ],
    python_requires='>=3.6',
)
