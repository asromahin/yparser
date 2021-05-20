import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yparser",
    version="0.1",
    author="asromahin",
    author_email="asromahin@mail.ru",
    description="Use for grab images from Yandex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asromahin/yparser",
    #package_dir={"": "yparser"},
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    python_requires='>=3.6',
)
