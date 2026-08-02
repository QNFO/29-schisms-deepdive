#!/usr/bin/env python3
"""Depth-4 search — FAST variant with progress prints and file output."""
import sys, random, time
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

random.seed(20260802)
t0 = time.time()
OUT = r'C:\Users\LENOVO\Projects\29-schisms-task13\_depth4_hits.txt'
tree5 = build_tree(max_depth=5)
nodes5 = sorted(tree5.keys(), key=lambda n: (tree5[n][2], n))
N5 = len(nodes5)
idx5 = {n: i for i, n in enumerate(nodes5)}

D5 = [[0.0] * N5 for _ in range(N5)]
for i, a in enumerate(nodes5):
    for j in range(i + 1, N5):
        d = dist(a, nodes5[j], tree5)
        D5[i][j] = D5[j][i] = d

def is_ne(images):
    for i in range(N5):
        for j in range(i + 1, N5):
            if D5[images[i]][images[j]] > D5[i][j] + 1e-12:
                return False
    return True

def fp_traj(images):
    cur, seen, traj = idx5[EMPTY], set(), [idx5[EMPTY]]
    for _ in range(100):
        nxt = images[cur]
        if nxt == cur:
            return cur, traj
        if nxt in seen:
            return None, traj
        seen.add(nxt)
        traj.append(nxt)
        cur = nxt
    return None, traj

pools = {}
for n in nodes5:
    anc = [a for a in nodes5 if a in ancestor_path(n, tree5)]
    ch = [c for c in nodes5 if tree5[c][0] == n]
    pools[n] = list(dict.fromkeys(anc + [n] + ch))

d1 = [n for n in nodes5 if tree5[n][2] == 1]
d2 = [n for n in nodes5 if tree5[n][2] == 2]
d3 = [n for n in nodes5 if tree5[n][2] == 3]
d4 = [n for n in nodes5 if tree5[n][2] == 4]
climbs = []
for a in d1:
    for b in [c for c in d2 if tree5[c][0] == a]:
        for x in [c for c in d3 if tree5[c][0] == b]:
            for y in [c for c in d4 if tree5[c][0] == x]:
                climbs.append((a, b, x, y))
for b in d2:
    for x in [c for c in d3 if tree5[c][0] == b]:
        for y in [c for c in d4 if tree5[c][0] == x]:
            climbs.append(('#', b, x, y))

SAMPLES = 50000
hits = []
with open(OUT, 'w') as f:
    for ci, (a, b, x, y) in enumerate(climbs):
        t1 = time.time()
        chain = [(EMPTY, a), (a, b), (b, x), (x, y), (y, y)]
        climbers = set(n for n, _ in chain)
        cmap = dict(chain)
        other = [n for n in nodes5 if n not in climbers]
        found = False
        for s in range(SAMPLES):
            images = [0] * N5
            for n, img in chain:
                images[idx5[n]] = idx5[img]
            for n in other:
                images[idx5[n]] = idx5[random.choice(pools[n])]
            if not is_ne(images):
                continue
            fp, traj = fp_traj(images)
            if fp is not None and nodes5[fp] == y:
                Fd = {n: nodes5[v] for n, v in enumerate(images)}
                hits.append((ci, y, Fd))
                line = f"HIT climb {ci}: T*={y!r} depth={tree5[y][2]} F={Fd}\n"
                f.write(line)
                f.flush()
                print(line.rstrip())
                found = True
                break
        dt = time.time() - t1
        print(f"climb {ci}: T*={y!r} chain={a!r}->{b!r}->{x!r}->{y!r} done {SAMPLES}samples/{dt:.1f}s {'HIT!' if found else 'none'}")
        if found:
            break

with open(OUT, 'a') as f:
    f.write(f"\nTOTAL: {len(hits)} hits in {time.time()-t0:.1f}s\n")
print(f"\nTOTAL: {len(hits)} hits in {time.time()-t0:.1f}s")
for ci, tstar, Fd in hits:
    viol = sum(1 for i, a in enumerate(nodes5) for j in range(i+1,N5)
               if D5[idx5[Fd[a]]][idx5[Fd[b]]] > D5[idx5[a]][idx5[nodes5[j]]] + 1e-12)
    print(f"  Verify climb {ci}: T*={tstar!r} violations={viol}")
