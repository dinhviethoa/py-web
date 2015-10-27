import setuptools


setuptools.setup(
    version="0.0.1",
    license='mit',
    name='py-web',
    author='nathan todd-stone',
    author_email='me@nathants.com',
    url='http://github.com/nathants/py-web',
    packages=['web'],
    install_requires=['tornado==4.1',
                      'mock==1.0.1'],
    description='a minimal, data centric web library'
)
