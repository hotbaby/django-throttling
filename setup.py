
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-throttling-py",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
