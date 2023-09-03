# FastAPI Experiment: Async vs Sync

An experiment to compare performance of sync and async workers in FastAPI.

## Setup

The repository uses Python 3.11. Follow the steps below to get started:

-   Create conda environment:

    ```bash
    conda create -n fastapi-tests python=3.11 -y
    conda activate fastapi-tests
    ```

    You can choose any other environment manager of your choice.

-   Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    **Note**: All requirement files are generated using `pip-tools`.

## Run experiments

### Gunicorn Configuration

The experiments use `gunicorn` as the server. The configuration is as follows:

- experiment 1: 1 worker 4 threads

```bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker --threads 4 app:app
```

- experiment 2: 4 workers 1 thread

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --threads 1 app:app
```

### wrk benchmarks

The experiments use `wrk` to benchmark the server. The configuration is as follows:

```bash
wrk -t4 -c100 -d1m --timeout 30s <fastapi-endpoint>
```

-   4 threads
-   100 connections
-   1 minute duration
-   30 seconds timeout

Run the benchmark script:

```bash
./benchmark.sh
```

## Results

### Experiment: 1 worker 4 threads


### Experiment: 4 workers 1 thread
