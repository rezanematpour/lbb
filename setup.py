zfrom setuptools import setup

setup(
    name='reza',
    version='1.0.3',
    author='Fernando Marcos Wittmann',
    #author_email='fernando.wittmann[at]gmail[dot]com',
    description='A Python tool to rank Google Scholar publications by citations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
