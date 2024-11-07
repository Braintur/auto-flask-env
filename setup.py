from setuptools import setup, find_packages

setup(
    name='auto-flaskenv',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'auto-flaskenv = auto_flaskenv.main:create_structure',  # Updated module name
        ],
    },
)