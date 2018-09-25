from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = [
        requirement
        for requirement in f.read().splitlines()
        if requirement and not requirement.startswith('#')
    ]

setup(
    name='ttc_api_scraper',
    version='0.3',
    description="Script to pull data from the TTC's Subway API and store them in a database",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3,<3.7.0',
    entry_points='''
        [console_scripts]
        ttc_api_scraper=ttc_api_scraper:main
        '''
)
