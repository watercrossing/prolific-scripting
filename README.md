# Managing Prolific Studies with Jupyter Notebook

The notebook `study-management.ipynb` demonstrates how [Prolific](https://prolific.com)'s API can be used to create and manage a stratified study.

A minimal API for Prolific and Qualtrics is implemented in the file `APIs.py`. Both APIs require API keys, they can set via environment variables or in the file `.env`. See `.env.default` for details.

## Setup

This project uses [Jupyter Notebooks](https://jupyter.org/). To reduce the dependencies, this repository does not depend on `notebook` locally, but instead relies on a globally installed Jupyter Notebook installation. If you do not want to install Jupyter Notebook globally, see the alternative instructions below. You can skip steps 1-3 if you already have Jupyter Notebook installed. 

1. [Install python 3.11](https://www.python.org/downloads/) (other versions will probably also work)
2. [Install pipx](https://pypa.github.io/pipx/)
3. Install notebook in pipx (`pipx install notebook`)
3. Install pipenv in pipx (`pipx install pipenv`)
3. Make the pipenv kernel available to your notebook installation  `pipenv run python -m ipykernel install --name prolific-scripting --user` (or [automate this process for all pipenv kernels](https://stackoverflow.com/questions/73525908/pipenv-aware-jupyter-kernel))
3. Clone repo (`git clone <repo>`)
3. Install dependencies  (`pipenv install`)
3. Run `jupyter-notebook`

## Alternative setup

1. [Install python 3.11](https://www.python.org/downloads/)
2. [Install pipenv](https://pipenv.pypa.io/en/latest/) (`pip install --user pipenv`)
3. Clone repo (`git clone repo`)
3. Install dependencies (`pipenv install`)
3. Add Jupyter Notebook to local dependencies (`pipenv install notebook`)
3. Run `pipenv run jupyter-notebook`
3. Please do not commit the updated Pipfile with the notebook dependency

