from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a requirements.txt file.
    It also removes '-e .' if present.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters and remove extra spaces
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' from requirements if it's present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="ml-project",
    version="0.0.1",
    author="Aamil Abd",
    author_email="aamilabdulla123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
