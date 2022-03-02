BRANCH	 = main
OWNER  	 = {{cookiecutter.git_owner}}
REPO   	 = {{cookiecutter.git_repo}}

.SILENT: git
.SILENT: venv
.SILENT: packages
.SILENT: packages_data
.SILENT: packages_dev
.SILENT: editor
.SILENT: sphinx
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
	{%- if cookiecutter.use_sphinx == "True" %}
	make sphinx
	{%- endif %}
	{%- if cookiecutter.editor in ("vscode",'atom','sublime') %}
	make editor
	{%- endif %}

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
	git config user.name "FULL_NAME" &> /dev/null
	git config user.email "EMAIL_ADDRESS" &> /dev/null

{% if cookiecutter.use_sphinx == "True" %}
sphinx:
	$(info ** Sphinx Documentation *************)
	poetry add --dev sphinx &> /dev/null
	poetry add --dev sphinx_rtd_theme &> /dev/null
	poetry run sphinx-quickstart --project "{{cookiecutter.project_name}}" --author "FULL_NAME <EMAIL_ADDRESS>" --release 0.0.1 --language en --no-sep --ext-autodoc --ext-todo --ext-viewcode --makefile --no-batchfile docs --quiet
	sed -i '' 's/^# import os/import os/' conf.py &> /dev/null
	sed -i '' 's/^# import sys/import sys/' conf.py &> /dev/null
	sed -i '' 's/^# sys.path.insert(0, os.path.abspath('.'))/sys.path.insert(0, os.path.abspath('..'))/' conf.py &> /dev/null
	sed -i '' 's/alabaster/sphinx_rtd_theme/' conf.py &> /dev/null
{%- endif %}

{% if cookiecutter.editor in ("vscode",'atom','sublime') %}
editor:
{%- if cookiecutter.editor == "vscode" %}
	code .
{%- elif cookiecutter.editor == "atom" %}
	atom .
{%- elif cookiecutter.editor == "sublime" %}
	subl .
{%- endif %}
{%- endif %}
