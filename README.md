# Detector Latency Report

Compare inference timings and throughput by detector and image size.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `[{"model":"RT-DETR","width":640,"height":480,"milliseconds":230.4}]`

Run: `python main.py timings.json report.csv`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

RT-DETR, Detectron2, or any detector with timing logs. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

Input timings must be measured externally; this tool does not run a detector. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.


## Why it is useful

Detector speed numbers are only meaningful with context. This tool groups externally measured inference times by model and input dimensions, then computes sample count, mean, median, and images per second.

## Data contract

Input is a JSON array of `{model, width, height, milliseconds}` records. Each record represents one completed inference. Output is CSV, grouped by model name and resolution.

## Reproduce the example

```bash
python main.py examples/timings.json examples/report.csv
```

The command reads the included sample input. Generated reports in `examples/` can be removed when finished.

## Interpretation

The script does not distinguish preprocessing, model execution, and postprocessing. Record timing boundaries and hardware when collecting samples; do not compare unlike runs.

## License

MIT. See `LICENSE`.

