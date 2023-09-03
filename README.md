# FastAPI Experiment: Async vs Sync

An experiment to compare performance of sync and async endpoints in FastAPI.

## Overview:

-   [Setup](#setup)
-   [Run experiments](#run-experiments)
-   [Results](#results)
-   [Conclusion](#conclusion)

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

### FastAPI Application

The experiments are run on a simple FastAPI application. The application has two endpoints:

-   `/sync`: A synchronous endpoint that sleeps for 10 seconds and returns a response.
-   `/async`: An asynchronous endpoint that sleeps for 10 seconds and returns a response.

### Gunicorn Configuration

The experiments use `gunicorn` as the server. The configuration is as follows:

- experiment 1: 1 worker 1 thread

```bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker --threads 1 app:app
```

- experiment 2: 1 worker 4 threads

```bash
gunicorn -w 1 -k uvicorn.workers.UvicornWorker --threads 4 app:app
```

- experiment 3: 4 workers 1 thread

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --threads 1 app:app
```

- experiment 4: 4 workers 4 threads

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --threads 4 app:app
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

### Experiment 1: 1 worker 1 thread

- sync benchmark result:

```
Running 1m test @ http://localhost:8000/sync
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.04s     5.43s   30.00s    66.67%
    Req/Sec    32.61     59.70   220.00     89.29%
  200 requests in 1.00m, 28.52KB read
  Socket errors: connect 0, read 0, write 0, timeout 50
Requests/sec:      3.33
Transfer/sec:     486.37B
```

- async benchmark result:

```
Running 1m test @ http://localhost:8000/async
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.01s     6.23ms  10.03s    65.60%
    Req/Sec    26.15     46.83   200.00     87.88%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

### Experiment 2: 1 worker 4 threads

- sync benchmark result:

```
Running 1m test @ http://localhost:8000/sync
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    17.80s     5.21s   30.00s    68.03%
    Req/Sec    34.61     54.21   210.00     83.87%
  200 requests in 1.00m, 28.52KB read
  Socket errors: connect 0, read 0, write 0, timeout 53
Requests/sec:      3.33
Transfer/sec:     486.52B
```

- async benchmark result:

```
Running 1m test @ http://localhost:8000/async
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.00s     4.96ms  10.02s    84.80%
    Req/Sec    16.08     41.37   180.00     87.50%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

### Experiment 3: 4 workers 1 thread

- sync benchmark result:

```
Running 1m test @ http://localhost:8000/sync
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.00s     2.65ms  10.01s    60.00%
    Req/Sec     2.00      0.00     2.00    100.00%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

- async benchmark result:

```
Running 1m test @ http://localhost:8000/async
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.00s     1.87ms  10.01s    74.40%
    Req/Sec     2.00      0.00     2.00    100.00%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

### Experiment 4: 4 workers 4 threads

- sync benchmark result:

```
Running 1m test @ http://localhost:8000/sync
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.01s     3.63ms  10.02s    67.60%
    Req/Sec    12.42     26.35   100.00     83.33%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

- async benchmark result:

```
Running 1m test @ http://localhost:8000/async
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.00s     2.11ms  10.01s    79.20%
    Req/Sec     2.00      0.00     2.00    100.00%
  500 requests in 1.00m, 71.29KB read
Requests/sec:      8.33
Transfer/sec:      1.19KB
```

## Conclusion

1.  Sync endpoint:

    - shows high average latency with 1 worker
    - shows similar latency as async endpoint when number of workers is increased

2.  Async endpoint:

    - shows consistent latency across all experiments. Increasing the number of
    workers or threads does not affect the latency

In case of sync endpoints, increasing the number of workers improves the performance.
However, in case of async endpoints, increasing the number of workers or threads doesn't
appear to have any effect on the performance despite `asyncio.sleep` being a non-blocking call.
