from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_snake }}",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "{{ cookiecutter.cli_entrypoint }}={{ cookiecutter.project_snake }}.cli:cli",
        ],
    }
)
