import setuptools

with open("README.md") as rm:
    desc = rm.read()

setuptools.setup(
    name="KtpReader",
    version="1.0",
    author="Robet Atiq Maulana Rifqi",
    author_email="blank345red@gmail.com",
    description="Read your ktp data",
    long_description="this package can read your ktp data from, name, photo, NIK, address etc.",
    long_description_content_type="text/markdown",
    url="https://github.com/nothing2512/KtpReader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MITLicense",
        "Operating System :: OS Independent"
    ]
)