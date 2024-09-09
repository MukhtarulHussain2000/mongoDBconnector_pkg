from setuptools import setup, find_packages
from typing import List

def parse_requirements(filename:str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "mongoDBconnector_pkg"
PKG_NAME= "databaseConnector2000"
AUTHOR_USER_NAME = "MukhtarulHussain2000"
AUTHOR_EMAIL = "mukhtarulhussainofficial@gmail.com"

setup(
     name=PKG_NAME,
     version=__version__,
     author=AUTHOR_USER_NAME,
     author_email=AUTHOR_EMAIL,
     description="A python package for connecting with database.",
     long_description=long_description,
     long_description_content="text/markdown",
     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
     project_urls={
          "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
     },
     package_dir={"": "src"},
     packages=find_packages(where="src"),
     install_requires=parse_requirements('requirements.txt')
)



