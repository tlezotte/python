# {{cookiecutter.project_name}}

> A {{cookiecutter.project_type.upper()}} Project

## Init Python Project

```
make init
```

## Project Structure

> Repo Home: https://github.com/{{ cookiecutter.git_owner }}/{{ cookiecutter.git_repo }}

### Installed Packages
{% if cookiecutter.project_type == "api" %}
- [FastAPI](https://fastapi.tiangolo.com)
- [SQLModel](https://sqlmodel.tiangolo.com)
- [uvicorn](https://www.uvicorn.org)
{%- endif %}
{%- if cookiecutter.project_type == "cli" %}
- [Typer](https://typer.tiangolo.com) 
- [rich](https://rich.readthedocs.io)
{%- endif %}
{% if cookiecutter.project_data == "True" %}
- [pandas](https://pandas.pydata.org)
{%- endif %}

### Package Basics

{% if cookiecutter.project_type == "api" %}
#### Uvicorn Server

Run it: `uvicorn main:app --reload`

Homepage: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs
{%- endif %}
