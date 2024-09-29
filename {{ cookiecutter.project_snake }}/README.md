# {{ cookiecutter.project_name }}

- rename template.secrets.toml to .secrets.toml
- pipenv install --dev
- pipenv run pytest
- pipenv run black src/{{ cookiecutter.project_snake }}
- pipenv run {{ cookiecutter.cli_entrypoint }} --help
