# Python Template

## Init a Python project

```
cookiecutter gh:tlezotte/python
```

# Setup

```
brew install make
poetry config virtualenvs.in-project true
poetry config virtualenvs.create true
```

```
poetry new template --quiet
cd template
poetry env use python3 --quiet
#direnv allow
```

```
#pip install -U pip
poetry add uvicorn[standard] --quiet
poetry add fastapi --quiet
poetry add sqlmodel --quiet
poetry add typer --quiet
poetry add rich --quiet
poetry show
```

```
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:tlezotte/project1.git 
git push 
```
