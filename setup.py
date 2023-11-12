from setuptools import setup, find_packages

setup(
    name='csv_data_extractor',
    version='1.0.0',
    author='Mohammad Jaqmaqji',
    author_email='mohjak@gmail.com',
    description='A package for extracting and processing data from CSV files based on specific criteria',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mohjak/csv_data_extractor',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add any additional package dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # Adjust the license as per your choice
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    keywords='csv processing data-extraction',
)
