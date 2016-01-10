from setuptools import setup, find_packages

setup(
    name="spinner",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="Taff Gao",
    author_email="gaotongfei1995@gmail.com",
    install_requires=[
        "args==0.1.0",
        "clint==0.5.1",
        "wheel==0.24.0"
    ],
    entry_points='''
    [console_scripts]
    spinner=spinner.cli:main
    '''
)
