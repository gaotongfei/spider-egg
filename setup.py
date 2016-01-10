from setuptools import setup, find_packages

setup(
    name="spider-egg",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="Taff Gao",
    description="a template for python crawler with requests and beautifulsoup",
    author_email="gaotongfei1995@gmail.com",
    url="https://github.com/gaotongfei/spider-egg",
    install_requires=[
        "args==0.1.0",
        "clint==0.5.1",
        "wheel==0.24.0"
    ],
    entry_points='''
    [console_scripts]
    spider_egg=spider_egg.cli:main
    '''
)
