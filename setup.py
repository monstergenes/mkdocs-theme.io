from setuptools import setup, find_packages

VERSION = '1.1'


setup(
    name="munstergenes-mkdocs-theme",
    version=VERSION,
    url='https://github.com/munstergenes/munstergenes-mkdocs-theme',
    license='MIT',
    description='dark video background header and sleek',
    author='MONSTERCRYST',
    author_email='https://github.com/monstergenes',
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'mkdocs.themes': [
            'munstergenestheme = munstergenes-mkdocs-theme',
            ]
          },
         zip_safe=False)
