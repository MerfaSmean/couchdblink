from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="couchdblink",
    version="0.0.2",
    description="A thin layer of abstraction for linking python projects to data in CouchDB servers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MerfaSmean/couchdblink",
    download_url="https://github.com/MerfaSmean/couchdblink/archive/refs/heads/main.zip",
    author="Samuel Freeman",
    author_email="soundmaking@merfasmean.com",
    license="MIT",
    #packages=["couchdblink"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pycouchdb"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 2 - Pre-Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.7",
    ],
)

# cite reference: https://gist.github.com/ustropo/98d5d32dc506315f6c2c792b87bb985b#file-setup-py
