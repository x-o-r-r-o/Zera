from pathlib import Path
from setuptools import setup

CURRENT_DIR = Path(__file__).parent

def get_long_description():
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()

setup(
    name="zera",
    version=1,
    packages=["zera"],
    author="Furkan Onder",
    author_email="furkantahaonder@gmail.com",
    description="static website generator",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="static web generator html markdown",
    url="https://github.com/furkanonder/Zera",
    include_package_data=True,
    entry_points={"console_scripts": ["zera = zera.zera:main"]},
    install_requires=["markdown2", "click"],
)
