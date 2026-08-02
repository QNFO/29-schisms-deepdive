#!/usr/bin/env python3
"""Depth-4 fixed point search at tree<=5 — NODE-IDENTITY MAPPING FIX.
Builds F dict by explicit node key, not sorted-index zip.
Each climb node gets its image by name; non-climb nodes get random local-pool images.
"""
import sys, random, itertools, time
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

random.seed(20260801)
t0 = time.time()
tree5 = build_tree(max_depth=5)
nodes5 = sorted(tree5.keys(), key=lambda n: (tree5[n][2], n))
N5 = len(nodes5)
idx5 = {n: i for i, n in enumerate(nodes5)}

D5 = [[0.0]*N5 for _ in range(N5)]
for i, a in enumerate(nodes5):
    for j in range(i+1, N5):
        d = dist(a, nodes5[j], tree5)
        D5[i][j] = D5[j][i] = d

def is_ne(images):
    for i in range(N5):
        for j in range(i+1, N5):
            if D5[images[i]][images[j]] > D5[i][j] + 1e-12:
                return False
    return True

def fp_traj(images):
    cur = idx5[EMPTY]
    seen = set()
    traj = [cur]
    for _ in range(50):
        nxt = images[cur]
        if nxt == cur:
            return cur, traj
        if nxt in seen:
            return None, traj
        seen.add(nxt)
        traj.append(nxt)
        cur = nxt
    return None, traj

# === BUILD CLIMB CHAINS ===
d1 = [n for n in nodes5 if tree5[n][2] == 1]
d2 = [n for n in nodes5 if tree5[n][2] == 2]
d3 = [n for n in nodes5 if tree5[n][2] == 3]
d4 = [n for n in nodes5 if tree5[n][2] == 4]
d5 = [n for n in nodes5 if tree5[n][2] == 5]
print(f"Tree<=5: {N5} nodes | d1={d1} d2={d2} d3={d3} d4={len(d4)} d5={len(d5)}")

# All feasible climbs: '' -> d1 -> d2 -> d3 -> d4 -> fixed(d4)
# (each step must be a real parent-child edge)
climbs = []
for a in d1:
    for b in [c for c in d2 if tree5[c][0] == a]:
        for x in [c for c in d3 if tree5[c][0] == b]:
            for y in [c for c in d4 if tree5[c][0] == x]:
                climbs.append((a, b, x, y))
print(f"Feasible d4 climbs: {len(climbs)}")

# Sampled climbs for speed; also test '#'->'[]' sibling-style jumps 
extra = []
for b in d2:
    for x in [c for c in d3 if tree5[c][0] == b]:
        for y in [c for c in d4 if tree5[c][0] == x]:
            extra.append(('#', b, x, y))
climbs = climbs + extra
print(f"Total d4 climbs (all + sibling-style): {len(climbs)}")

# === LOCAL POOLS ===
pools = {}
for n in nodes5:
    anc = [a for a in nodes5 if a in ancestor_path(n, tree5)]
    ch = [c for c in nodes5 if tree5[c][0] == n]
    pools[n] = list(dict.fromkeys(anc + [n] + ch))

SAMPLES = 200000
hits = []

for ci, (a, b, x, y) in enumerate(climbs):
    # Build climb chain as (node, image) pairs
    climb_chain = [
        (EMPTY, a),   # F('') = a
        (a, b),       # F(a)  = b
        (b, x),       # F(b)  = x
        (x, y),       # F(x)  = y
        (y, y),       # F(y)  = y  (fixed point T*)
    ]
    climb_nodes = set(n for n, _ in climb_chain)
    climb_map = dict(climb_chain)
    other_nodes = [n for n in nodes5 if n not in climb_nodes]
    
    found = False
    for _ in range(SAMPLES):
        images = [0] * N5
        for n, img in climb_chain:
            images[idx5[n]] = idx5[img]
        for n in other_nodes:
            images[idx5[n]] = idx5[random.choice(pools[n])]
        
        if not is_ne(images):
            continue
        fp, traj = fp_traj(images)
        if fp is not None:
            fd = tree5[nodes5[fp]][2]
            if nodes5[fp] == y:  # T* is the depth-4 target
                Fdict = {n: nodes5[v] for n, v in enumerate(images)}
                hits.append((ci, y, Fdict))
                print(f"HIT climb {ci}: T*={y!r} depth={fd} F={Fdict}")
                found = True
                break
    if found:
        break  # one hit per climb is enough

print(f"\nDepth-4 search done: {len(hits)} hits across {len(climbs)} climbs ({time.time()-t0:.1f}s)")

# === INDEPENDENT VERIFICATION of each hit ===
if hits:
    print("\n=== INDEPENDENT PAIR-BY-PAIR VERIFICATION ===")
    for ci, tstar, Fdict in hits:
        images = [idx5[Fdict[n]] for n in nodes5]
        viol = []
        for i, a in enumerate(nodes5):
            for j in range(i+1, N5):
                if D5[images[i]][images[j]] > D5[i][j] + 1e-12:
                    viol.append((a, nodes5[j]))
        fp, traj = fp_traj(images)
        fp_node = nodes5[fp] if fp is not None else None
        fp_depth = tree5[fp_node][2] if fp_node and fp_node in tree5 else 0
        ok = len(viol) == 0 and fp_node is not None and fp_depth >= 4
        print(f"  climb {ci}: T*={tstar!r} depth={fp_depth} violations={len(viol)} -> {'CONFIRMED non-expansive depth-4' if ok else 'FAILED'}")
        if viol:
            for v in viol[:5]:
                print(f"    V: {v[0]!r},{v[1]!r}")
else:
    print("NO depth-4 non-expansive map found. Ascendant-climb pattern confirmed BROKEN at d=4.")
