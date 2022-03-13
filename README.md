# 📈 Awesome Panel [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-panel)

[<img src="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/panel-logo.png?raw=true" align="right" height="75">](https://panel.pyviz.org/)

[![GitHub Repo stars](https://img.shields.io/github/stars/marcskovmadsen/awesome-panel?style=social)](https://github.com/marcskovmadsen/awesome-panel) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen) [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCWaK0P72WvNUn4uB_oTh_0w?style=social)](https://www.youtube.com/playlist?list=PLrrcIlm1vLr69f4CsTlrO0wSNBw6VbsJA) [![Linked In](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/marcskovmadsen/)

[Panel](https://panel.holoviz.org/) **makes it easy to make your data, models and analytics interactive using the tools you know and love**.

[Awesome Panel](https://awesome-panel.org) aims to

- inspire and help users of Panel and
- push the framework forward.

This project provides

- A Panel [**Web Site**](https://awesome-panel.org) with an [**Awesome List**](https://awesome-panel.org/awesome-list) and a [**Gallery**](https://awesome-panel.org/gallery) of live Panel Apps with code.
- A [**Youtube Channel**](https://www.youtube.com/playlist?list=PLrrcIlm1vLr69f4CsTlrO0wSNBw6VbsJA).
- Some [**Docs**](http://awesome-panel.readthedocs.org/) with tips and tricks.

**Check out** [awesome-panel.org](https://awesome-panel.org).

[![Awesome Panel Org Animation](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/awesome-panel-full-branded.gif?raw=true)](https://awesome-panel.org)

**Check out** the [awesome-panel.org youtube channel](https://www.youtube.com/playlist?list=PLrrcIlm1vLr69f4CsTlrO0wSNBw6VbsJA).

[![Awesome Panel Youtube](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/awesome-panel-youtube.png)](https://www.youtube.com/playlist?list=PLrrcIlm1vLr69f4CsTlrO0wSNBw6VbsJA)

Panel is **completely open source and free** for both commercial and non-commercial use. Panel is part of the [HoloViz](https://holoviz.org/) ecosystem.

[<img src="https://holoviz.org/assets/panel.png" height="75">](https://panel.pyviz.org)
[<img src="https://holoviz.org/assets/hvplot.png" height="75">](https://hvplot.pyviz.org)
[<img src="https://holoviz.org/assets/holoviews.png" height="75">](https://holoviews.org)
[<img src="https://holoviz.org/assets/geoviews.png" height="75">](http://geoviews.org)
[<img src="https://holoviz.org/assets/datashader.png" height="75">](http://datashader.org)
[<img src="https://holoviz.org/assets/param.png" height="75">](https://param.pyviz.org)
[<img src="https://holoviz.org/assets/colorcet.png" height="75">](https://colorcet.pyviz.org)

## 🎁 Contribute

GitHub [Issues](https://github.com/MarcSkovMadsen/awesome-panel/issues) and [Pull requests](https://github.com/MarcSkovMadsen/awesome-panel/pulls) are very welcome!

### 🔗 Contribute an Item to the Awesome List

Do as much of the below as possible.

- Open a [Feature Request](https://github.com/MarcSkovMadsen/awesome-panel/issues) on Github describing the item.

- Make a PR to the [awesome_list.yml](application/pages/awesome_list/awesome_list.yml) file.

### 🖥️ Contribute an App to the Gallery

Do as much of the below as possible and reach out for help if needed.

- Open a [Feature Request](https://github.com/MarcSkovMadsen/awesome-panel/issues) on Github describing the request.
  If you already have an application attach the url, notebook, code file, .zip file etc. if possible.
- [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and follow the [Getting Started Instructions](#getting-started-with-the-awesome-panel-repository) below.
- Register your self as a new author in [_authors.py](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/config/_authors.py) and [_site.py](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/config/_site.py).
- Add your application as a new subfolder to [application/pages](application/pages).
- Add your application as a new route to [`APP_ROUTES`]([application\pages\__init__.py]).
- Add your application to the menus [links.html](application\assets\html\links.html) and [links_fast.html](application\assets\html\links_fast.html)
- Add any tests you might have to [tests/application](tests/application)
- Run `panel serve app.py` and manully test your app
- Run `invoke test.all` and fix all errors.
- Add your app to the [Locust end-2-end Test](performance\locust_e2e.py) and run `locust -f performance/locust_e2e.py` to monitor the performance of your app.
- Create a [pull request](https://github.com/marcskovmadsen/awesome-panel/pulls).
- Mark your [pull request](https://github.com/marcskovmadsen/awesome-panel/pulls) as "Ready".

## 🕊️ Share on Social Media

You can follow me on [Twitter](https://twitter.com/MarcSkovMadsen) and [Linked In](https://www.linkedin.com/in/marcskovmadsen/) and like or repost my posts.

## ☕ Sponsor the Awesome Panel Project

If you would like to **sponsor my time or the infrastructure** the platform is running on, feel free to [reach out](https://datamodelsanalytics.com). I would love to run [https://awesome-panel.org](https://awesome-panel.org) on some decent hardware instead of a low end dev server in Azure.

You can also appreciate the work that has already been done if you

[![Buy me a coffee](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/buymeacoffee.png?raw=true)](https://www.buymeacoffee.com/4jlTzBJyQ)

Thanks

### ⚖️ LICENSE

[Apache 2.0 License](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/LICENSE)

## 🏃 Getting Started with the Awesome Panel Repository

### 🧰 Prerequisites

- A working [Python](https://www.python.org/) installation.
    - Currently we are using v3.9.9.

### 🏎️ Installation

Clone the repo

```bash
git clone https://github.com/MarcSkovMadsen/awesome-panel.git
```

cd into the project root folder

```bash
cd awesome-panel
```

#### Create virtual environment and install Requirements

##### via python

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment using one of the below commands.

```bash
source .venv/Scripts/activate
```

```bash
source .venv/bin/activate
```

or for windows

```bash
.venv/Scripts/activate.bat
```

On windows please manually install the geopandas requirements as described in [using-geopandas-windows](https://geoffboeing.com/2014/09/using-geopandas-windows/)

Then you should install the local requirements

```bash
pip install -r requirements_local.txt -f https://download.pytorch.org/whl/torch_stable.html
```

##### or via Anaconda

Create virtual environment named awesome-panel

```bash
conda create -n awesome-panel python=3.9.9
```

and activate environment.

```bash
activate awesome-panel
```

On windows please manually install the geopandas requirements as described in [using-geopandas-windows](https://geoffboeing.com/2014/09/using-geopandas-windows/)

Then you should install the local requirements

```bash
conda install --file requirements_local.txt
```

### 🧱 Build and run the Application Locally

#### Set the environment variables if needed

on bash:

```bash
export BOKEH_ADDRESS=localhost
export BOKEH_PORT=5006
```

on powershell:

```powershell
$env:BOKEH_ADDRESS = 'localhost'
$env:BOKEH_PORT = 5006
```

Running the Application Locally

```bash
panel serve awesome_panel/apps/*.py --index home.py
```

or as a Docker container via

```bash
invoke docker.build --rebuild
invoke docker.run-server
```

### 🐋 Run the Application via Docker

If you don't want to clone the repo and build the docker container you can just use `docker run` to run the image from [Dockerhub](https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-panel)

To run the panel interactively on port 80

```bash
docker run -it -p 80:80 marcskovmadsen/awesome-panel:latest
```

To run bash interactively

```bash
docker run -it -p 80:80 --entrypoint "/bin/bash" marcskovmadsen/awesome-panel:latest
```

### Code quality and Tests

We use

- [isort](https://pypi.org/project/isort/) for sorting import statements
- [autoflake](https://github.com/myint/autoflake) to remove unused imports and unused variables
- [black](https://pypi.org/project/black/) the opinionated code formatter
- [pylint](https://www.pylint.org/) for static analysis
- [mypy](https://github.com/python/mypy) for static type checking
- [pytest](https://github.com/pytest-dev/pytest) for unit to functional tests
- [locust](https://locust.io/) for end-2-end tests.

to ensure a high quality of our code and application.

You can run most tests using

```bash
invoke test.all
```

You can run the Locust end-2-end tests via

```bash
invoke test.e2e
```

![Locust Gif](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/locust_e2e.gif?raw=true)

Please note you will need to have the Panel server running and point Locust to the correct host and port.

### 👷 Workflow

We use the power of [Invoke](http://www.pyinvoke.org/) to semi-automate the local workflow. You can see the list of available commands using

```bash
$ invoke --list
Available tasks:

  docker.build                            Build Docker image
  docker.push                             Push the Docker container
  docker.remove-unused                    Removes all unused containers to free up space
  docker.run                              Run the Docker container bash terminal interactively.
  docker.run-server                       Run the Docker image with the Panel server.
  docker.run-server-with-ping             Run the docker image with Panel server and
  docker.system-prune                     The docker system prune command will free up space
  jupyter.notebook                        Run jupyter notebook
  package.build                           Builds the awesome-panel package)
  sphinx.build                            Build local version of site and open in a browser
  sphinx.copy-from-project-root           We need to copy files like README.md into docs/_copy_of_project_root
  sphinx.linkcheck                        Build local version of site and open in a browser
  sphinx.livereload                       Start autobild documentation server and open in browser.
  sphinx.test                             Checks for broken internal and external links and
  test.all (test.pre-commit, test.test)   Runs isort, autoflake, black, pylint, mypy and pytest
  test.autoflake                          Runs autoflake to remove unused imports on all .py files recursively
  test.bandit                             Runs Bandit the security linter from PyCQA.
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.e2e                                Runs the Locust end to end tests
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
```

### 💻 CI/ CD and Hosting

The application is

- built as a Docker image and tested via Azure Pipelines.
  - You can find the Dockerfiles [here](https://github.com/MarcSkovMadsen/awesome-panel/tree/master/devops/docker) and the Azure pipelines yml files [here](https://github.com/MarcSkovMadsen/awesome-panel/tree/master/devops/azure-pipelines).

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/azure-pipeline.png?raw=true)
![Azure Pipelines Build and Test](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/azure-pipeline-build-test.png?raw=true)

- pushed to the Dockerhub repository [marcskovmadsen/awesome-panel](https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-panel).

![Dockerhub](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/dockerhub.png?raw=true)

- released via Azure Pipelines

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/azure-pipeline-release.png?raw=true)

- to a web app for containers service on Azure on the cheapest non-free pricing tier

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/azure-pricing-tier.png?raw=true)

- We also deploy the [awesome-panel docs](http://awesome-panel.readthedocs.org/) on Read the Docs.

## Build and Deploy the Awesome Panel Package

PLEASE NOTE THE AWESOME PANEL PACKAGE IS OBSOLETE AND REPLACED BY [awesome-panel-extensions](https://github.com/marcskovmadsen/awesome-panel-extensions).

You can build the package using

```bash
cd package
python setup.py sdist bdist_wheel
```

If you want to publish the package to PyPi you should first

update the version number in the setup.py file. The format is `YYYYmmdd.version`. For example `20191208.1`

Then you run

```bash
twine upload dist/awesome-panel-YYYYmmdd.version.tar.gz -u <the-pypi-username> -p <the-pypi-password>
```