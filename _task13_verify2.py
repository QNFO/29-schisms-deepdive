"""
Task 1.3 Numerical Verification — OPTIMIZED
Precomputes distance matrix; exhaustive search becomes O(N^2) per map with
O(1) distance lookups. 823K maps on 8 nodes: ~10s.
"""
import sys, itertools, math, random, time
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

def is_ancestor(a, b, tree):
    if a == b:
        return True
    return a in ancestor_path(b, tree)

def precompute(tree):
    """Return (nodes, idx, D, anc). D: distance matrix. anc: dict node->set of ancestors."""
    nodes = list(tree.keys())
    idx = {n: i for i, n in enumerate(nodes)}
    N = len(nodes)
    D = [[0.0]*N for _ in range(N)]
    anc = {}
    for i, a in enumerate(nodes):
        anc[a] = frozenset(n for n in nodes if is_ancestor(n, a, tree))
        for j in range(i+1, N):
            d = dist(a, nodes[j], tree)
            D[i][j] = D[j][i] = d
    return nodes, idx, D, anc

def make_ne_checker(idx, D):
    """Return fast non-expansiveness checker for a map given as tuple of images."""
    N = len(idx)
    pairs = [(i, j) for i in range(N) for j in range(i+1, N)]
    def is_ne(images):
        for i, j in pairs:
            if D[images[i]][images[j]] > D[i][j] + 1e-12:
                return False
        return True
    return is_ne, pairs

print("=" * 70)
print("TASK 1.3 NUMERICAL VERIFICATION (OPTIMIZED)")
print("=" * 70)

t0 = time.time()
tree3 = build_tree(max_depth=3)
tree4 = build_tree(max_depth=4)
print(f"\nTree depth<=3: {len(tree3)} nodes | depth<=4: {len(tree4)} nodes")

nodes3, idx3, D3, anc3 = precompute(tree3)
nodes4, idx4, D4, anc4 = precompute(tree4)
print(f"Precompute done in {time.time()-t0:.2f}s")

N3 = len(nodes3)
# Images are indices; map tuples of length N3
is_ne3, pairs3 = make_ne_checker(idx3, D3)

# ═══════════════════════════════════════════════════════════════
# T4.1: Royden Obstruction — enumerate ALL ancestor-monotone maps
print("\n" + "=" * 70)
print("VERIFY T4.1: ROYDEN OBSTRUCTION (ancestor-monotone traps ROOT)")
print("=" * 70)
t1 = time.time()
root_idx = idx3[EMPTY]
# For each node, ancestor options (as indices)
am_options = []
for n in nodes3:
    am_options.append([idx3[a] for a in anc3[n]])
count_am = 0
count_root_fixed = 0
count_am_ne = 0
for combo in itertools.product(*am_options):
    count_am += 1
    if combo[root_idx] == root_idx:
        count_root_fixed += 1
    if is_ne3(combo):
        count_am_ne += 1
print(f"Ancestor-monotone maps (depth<=3): {count_am} ({time.time()-t1:.2f}s)")
print(f"  F(ROOT)=ROOT: {count_root_fixed} ({100.0*count_root_fixed/count_am:.2f}%)")
print(f"  Royden Obstruction CONFIRMED: {count_root_fixed == count_am}")
print(f"  Ancestor-monotone AND non-expansive: {count_am_ne}")

# ═══════════════════════════════════════════════════════════════
# SINGLE COMBINED PASS: T6.1 + T4.2 + T3.2 stats from one 7^7 enumeration
# (sibling pairs + contractive checker definitions first)
from collections import defaultdict
by_parent = defaultdict(list)
for n in nodes3:
    p = tree3[n][0]
    if p is not None:
        by_parent[p].append(n)
sib_pairs = []
for p, kids in by_parent.items():
    for i, k1 in enumerate(kids):
        for k2 in kids[i+1:]:
            sib_pairs.append((idx3[k1], idx3[k2]))

def is_contractive_fast(images):
    for i, j in pairs3:
        if images[i] != images[j]:
            if D3[images[i]][images[j]] >= D3[i][j] - 1e-12:
                return False
    return True

print("\n" + "=" * 70)
print("VERIFY T6.1 + T4.2 + T3.2 (single combined 7^7 pass)")
print("=" * 70)
t2 = time.time()
all_maps = N3 ** N3
nontrivial_hits = 0
ne_count = 0
fp_dist = {}
ne_nonroot = 0
depth_of_root_images = {}
cont_count = 0
t32_viol = 0
bullet = [n for n in nodes3 if n == '#']
bullet_idx = idx3[bullet[0]] if bullet else None

