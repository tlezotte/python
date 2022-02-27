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
	$(info Creating VENV **********)
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry env use python --quiet

{% if cookiecutter.project_type == "api" %}
packages:
	$(info Installing API Software **********)
	poetry add uvicorn[standard] --quiet
	poetry add fastapi --quiet
	poetry add sqlmodel --quiet
{%- endif %}

{% if cookiecutter.project_type == "cli" %}
packages:
	$(info Installing CLI Software **********)
	poetry add typer --quiet
	poetry add rich --quiet
{%- endif %}

git:
	$(info Initiate Git Repo **********)
	git init 2> /dev/null
	git add . 2> /dev/null
	git commit -m "first commit" 2> /dev/null
	git branch -M $(BRANCH) 2> /dev/null
	git remote add origin git@github.com:$(OWNER)/$(REPO).git 2> /dev/null

show:
	$(info Installed Packages **********)
	poetry show
