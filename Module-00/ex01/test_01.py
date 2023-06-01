from TinyStatistician import TinyStatistician as ts

a = [1, 42, 300, 10, 59]
print(f"a = {a}")
print(f"sorted(a) = {sorted(a)}")

print(f"\nmean(a) = {ts.mean(a)}")
print(f"example: {82.4}")

print(f"\nmedian(a) = {ts.median(a)}")
print(f"example: {42.0}")

print(f"\nquartile(a) = {ts.quartile(a)}")
print(f"example: {[10.0, 59.0]}")

print(f"\npercentile(a, 10) = {ts.percentile(a, 10)}")
print(f"example: {4.6}")

print(f"\npercentile(a, 15) = {ts.percentile(a, 15)}")
print(f"example: {6.4}")

print(f"\npercentile(a, 20) = {ts.percentile(a, 20)}")
print(f"example: {8.2}")

print(f"\nvariance(a) = {ts.variance(a)}")
print(f"example: {15349.3}")

print(f"\nstd(a) = {ts.std(a)}")
print(f"example: {123.89229193133849}")
