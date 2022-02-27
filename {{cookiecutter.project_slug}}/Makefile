BRANCH	 = main
OWNER  	 = {{cookiecutter.git_owner}}
REPO   	 = {{cookiecutter.git_repo}}

.SILENT: git
.SILENT: venv
.SILENT: packages
.SILENT: packages_data
.SILENT: packages_dev
.SILENT: editor
.SILENT: init


# Default target.
all:
	echo "Hello $(LOGNAME), nothing to do by default"

init:
	make venv
	make packages
	make packages_dev
	{%- if cookiecutter.project_data == "True" %}
	make packages_data
	{%- endif %}
	make git
	make editor

venv:
	$(info ** Creating VENV ********************)
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry env use python --quiet

{% if cookiecutter.project_type == "api" %}
packages:
	$(info ** Installing API Software **********)
	poetry add uvicorn[standard] &> /dev/null
	poetry add fastapi &> /dev/null
	poetry add sqlmodel &> /dev/null
{%- endif %}

{%- if cookiecutter.project_type == "cli" %}
packages:
	$(info ** Installing CLI Software **********)
	poetry add typer &> /dev/null
	poetry add rich &> /dev/null
{%- endif %}

{% if cookiecutter.project_data == "True" %}
packages_data:
	$(info ** Installing Data Software *********)
	poetry add pandas &> /dev/null
{%- endif %}

packages_dev:
	poetry add --dev black &> /dev/null
	poetry add --dev pytest &> /dev/null
	poetry add --dev autopep8 &> /dev/null
	poetry add --dev ipykernel &> /dev/null

git:
	$(info ** Initiate Git Repo ****************)
	git init &> /dev/null
	git add . &> /dev/null
	git commit -m "first commit" &> /dev/null
	git branch -M $(BRANCH) &> /dev/null
	git remote add origin git@github.com:$(OWNER)/$(REPO).git &> /dev/null

editor:
	echo
{%- if cookiecutter.editor == "vscode" %}
	code .
{%- endif %}
{%- if cookiecutter.editor == "atom" %}
	atom .
{%- endif %}
{%- if cookiecutter.editor == "sublime" %}
	subl .
{%- endif %}
