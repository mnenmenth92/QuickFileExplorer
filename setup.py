import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QuickFileExplorer-pkg-mnenmenth92",
    version="0.0.1",
    author="Maciej Such",
    author_email="msuch92@gmail.com",
    description="Console file explorer for windows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Win32 (MS Windows)",
    ],
    python_requires='>=3.8',
)