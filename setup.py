import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    reqs = fh.readlines()
    requirements = [e for e in reqs if len(e) > 0]

setuptools.setup(
    name="webhook-test",
    version="0.0.1",
    author="John F Marion",
    author_email="john.f.marion@gmail.com",
    description="A flask server that prints incoming requests, for testing webhooks.",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfmario/webhook-test",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)