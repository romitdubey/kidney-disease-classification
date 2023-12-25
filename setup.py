import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "kidney-disease-classification"
AUTHOR_USER_NAME = "romitdubey"
SRC_REPO = "src\cnnClassifier"
AUTHOR_EMAIL = "romitdubey1@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN App",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src")   
)