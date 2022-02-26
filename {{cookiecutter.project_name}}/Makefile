BRANCH	 = main
OWNER  	 = {{cookiecutter.project_owner}}
REPO   	 = {{cookiecutter.project_repo}}

.SILENT: git
.SILENT: install
.SILENT: cli
.SILENT: api
.SILENT: show


# Default target.
all:
	echo "Hello $(LOGNAME), nothing to do by default"

install:
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry env use python --quiet

git:
	git init
	git add .
	git commit -m "Initial commit"
	git remote add origin git@github.com:$(OWNER)/$(REPO).git
	git push

cli:
	poetry add typer --quiet
	poetry add rich --quiet

api:
	poetry add uvicorn[standard] --quiet
	poetry add fastapi --quiet
	poetry add sqlmodel --quiet

show:
	poetry show
