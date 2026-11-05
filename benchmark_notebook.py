"""Summarize numerical benchmark samples from JSON input."""
import argparse
import json
import math
import statistics
import sys

def summarize(samples):
    if not isinstance(samples,list) or not samples: raise ValueError("samples must be a nonempty array")
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in samples):
        raise ValueError("samples must contain finite numbers")
    values=sorted(samples)
    def percentile(p):
        rank=max(1,math.ceil(p*len(values)))
        return values[rank-1]
    return {"count":len(values),"min":values[0],"max":values[-1],
            "mean":statistics.mean(values),"median":statistics.median(values),
            "p50":percentile(.50),"p90":percentile(.90),"p95":percentile(.95),"p99":percentile(.99)}

def main(argv=None):
    p=argparse.ArgumentParser(description="Summarize benchmark samples")
    p.add_argument("file",help="JSON file with a samples array")
    args=p.parse_args(argv)
    try:
        with open(args.file,encoding="utf-8") as f: data=json.load(f)
        if not isinstance(data,dict): raise ValueError("input must be a JSON object")
        result=summarize(data.get("samples"))
    except (OSError,ValueError,TypeError) as exc:
        print(str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
