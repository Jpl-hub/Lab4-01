# Lab 4 - CI & CD

## Development

```shell script
poetry shell                   # activate a working virtual environment
poetry install                 # install all dependencies
pre-commit install             # install pre-commit hooks
black .                        # lint all Python code
pytest -r P --cov=pygraph      # run all tests with test stdout and coverage report
python -m pdoc --html pygraph  # build API documentation and deploy to html/
```
