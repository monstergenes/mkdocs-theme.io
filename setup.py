from setuptools import setup, find_packages

VERSION = '1.1'


setup(
    name="monstergenes/mkdocs-theme.io",
    version=VERSION,
    url='https://github.com/monstergenes/mkdocs-theme.io/',
    license='MIT',
    description='dark video background header and sleek',
    author='MONSTERCRYST',
    author_email='munsterkreations@icloud.com',
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'custom_themes': [
            'Home =  main.html',
            'Stylesheet = styles.css',
            ]
        'docs':
            'about = about.md',
            'index = index.html',
          },
         zip_safe=False)
