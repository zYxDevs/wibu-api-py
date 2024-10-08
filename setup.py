import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name="wibuapi",
    version="0.1.8",
    description="Official Sync and Async Python Wrapper for Wibu API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Yoga Pranata",
    author_email="yoga@zyxdevs.eu.org",
    url="https://wibu-api.eu.org",
    packages=setuptools.find_packages(),
    keywords=[
        "wibu",
        "weebs",
        "otaku",
        "anime",
        "hentai",
        "donghua",
        "manga",
        "doujin",
        "manhwa",
        "manhua",
        "jdrama",
        "jav",
        "music",
        "novel",
        "api",
        "ip",
        "terabox",
        "lyrics",
        "booru",
        "sfw",
        "nsfw",
        "scraper",
        "bypasser",
        "genshin",
        "facebook",
        "youtube",
    ],
    project_urls={
        "Source": "https://github.com/zYxDevs/wibu-api-py",
        "Funding": "https://github.com/sponsors/zYxDevs",
        "Documentation": "https://wibu-api.eu.org/redoc",
        "Bug Tracker": "https://github.com/zYxDevs/wibu-api-py/issues",
        "Changelog": "https://github.com/zYxDevs/wibu-api-py/releases",
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    install_requires=["requests", "aiohttp"],
    python_requires=">=3.8",
)
