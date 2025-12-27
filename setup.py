from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    This function returns a list of requirements.txt

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace('\n',' ') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='student-performace-prediction',
    version='0.0.1',
    author= 'Sandun Munasinghe',
    author_email='sandunmunasinghe2017@gamil.com',
    packages=find_packages(),
    insatall_requires = get_requirement('requirements.txt')
)
    

                                