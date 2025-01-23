from typing import List
from setuptools import setup, find_packages

def get_requirement_text(file_path:str)-> List[str]:
    hyphen = "-e ."
    requirement = []
    with open(file_path, 'r') as file:
        file  = file.readline()
        requirement = [req.replace("/n"," ")for req in requirement]

        if hyphen in requirement:
            requirement.remove(hyphen)
    return requirement




setup(
    name= 'Project_3',
    version = '0.1',
    author = 'Pratham',
    author_email = 'prathamvichare645@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement_text('req.txt'),

)