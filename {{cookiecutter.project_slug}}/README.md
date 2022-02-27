# {{cookiecutter.project_name}}

> A {{cookiecutter.project_type.upper()}} Project

## Init Python Project

```
make init
```

## Project Structure

> Repo Home: https://github.com:$(OWNER)/$(REPO).git

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
#### uvicorn server

Run it: `uvicorn main:app --reload`

Homepage: http://127.0.0.1:8000

Documentation: http://127.0.0.1:8000/docs
{%- endif %}
