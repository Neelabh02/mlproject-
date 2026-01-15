from setuptools import setup, find_packages

setup(
    name='mlproject',
    version='0.0.1',
    author='Neelabh'
    author_email='neelabhtripathi2002@gmail.com'
    packages=find_packages(),
    install_requires=[
        'numpy','pandas','scikit-learn','flask'
    ]
)