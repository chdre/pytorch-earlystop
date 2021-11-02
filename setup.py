import setuptools

with open('README.md', 'r') as infile:
    long_description = infile.read()

setuptools.setup(
    name='torch_earlystop',
    version='0.1.1',
    author='Christer Dreierstad',
    author_email='christerdr@outlook.com',
    description='Package for early stopping for Pytorch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chdre/pytorch-earlystopping',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['torch'],
    include_package_data=True,
)
