from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='sbdlib', # SoBigData Library 
      version='0.0.1',
      author='Alberto Bucci',
      author_email='albertobucci1995@gmail.com',
      description='SoBigData library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/pypa/sampleproject",
      packages=setuptools.find_packages(),
      classifiers=[                                       #???????????
          "Programming Language :: Python :: 3",          #???????????
          "License :: OSI Approved :: MIT License",       #???????????
          "Operating System :: OS Independent",           #???????????
      ],
      python_requires='>=3.6',
      )
