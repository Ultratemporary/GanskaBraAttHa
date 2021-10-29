import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='BraPaketet',
    version='0.0.1',
    author='Erik A',
    author_email='',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ultratemporary/goodtohave',
    project_urls = {
        "Bug Tracker": "https://github.com/Ultratemporary/goodtohave/issues"
    },
    license='MIT',
    packages=['BraPaketet'],
    install_requires=['requests']
)
