BRANCH	 = main
OWNER  	 = {{cookiecutter.git_owner}}
REPO   	 = {{cookiecutter.project_slug}}
SPCONF   = docs/conf.py

.SILENT: git
.SILENT: poetry
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
	make poetry
	make packages
	make packages_dev
	{%- if cookiecutter.use_pandas == "True" %}
	make packages_data
	{%- endif %}
	{%- if cookiecutter.use_sphinx == "True" %}
	make sphinx
	{%- endif %}
	make git
	{%- if cookiecutter.editor in ("vscode",'atom','sublime') %}
	make editor
	{%- endif %}

poetry:
	$(info ** Initiate Poetry ******************)
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry init --name {{cookiecutter.project_slug}} --description "{{cookiecutter.project_name}}" --author "{{cookiecutter.full_name}} <{{cookiecutter.email_address}}>" --python {{cookiecutter.min_python_version}} --no-interaction --quiet
	mkdir {{cookiecutter.project_slug}}
	printf "__version__ = '{{cookiecutter.project_version}}'" > {{cookiecutter.project_slug}}/__init__.py
	mkdir tests
	touch tests/__init__.py
	printf "from {{cookiecutter.project_slug}} import __version__\n\ndef test_version():\n    assert __version__ == '{{cookiecutter.project_version}}'" > tests/test_version.py
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

{% if cookiecutter.use_pandas == "True" %}
packages_data:
	$(info ** Installing Data Software *********)
	poetry add pandas &> /dev/null
{%- endif %}

packages_dev:
	poetry add --dev black &> /dev/null
	poetry add --dev pytest &> /dev/null
	poetry add --dev autopep8 &> /dev/null
	poetry add --dev ipykernel &> /dev/null

{% if cookiecutter.use_sphinx == "True" %}
sphinx:
	$(info ** Sphinx Documentation *************)
	poetry add --dev sphinx &> /dev/null
	poetry add --dev sphinx_rtd_theme &> /dev/null
	poetry run sphinx-quickstart --project "{{cookiecutter.project_name}}" --author "{{cookiecutter.full_name}} <{{cookiecutter.email_address}}>" --release {{cookiecutter.project_version}} --language en --no-sep --ext-autodoc --ext-todo --ext-viewcode --makefile --no-batchfile docs &> /dev/null
	sed -i '' 's/^# import os/import os/' $(SPCONF) &> /dev/null
	sed -i '' 's/^# import sys/import sys/' $(SPCONF) &> /dev/null
	sed -i '' "s/^# sys.path.insert(0, os.path.abspath('.'))/sys.path.insert(0, os.path.abspath('..'))/" $(SPCONF) &> /dev/null
	sed -i '' 's/alabaster/sphinx_rtd_theme/' $(SPCONF) &> /dev/null
{%- endif %}

git:
	$(info ** Initiate Git Repo ****************)
	git init &> /dev/null
	git add . &> /dev/null
	git commit -m "first commit" &> /dev/null
	git branch -M $(BRANCH) &> /dev/null
	git remote add origin git@github.com:$(OWNER)/$(REPO).git &> /dev/null
	git config user.name "{{cookiecutter.full_name}}" &> /dev/null
	git config user.email "{{cookiecutter.email_address}}" &> /dev/null

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
