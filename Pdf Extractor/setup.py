from setuptools import setup, find_packages

setup(
    name='pdf-reader-streamlit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2==1.26.0',
        'spacy==3.0.6',
        'transformers==4.11.3',
        'streamlit==1.5.0'
    ],
    entry_points={
        'console_scripts': [
            'pdf-reader = your_module_name:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

