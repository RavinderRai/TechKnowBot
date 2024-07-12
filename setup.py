import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "TechKnowBot"
AUTHOR_USER_NAME = "RavinderRai"
SRC_REPO = "tech_know_bot"
AUTHOR_EMAIL = "ravi.b.rai@outlook.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A micro-SaaS meant to be an analytics chatbot to help in product puchasing decision making.",
    long_description=long_description,
    long_description_context="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.10'
)