import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name="wibuapi",
    version="0.0.6",
    description="Official Python Wrapper for Wibu API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    author="Yoga Pranata",
    author_email="yoga@zyxdevs.eu.org",
    url="https://github.com/zYxDevs/wibu-api-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires=">=3.6",
)
