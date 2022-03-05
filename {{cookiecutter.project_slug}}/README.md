# {{cookiecutter.project_name}}

{% if cookiecutter.project_type == "api" %}
> An {{cookiecutter.project_type.upper()}} Python Project
{%- else %}
> A {{cookiecutter.project_type.upper()}} Python Project
{%- endif %}

## Project Structure

- Repo Home: https://github.com/{{ cookiecutter.git_owner }}/{{ cookiecutter.git_repo }}

### Project Applications

#### [Poetry](https://python-poetry.org)

> Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

- Uses Virtualenv: `{{cookiecutter.project_slug}}/.venv`

### Installed Packages
{% if cookiecutter.project_type == "api" %}
#### [FastAPI](https://fastapi.tiangolo.com)

> FastAPI framework, high performance, easy to learn, fast to code, ready for production

#### [SQLModel](https://sqlmodel.tiangolo.com)

> SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.

#### [uvicorn](https://www.uvicorn.org)  [:blue_book:](#uvicorn-server)

> Uvicorn is an ASGI web server implementation for Python.

{%- endif %}
{%- if cookiecutter.project_type == "cli" %}
#### [Typer](https://typer.tiangolo.com)

> Typer, build great CLIs. Easy to code. Based on Python type hints.

#### [rich](https://rich.readthedocs.io)

> Rich is a Python library for writing rich text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax highlighted code.

{%- endif %}
{% if cookiecutter.use_pandas == "True" %}
#### [pandas](https://pandas.pydata.org)

> pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
{%- endif %}

{% if cookiecutter.project_type in ("api") %}
### Package Basics

{% if cookiecutter.project_type == "api" %}
#### Uvicorn Server

Run it: `uvicorn main:app --reload`

Homepage: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs
{%- endif %}
{%- endif %}

{%- if cookiecutter.use_sphinx == "True" %}
## Sphinx Documentation

>Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.

### Generate Docs

```
cd docs
poetry run sphinx-apidoc -o . ..
```

### Convert Docs to HTML

```
poetry run make html
open _build/html/index.html
```
{%- endif %}
