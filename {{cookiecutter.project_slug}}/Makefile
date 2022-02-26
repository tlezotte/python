BRANCH	 = main
OWNER  	 = {{cookiecutter.git_owner}}
REPO   	 = {{cookiecutter.git_repo}}

#.SILENT: git
#.SILENT: install
#.SILENT: cli
#.SILENT: api
#.SILENT: show


# Default target.
all:
	echo "Hello $(LOGNAME), nothing to do by default"

install:
	poetry config virtualenvs.in-project true --quiet
	poetry config virtualenvs.create true --quiet
	poetry new {{ cookiecutter.project_slug }} --quiet
	cd {{ cookiecutter.project_slug }}
	poetry env use python --quiet

git:
	git init
	git add .
	git commit -m "first commit"
	git branch -M $(BRANCH)
	git remote add origin git@github.com:$(OWNER)/$(REPO).git
	git push -u origin main

cli:
	poetry add typer --quiet
	poetry add rich --quiet

api:
	poetry add uvicorn[standard] --quiet
	poetry add fastapi --quiet
	poetry add sqlmodel --quiet

show:
	poetry show
