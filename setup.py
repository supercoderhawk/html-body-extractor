from distutils.core import setup

setup(
    name='body-extractor-py3',
    version='0.0.1.2',
    packages=['body_extractor'],
    url='https://github.com/xyb930826/html-body-extractor',
    license='MIT License',
    author='supercoderhawk',
    author_email='supercoderhawk@gmail.com',
    description='HTML body content extractor',
    install_requires=[
        "beautifulsoup4 >= 4.5.1",
        "html5lib >= 0.999999999",
        "requests >= 2.11.1"
    ]
)
