from setuptools import setup, find_packages

setup(
    name="vanq",
    version="0.1.7",
    py_modules=["main"],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "click==8.1.4",
        "transformers==4.30.2",
        "torch==2.0.1",
        "setuptools==68.0.0",
    ],
    entry_points={"console_scripts": ["vanq = main:main"]},
)
