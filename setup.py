from setuptools import find_packages, setup
from typing import List

Hyphen_E_Dot = "-e ."
def get_requirements(file_path):
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if Hyphen_E_Dot in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="ML-Project-1",
    version="0.0.1",
    author="Krish",
    author_email="krishkothari36@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)