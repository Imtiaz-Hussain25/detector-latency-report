import argparse, csv, json, statistics
from collections import defaultdict

def report(records):
    groups = defaultdict(list)
    for row in records:
        groups[(row["model"], int(row["width"]), int(row["height"]))].append(float(row["milliseconds"]))
    output = []
    for (model, width, height), times in sorted(groups.items()):
        mean = statistics.mean(times)
        output.append({"model":model,"width":width,"height":height,"samples":len(times),
                       "mean_ms":round(mean,2),"median_ms":round(statistics.median(times),2),
                       "images_per_second":round(1000/mean,2) if mean else 0})
    return output

def main():
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output"); a=p.parse_args()
    rows=report(json.load(open(a.input,encoding="utf-8")))
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["model","width","height","samples","mean_ms","median_ms","images_per_second"])
        w.writeheader(); w.writerows(rows)
if __name__=="__main__": main()

