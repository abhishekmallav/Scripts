import pkg_resources
import os


def get_size(path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total


dists = sorted(pkg_resources.working_set, key=lambda d: d.project_name.lower())
sizes = []

for dist in dists:
    try:
        size = get_size(dist.location + "/" +
                        dist.project_name.replace("-", "_"))
        sizes.append((dist.project_name, size / 1024 / 1024))  # MB
    except Exception:
        pass

# Open file for writing
with open("pip_packages.txt", "w") as f:
    for name, size in sorted(sizes, key=lambda x: x[1], reverse=True):
        line = f"{name:<30} {size:.2f} MB"
        print(line)       # print to terminal
        f.write(line + "\n")  # save to file

print("\n✅ Saved results to pip_packages.txt")
