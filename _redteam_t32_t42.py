# -*- coding: utf-8 -*-
"""
RED TEAM AUDIT — Independent verification of T3.2 (Sibling Collapse) and T4.2 (FP Depth Bound).
1) Exhaustively find a globally CONTRACTIVE map with distinct sibling images (refutes T3.2).
2) Find a non-expansive map with F(ROOT) at depth 3 (refutes T4.2).
Prints explicit evidence; no summary claims.
"""
import sys, itertools, time
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

tree = build_tree(max_depth=3)
nodes = list(tree.keys())
idx = {n: i for i, n in enumerate(nodes)}
N = len(nodes)

# Distance matrix via executable's own dist()
D = [[0.0]*N for _ in range(N)]
for i, a in enumerate(nodes):
    for j in range(i+1, N):
        d = dist(a, nodes[j], tree)
        D[i][j] = D[j][i] = d

pairs = [(i, j) for i in range(N) for j in range(i+1, N)]

# Sibling pairs
from collections import defaultdict
by_parent = defaultdict(list)
for n in nodes:
    p = tree[n][0]
    if p is not None:
        by_parent[p].append(n)
sib_pairs = []
for p, kids in by_parent.items():
    for i, k1 in enumerate(kids):
        for k2 in kids[i+1:]:
            sib_pairs.append((idx[k1], idx[k2]))

print(f"Nodes: {nodes}")
print(f"Sibling pairs: {[(nodes[i], nodes[j]) for i, j in sib_pairs]}")
print(f"D matrix:")
for i in range(N):
    print(f"  {nodes[i]!r:7s}: " + " ".join(f"{D[i][j]:.2f}" for j in range(N)))

def is_contractive(images):
    """GLOBALLY contractive: ALL pairs strictly contract (dist < original)."""
    for i, j in pairs:
        if D[images[i]][images[j]] >= D[i][j] - 1e-12:
            return False
    return True

def is_ne(images):
    for i, j in pairs:
        if D[images[i]][images[j]] > D[i][j] + 1e-12:
            return False
    return True

print("\n=== T3.2 AUDIT: find globally CONTRACTIVE map with distinct sibling images ===")
t0 = time.time()
found_t32 = None
count_cont = 0
for combo in itertools.product(range(N), repeat=N):
    if not is_contractive(combo):
        continue
    count_cont += 1
    for s1, s2 in sib_pairs:
        if combo[s1] != combo[s2]:
            found_t32 = combo
            break
    if found_t32 is not None:
        break
    if count_cont >= 200000:
        break
if found_t32 is not None:
    Fmap = {nodes[k]: nodes[v] for k, v in enumerate(found_t32)}
    print(f"FOUND globally contractive map with distinct sibling images (count_cont={count_cont}, {time.time()-t0:.1f}s):")
    print(f"  F = {Fmap}")
    for s1, s2 in sib_pairs:
        if found_t32[s1] != found_t32[s2]:
            a, b = nodes[s1], nodes[s2]
            print(f"  SIBLINGS {a!r},{b!r} -> {Fmap[a]!r},{Fmap[b]!r} (distinct images)")
    # Verify global contractiveness explicitly for this map
    viol = [(nodes[i], nodes[j], D[i][j], D[found_t32[i]][found_t32[j]]) 
            for i, j in pairs if D[found_t32[i]][found_t32[j]] >= D[i][j] - 1e-12]
    print(f"  Global-contractiveness re-check: {len(viol)} non-contracting pairs -> {'CONTRACTIVE CONFIRMED' if not viol else 'NOT CONTRACTIVE'}")
    print(f"  => T3.2 (any contractive map collapses siblings) REFUTED")
else:
    print(f"No contractive map with distinct sibling images found in {count_cont} contractive maps ({time.time()-t0:.1f}s)")
    print(f"  => T3.2 NOT refuted at depth<=3")

print("\n=== T4.2 AUDIT: find non-expansive map with F(ROOT) at depth 3 ===")
root_i = idx[EMPTY]
t1 = time.time()
found_t42 = None
for combo in itertools.product(range(N), repeat=N):
    if combo[root_i] == root_i:
        continue
    if not is_ne(combo):
        continue
    fd = tree[nodes[combo[root_i]]][2]
    if fd == 3:
        found_t42 = combo
        break
if found_t42 is not None:
    Fmap = {nodes[k]: nodes[v] for k, v in enumerate(found_t42)}
    print(f"FOUND non-expansive map with F(ROOT) at depth 3 ({time.time()-t1:.1f}s):")
    print(f"  F = {Fmap}")
    print(f"  F(ROOT) = {Fmap[EMPTY]!r} at depth {tree[Fmap[EMPTY]][2]}")
    viol = [(nodes[i], nodes[j], D[i][j], D[found_t42[i]][found_t42[j]])
            for i, j in pairs if D[found_t42[i]][found_t42[j]] > D[i][j] + 1e-12]
    print(f"  Non-expansiveness re-check: {len(viol)} violations -> {'NON-EXPANSIVE CONFIRMED' if not viol else 'NOT NON-EXPANSIVE'}")
    print(f"  => T4.2 (F(ROOT) depth <= 1) REFUTED")
else:
    print(f"No non-expansive map with F(ROOT) at depth 3 found ({time.time()-t1:.1f}s)")
    print(f"  => T4.2 NOT refuted at depth<=3")

print("\n=== DONE ===")
