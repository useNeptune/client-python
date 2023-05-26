from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'A Python client for withgraham.io'
LONG_DESCRIPTION = 'A Python client for withgraham.io'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="graham-client", 
        version=VERSION,
        author="WithGraham",
        author_email="support@withgraham.io",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'requests >= 2.31.0',
            'ratelimiter >= 1.2.0.post0'
        ],
        keywords=['python', 'financial', 'data', 'api', 'withgraham', 'graham', 'value investing'],
        classifiers= []
)