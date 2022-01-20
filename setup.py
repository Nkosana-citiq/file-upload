from setuptools import setup, find_packages


setup(name='test_upload',
    version='1.0',
    author='Nkosana Nikani',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'falcon==1.2.0',
        'falcon-cors',
        'falcon-multipart'
    ]
)
