from setuptools import setup, find_packages

setup(
    name="muscrape",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.
        "pytube==15.0.0",
        "pydantic==2.4.2",
        "PyYAML==6.0.1",
        "python-dotenv==1.0.0",
        "pandas==2.1.1",
        "loguru==0.7.2",
        "kaggle==1.5.16",
    ],
    author="Aditya Karnam",
    author_email="akarnam37@gmail.com",
    description="A project to scrape music from youtube",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/metaquantz/muscrape",
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
