# Benchmark Notebook

A dependency-free Python benchmark analyzer for latency, duration, and other numerical samples.

## Usage

```bash
python benchmark_notebook.py examples/latency.json
python -m unittest discover -s tests -v
```

The input file contains a JSON object with a nonempty `samples` array of finite numbers. The tool calculates count, mean, median, minimum, maximum, and nearest-rank p50/p90/p95/p99 percentiles. It rejects nonnumeric or nonfinite samples. Returns exit code 0 on success and 2 on malformed input.

## Scope

This is a **statistical summary** tool, not a benchmark runner. It does not execute workloads, estimate confidence intervals, or compare distributions automatically.
