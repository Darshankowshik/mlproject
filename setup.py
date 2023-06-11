from setuptools import find_packages,setup
from typing import List

autorun='-e .'
#-e . will automatically trigger setup.py
#it returns a list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        #read the lines in file using obj(file_obj)
        requirements=file_obj.readlines()
        #in requirements.txt file we read every line and at the end of every line there will be \n we replace these with a blank space
        requirements=[req.replace("\n","") for req in requirements]
        #in requirements -e. will also be added to remove that
        if autorun in requirements:
            requirements.remove(autorun)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Darshan',
author_email='darshankowshik@gmail.com',
#finds all the folder as package with __init__ as its file inside it
package=find_packages(),
install_requires=get_requirements('requirements.txt')


)