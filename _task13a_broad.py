# -*- coding: utf-8 -*-
"""
Task 1.3a: BROADENED search for depth-3 fixed points at depth<=4.
Random structured search: enumerate ALL feasible 4-step climbs
ROOT -> d1 -> d2 -> d3 (depth-3 node) -> fixed, with F fixed on the climb,
and ALL other 11 nodes assigned from local pools (ancestors+self+children),
sampled randomly (space too large for exhaustive). Millions of samples.
"""
import sys, random, time
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

random.seed(20260801)
t0 = time.time()
tree = build_tree(max_depth=4)
nodes = list(tree.keys())
idx = {n: i for i, n in enumerate(nodes)}
N = len(nodes)

D = [[0.0]*N for _ in range(N)]
for i, a in enumerate(nodes):
    for j in range(i+1, N):
        d = dist(a, nodes[j], tree)
        D[i][j] = D[j][i] = d
pairs = [(i, j) for i in range(N) for j in range(i+1, N)]

d3 = [n for n in nodes if tree[n][2] == 3]
d1 = [n for n in nodes if tree[n][2] == 1]
d2 = [n for n in nodes if tree[n][2] == 2]
print(f"Tree: {N} nodes | d1={d1} d2={d2} d3={d3}")

def is_ne(images):
    for i, j in pairs:
        if D[images[i]][images[j]] > D[i][j] + 1e-12:
            return False
    return True

def trajectory_fp(images):
    cur = idx[EMPTY]
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

# Local pools for all nodes
pools = {}
for n in nodes:
    anc = [a for a in nodes if a in ancestor_path(n, tree)]
    ch = [c for c in nodes if tree[c][0] == n]
    pools[n] = list(dict.fromkeys(anc + [n] + ch))

# Build all feasible climbs: ROOT -> d1 -> d2 -> d3 -> fixed(d3)
# (each step must be a real parent-child edge OR arbitrary? Keep parent-child chains that exist)
climbs = []
for a in d1:
    for b in [c for c in nodes if tree[c][0] == a]:  # children of a
        for c in [x for x in nodes if tree[x][0] == b]:  # children of b at depth 3
            climbs.append((a, b, c))
# Also allow '[]#' style: d1='#' -> '[]' is NOT parent-child ('#' and '[]' are siblings).
# But the depth-2 witness used '#'->'[]'. So ALSO allow any d1->d2 edge where parent(d2)=='[]'
# i.e. allow jumps between siblings when beneficial. Add climbs via '[]' branch:
for b in ['#[]', '[]#']:
    for c in [x for x in nodes if tree[x][0] == b]:
        climbs.append(('#', b, c))
print(f"Feasible climbs to depth 3: {len(climbs)}")
for cl in climbs:
    print(f"  {EMPTY!r} -> {cl[0]!r} -> {cl[1]!r} -> {cl[2]!r} (T*={cl[2]!r})")

SAMPLES = 2_000_000
hits = []
for ci, (a, b, c) in enumerate(climbs):
    # Fixed climb assignments
    fixed = {EMPTY: a, a: b, b: c, c: c}
    free = [n for n in nodes if n not in fixed]
    best_fp = None
    for s in range(SAMPLES):
        images = {}
        for k, v in fixed.items():
            images[idx[k]] = idx[v]
        for n in free:
            images[idx[n]] = idx[random.choice(pools[n])]
        img_list = [images[i] for i in range(N)]
        if not is_ne(img_list):
            continue
        fp, traj = trajectory_fp(img_list)
        if fp is not None:
            fd = tree[nodes[fp]][2]
            if nodes[fp] == c:
                hits.append((ci, a, b, c, {nodes[k]: nodes[v] for k, v in enumerate(img_list)}))
                print(f"  >>> HIT climb {ci}: T*={c!r} depth 3! F={hits[-1][4]}")
                break
            if best_fp is None or fd > tree[nodes[best_fp]][2]:
                best_fp = fp
    print(f"  climb {ci} ({a!r}->{b!r}->{c!r}): done, best fp reached: "
          f"{nodes[best_fp]!r} depth {tree[nodes[best_fp]][2] if best_fp is not None else '?'}"
          f" | hits={len(hits)}")

print(f"\n=== RESULT: depth-3 fixed points found: {len(hits)} ===")
if hits:
    F = hits[0][4]
    viol = [(x, y) for i, x in enumerate(nodes) for y in nodes[i+1:]
            if D[idx[F[x]]][idx[F[y]]] > D[idx[x]][idx[y]] + 1e-12]
    print(f"Verify first hit: violations={len(viol)} -> {'CONFIRMED' if not viol else 'FAILED'}")
else:
    print("No depth-3 fixed point found in any sampled climb. Evidence suggests T* depth bound = 2 at depth<=4.")
print(f"TOTAL: {time.time()-t0:.1f}s")