for combo in itertools.product(range(N3), repeat=N3):
    if is_ne3(combo):
        ne_count += 1
        # T6.1: fixed point from ROOT
        cur = root_idx
        seen = set()
        fp = None
        for _ in range(100):
            nxt = combo[cur]
            if nxt == cur:
                fp = cur
                break
            if nxt in seen:
                break
            seen.add(nxt)
            cur = nxt
        if fp is not None:
            fd = tree3[nodes3[fp]][2]
            fp_dist[fd] = fp_dist.get(fd, 0) + 1
            if fp != root_idx and fp != bullet_idx and fd >= 2:
                nontrivial_hits += 1
                if nontrivial_hits <= 5:
                    mapping = {nodes3[i]: nodes3[v] for i, v in enumerate(combo)}
                    print(f"  T6.1 HIT: fp={nodes3[fp]!r} depth={fd} F={mapping}")
        # T4.2: F(ROOT) != ROOT depth distribution
        if combo[root_idx] != root_idx:
            ne_nonroot += 1
            d = tree3[nodes3[combo[root_idx]]][2]
            depth_of_root_images[d] = depth_of_root_images.get(d, 0) + 1
    # T3.2: contractive maps collapse siblings
    if cont_count < 50000:
        if is_contractive_fast(combo):
            cont_count += 1
            for s1, s2 in sib_pairs:
                if combo[s1] != combo[s2]:
                    t32_viol += 1
                    if t32_viol <= 3:
                        print(f"  T3.2 VIOLATION: sibs {nodes3[s1]!r},{nodes3[s2]!r} -> {nodes3[combo[s1]]!r},{nodes3[combo[s2]]!r}")
                    break
print(f"Exhaustive {all_maps} maps in {time.time()-t2:.2f}s")
print(f"  Non-expansive maps: {ne_count}")
print(f"  Fixed-point depth distribution: {dict(sorted(fp_dist.items()))}")
print(f"  T6.1: {'CONFIRMED (no non-trivial fixed point depth>=2 from ROOT)' if nontrivial_hits == 0 else 'REFUTED (' + str(nontrivial_hits) + ' counterexamples)'}")
print(f"  T4.2 depth distribution of F(ROOT): {dict(sorted(depth_of_root_images.items()))}")
maxd = max(depth_of_root_images.keys()) if depth_of_root_images else 0
print(f"  T4.2: {'CONFIRMED (max F(ROOT) depth <= 1)' if maxd <= 1 else 'REFUTED (max depth ' + str(maxd) + ')'}")
print(f"  T3.2 contractive maps checked: {cont_count}, sibling-collapse violations: {t32_viol}")
print(f"  T3.2: {'CONFIRMED' if t32_viol == 0 else 'REFUTED'}")

# ═══════════════════════════════════════════════════════════════
# T3.1: DCA Preservation iff condition (random ancestor-monotone maps)
print("\n" + "=" * 70)
print("VERIFY T3.1: DCA PRESERVATION (iff)")
print("=" * 70)
random.seed(42)
mismatch = 0
tested = 0
for _ in range(5000):
    images = tuple(random.choice([idx3[a] for a in anc3[n]]) for n in nodes3)
    # check iff for all pairs
    for i, j in pairs3:
        # d = depth of DCA
        pa = ancestor_path(nodes3[i], tree3)
        pb = ancestor_path(nodes3[j], tree3)
        d = 0
        for na, nb in zip(pa, pb):
            if na == nb:
                d = tree3[na][2]
            else:
                break
        cond = (tree3[nodes3[images[i]]][2] >= d) and (tree3[nodes3[images[j]]][2] >= d)
        ne = D3[images[i]][images[j]] <= D3[i][j] + 1e-12
        tested += 1
        if cond != ne:
            mismatch += 1
            if mismatch <= 3:
                print(f"  MISMATCH: A={nodes3[i]!r} B={nodes3[j]!r} cond={cond} ne={ne}")
print(f"T3.1 tested pairs: {tested}, mismatches: {mismatch}")
print(f"  T3.1 DCA Preservation: {'CONFIRMED' if mismatch == 0 else 'REFUTED'}")

# ═══════════════════════════════════════════════════════════════
# T4.2: Fixed-Point Depth Bound (non-expansive, F(ROOT)!=ROOT)
print("\n" + "=" * 70)
print("VERIFY T4.2: FIXED-POINT DEPTH BOUND")
print("=" * 70)
depth_of_root_images = {}
ne_nonroot = 0
for combo in itertools.product(range(N3), repeat=N3):
    if combo[root_idx] == root_idx:
        continue
    if not is_ne3(combo):
        continue
    ne_nonroot += 1
    d = tree3[nodes3[combo[root_idx]]][2]
    depth_of_root_images[d] = depth_of_root_images.get(d, 0) + 1
    if ne_nonroot >= 100000:
        break
print(f"Non-expansive maps with F(ROOT)!=ROOT (cap 100k): {ne_nonroot}")
print(f"Depth distribution of F(ROOT): {dict(sorted(depth_of_root_images.items()))}")
maxd = max(depth_of_root_images.keys()) if depth_of_root_images else 0
print(f"  T4.2 (max depth <= 1): {'CONFIRMED' if maxd <= 1 else 'REFUTED'}")

# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("TOTAL TIME:", f"{time.time()-t0:.2f}s")
print("=" * 70)
print("Done.")
