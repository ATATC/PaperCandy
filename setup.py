import setuptools

setuptools.setup(
    name="paper-candy",
    version="0.0.1b7",
    author="ATATC",
    author_email="futerry@outlook.com",
    description="A loosely coupled lightweight framework for deep learning papers.",
    license='Apache License 2.0',
    long_description="**PaperCandy** is a loosely coupled lightweight framework for deep learning papers. "
                     "It provides a series of auxiliary tools for rapid rebuilding and writing papers, "
                     "including universal data loader, and automatically generating network structure and "
                     "training process diagram. So far support PyTorch as the only front-end framework.",
    long_description_content_type="text/markdown",
    url="https://github.com/ATATC/PaperCandy",
    packages=setuptools.find_packages(),
    install_requires=["torch", "opencv-python", "matplotlib"],
)
