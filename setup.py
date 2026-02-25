from setuptools import find_packages, setup

cnst = '-e .'

def get_requirements(file_path: str):
    requirements = []

    with open(file_path) as file_object:
        requirements = file_object.readlines()

    requirements = [req.replace("\n", "") for req in requirements]
    
    if cnst in requirements:
        requirements.remove(cnst)
    return requirements


setup(
    name = 'mlproject',
    verison = '0.0.1',
    author = 'Lalit',
    author_email = 'mail4lalitchandra@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)