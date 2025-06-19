from setuptools import setup, find_packages

setup(
    name='customprinter',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.4',
    ],
    author='Moaaz Yahia',
    author_email='moaaz.yahia.shrif@gmail.com',
    description='Advanced colored printer for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/customprinter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
