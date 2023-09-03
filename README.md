# FastAPI Experiment: Async vs Sync

A small experiment to compare performance of sync and async workers in FastAPI.

## Setup

The repository uses Python 3.11. Follow the steps below to get started:

1.  Create conda environment:

    ```bash
    conda create -n fastapi-tests python=3.11 -y
    conda activate fastapi-tests
    ```

    You can choose any other environment manager of your choice.

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    **Note**: All requirement files are generated using `pip-tools`.
