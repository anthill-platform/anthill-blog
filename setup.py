
from setuptools import setup, find_packages

DEPENDENCIES = [
    "anthill-common"
]

setup(
    name='anthill-blog',
    package_data={
      "anthill.event": ["anthill/blog/sql", "anthill/blog/static"]
    },
    setup_requires=["pypigit-version"],
    git_version="0.1.0",
    description='A service to deliver news and patch notes feed to the users inside the game',
    author='desertkun',
    license='MIT',
    author_email='desertkun@gmail.com',
    url='https://github.com/anthill-platform/anthill-blog',
    namespace_packages=["anthill"],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=DEPENDENCIES
)
