from distutils.core import setup

setup(
    name='body-extractor-py3',
    version='0.0.1.4',
    packages=['body_extractor'],
    url='https://github.com/xyb930826/html-body-extractor',
    license='MIT License',
    author='supercoderhawk',
    author_email='supercoderhawk@gmail.com',
    description='HTML body content extractor',
    install_requires=[
        "beautifulsoup4 >= 4.5.1",
        "lxml >= 3.6.4",
        "requests >= 2.11.1"
    ]
)
