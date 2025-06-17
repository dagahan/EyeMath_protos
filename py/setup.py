from setuptools import setup, find_packages

setup(
    name='eyemath_protos',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['grpcio>=1.0'],
    package_data={
        'eyemath_protos': ['**/*.pyi'],
    },
)