﻿from setuptools import setup, find_packages

setup(
    name="MOBiceps",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'joblib==1.2.0',
	'numpy==1.21.6',
	'pandas==1.4.1',
	'seaborn==0.11.2',
	'yellowbrick==1.5',
	'scikit-learn==1.2.1',
	'scipy==1.8.1',
	'scikit-image==0.19.2',
	'matplotlib==3.5.1',
	'shap==0.41.0',
	'xgboost==1.6.2',
	'tqdm==4.63.0',
	'pyopenms==2.7.0',
	'numba==0.55.1',
	'torch==1.13.1',
	'torchvision==0.14.1',
	'torchaudio==0.13.1',
	'statsmodels==0.13.2'],
    author='Jens Settelmeier',
    author_email='jenssettelmeier@googlemail.com',
    description='Python tools for Mass Spectrometry and Omics data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/JensSettelmeier/MOBiceps',  
    classifiers=[
	"License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
)