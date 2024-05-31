from importlib.metadata import entry_points
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PComponentA",
    version="0.0.3",
    author="Ri Shitetsu",
    author_email="/////",
    description="/////",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ri-Shitetsu/Decom",
    project_urls={
        "Bug Tracker": "https://github.com/Ri-Shitetsu/PComponentA",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    py_modules=['decom'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        'console_scripts':[
            'decom = decom:main'
        ]
    },
)




