#local package installation logic present here
import setuptools

with open("README.md", "r", encoding="utf-8") as f:# to publish this project as package we need to read the README.md file using pypi package
    long_description = f.read()


__version__ = "0.0.0" #intial version number 

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "apoorvsinghnegi"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "apoorvsinghnegi18@gmail.com"


#look for constructor file in every folder and install it. __init__.py and install as local package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
