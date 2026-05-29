from setuptools import setup, find_packages

setup(
    name="file-watcher-pro-security-20260527_052909",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'file=file:main',
        ],
    },
)