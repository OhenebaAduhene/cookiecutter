from setuptools import setup
setup(
    name="whichcraft",
    version="0.6.0",
    description="""This package provides cross-platform cross-python shutil.which functionality.""",
    # long_description=readme + "\n\n" + history,
    author="Daniel Roy Greenfeld",
    author_email="pydanny@gmail.com",
    url="https://github.com/pydanny/whichcraft",
    include_package_data=True,
    # py_modules=["whichcraft"],
    packages=["whichcraft"],
    license="BSD",
    zip_safe=False,
    keywords="whichcraft",
)
