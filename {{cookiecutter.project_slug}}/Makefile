BRANCH	 = main
OWNER  	 = {{cookiecutter.git_owner}}
REPO   	 = {{cookiecutter.git_repo}}

.SILENT: git
.SILENT: venv
.SILENT: packages
.SILENT: show
.SILENT: setup


# Default target.
all:
	echo "Hello $(LOGNAME), nothing to do by default"

setup:
	make venv
	make packages
	make git
	make show

venv:
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry env use python --quiet

{%- if cookiecutter.project_type == "api" %}
packages:
	poetry add uvicorn[standard] --quiet
	poetry add fastapi --quiet
	poetry add sqlmodel --quiet
{%- endif %}

{%- if cookiecutter.project_type == "cli" %}
packages:
	poetry add typer --quiet
	poetry add rich --quiet
{%- endif %}

git:
	git init
	git add .
	git commit -m "first commit"
	git branch -M $(BRANCH)
	git remote add origin git@github.com:$(OWNER)/$(REPO).git
	git push -u origin main

show:
	poetry show
