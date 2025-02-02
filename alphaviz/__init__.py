#!python

__project__ = "alphaviz"
__version__ = "1.1.15"
__license__ = "Apache"
__description__ = "A interactive Dashboard to explore mass spectrometry data."
__author__ = "Eugenia Voytik"
__author_email__ = "opensource@alphapept.com"
__github__ = "https://github.com/MannLabs/alphaviz"
__keywords__ = [
    "ms",
    "mass spectrometry",
    "bruker",
    "timsTOF",
    "proteomics",
    "bioinformatics",
    "visualization"
]
__python_version__ = ">=3.8,<3.9"
__classifiers__ = [
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive"
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
]
__console_scripts__ = [
    "alphaviz=alphaviz.cli:run",
]
__urls__ = {
    "Mann Labs at MPIB": "https://www.biochem.mpg.de/mann",
    "GitHub:": __github__,
    # "ReadTheDocs": "https://alphaviz.readthedocs.io/en/latest/",
    # "PyPi": "https://pypi.org/project/alphaviz/",
    # "Scientific paper": "",
}
__extra_requirements__ = {
    "development": "requirements_development.txt",
    "gui": "requirements_gui.txt"
}
__requirements_style__ = None
