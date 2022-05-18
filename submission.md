# Ploomber: Developing Maintainable and Reproducible Data Pipelines Interactively From Jupyter, VSCode, and PyCharm

## Abstract

In this tutorial, Eduardo and Ido will introduce Ploomber. This open-source framework allows practitioners to use interactive platforms such as Jupyter, VSCode, or PyCharm to develop maintainable and reproducible data pipelines (aka workflows). The tutorial will go from zero to testing pipelines on GitHub Actions, using Pull Requests to collaborate, parallel experiments, and execution in distributed environments like Kubernetes and SLURM.

## Tutorial description

Interactive environments such as Jupyter have a reputation for producing low-quality, unmaintainable code. As a result, it is common for practitioners to go through a refactoring process where the notebook's code transforms into a more modular, maintainable form, usually through scripts and functions.

However, this creates friction since the refactoring process happens every time the analysis needs changes, causing practitioners to move back and forth between their notebooks and the refactored code. This constant moving slows down the iteration process and risks reproducibility.

Ploomber is an open-source framework that addresses this problem. It allows practitioners to stay in the interactive interface they are the most productive with while providing the tools to help them build maintainable and reproducible data workflows from day one.

In this tutorial, Eduardo and Ido will introduce Ploomber, going from zero to testing pipelines on GitHub Actions, using Pull Requests to collaborate, parallel experiments, and execution in distributed environments like Kubernetes and SLURM.

## Outline

The first half of each section will be an explanation and demonstration from the facilitators, followed by a hands-on exercise.

(Total: 4 hours)


Block I: The basics
(1 hour + 10-minute break)

Introduction (5 minutes)
We'll motivate the project and explain why investing in organizing our project as a modular pipeline (multiple scripts/notebooks) instead of a big script/notebook helps us develop faster and enhances collaboration.

Refactoring a legacy notebook (10 minutes)
Users may already have existing projects in notebooks, and we want to help them easily migrate their code to Ploomber. We'll demonstrate how they can use our open-source tool to convert monolithic notebooks into Ploomber pipelines with one command.

The pipeline.yaml file (10 minutes)
The pipeline.yaml file is where users declare the source code they want to execute and their outputs. In this section, we explain how the pipeline.yaml file is structured.

The command-line interface (10 minutes)
We introduce the command-line interface, which allows us to manage our pipeline: execute the workflow fully or partially, generate a pipeline diagram, and check the status.

Using Ploomber from JupyterLab, VSCode, or PyCharm (10 minutes)
We'll show how practitioners can use Ploomber from their favorite text editor.

Pipeline parametrization (15 minutes)
We introduce the concept of parametrization, which allows us to run our pipeline with different parameters. Parametrization helps us apply the same analysis to additional data to organize our experiments.


Block II: Advanced features
(1 hour + 10-minute break)

Smoke testing (10 minutes)
When editing notebooks, we may add, remove, or change the order of our code cells, breaking our code; preventing the reproducibility of our results. Here we introduce the concept of smoke testing and apply it to our pipeline. We demonstrate how this low-effort action can dramatically speed up iteration speed and help us check if our code is reproducible.

Adding new tasks (10 minutes)
We demonstrate how to add new tasks to our existing pipeline and establish the dependency relations among tasks.

Incremental builds (10 minutes)
Data analysis is an iterative process, and we often make small changes and rerun the code to see how that affects our results. We'll show how incremental builds allow users to run more experiments faster by caching previous results.

Adding data quality tests (15 minutes)
Here we improve our testing strategy. We demonstrate how to use Ploomber to add data quality tests to each task in our pipeline. These tests serve as sanity checks to ensure each output produces high-quality data.

Debugging (15 minutes)
This section will show Ploomber's debugging capabilities, which allows us to debug our pipelines when they fail.


Block III: Collaboration
(45 minutes + 10-minute break)

Using GitHub Actions for smoke testing (20 minutes)
We'll demonstrate a simple setup to enhance collaboration using GitHub Action, a free tool that will automate code testing, so we know if we broke anything.

Collaboration using Pull Requests on GitHub (25 minutes)
This section will demonstrate how we can use Pull Requests for asynchronous collaboration.


Block IV: Scaling Up Experiments
(45 minutes)

Running experiments in parallel (15 minutes)
Often we want to run some analysis with the same input data but different parameters. Users typically rely on modules like multiprocessing to achieve this but require a lot of glue code and know-how. We demonstrate how to parallelize experiments in Ploomber, which manages the multiprocessing parts.

Execution in distributed environments (30 minutes)
We demonstrate how users can export their local workflows to run in distributed environments. For example, many universities and research institutes have SLURM clusters available. Ploomber can export pipelines to SLURM (and other platforms such as Kubernetes) to scale experiments.

## Pre-requisites

* Basic experience with Jupyter, VSCode or PyCharm
* Basic experience with pandas is required
* A GitHub account is required
* A mybinder.org link will be provided for users to follow the workshop without configuring an environment. Instructions for setting up a local environment will be provided as well.