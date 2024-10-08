# How Warm Is It In Delft?

[![Pytest](https://github.com/bilalbox/HoeWarmIsHetInDelft/actions/workflows/pytest-coverage-commentator.yml/badge.svg?branch=main)](https://github.com/bilalbox/HoeWarmIsHetInDelft/actions/workflows/pytest-coverage-commentator.yml)

[![Docker Image](https://github.com/bilalbox/HoeWarmIsHetInDelft/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/bilalbox/HoeWarmIsHetInDelft/actions/workflows/docker-image.yml)

Prints the current temperature in Delft in degrees Celcius.

## Project Tasks

1. Create a Python script called 'HoeWarmIsHetInDelft.py' that retrieves the current temperature in Delft from [www.weerindelft.nl](https://www.weerindelft.nl/) and prints it to standard output, rounded to degrees Celsius.

Example expected output
`8 degrees Celsius`

2. Write an appropriate dockerfile to containerize the script developed in point 1 3. Write a simple pipeline on [gitlab.com](https://www.gitlab.com) that builds the container above and then executes it. We'll review the code based on clarity and correctness. It is important for the code to be robust, run correctly in a pipeline environment and to be easily troubleshooted by other DevOps engineers.

3. Please submit your solution as a link to a repository, ensuring that it is accessible to everyone.

## USAGE

`docker run --rm ghcr.io/bilalbox/hoewarmishetindelft:main`

## INSTALLATION AND TESTING

1. Clone the repo with `git clone gitlab.com/bilalbox/hoewarmishetindelft.git && cd hoewarmishetindelft`
2. Create a virtual environment and activate it with `python -m venv .venv` and `source .venv/bin/activate`
3. Install dependencies with `pip install -r requirements`
4. For testing and code coverage reports, install dependencies with `pip install pytest coverage`
5. Run tests and generate code coverage reports with `coverage run -m pytest ./tests && coverage report -m` from the project root
