# -*- coding: utf-8 -*-
"""
INDEPENDENT VERIFICATION of the depth-3 fixed-point hit (Task 1.3a).
Climb 0 hit: T*='[[]#]' via ''->'[]'->'[]#'->'[[]#]'.
Checks ALL 105 pairs with explicit dist(); prints trajectory; confirms fixed point.
"""
import sys
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

tree = build_tree(max_depth=4)
nodes = list(tree.keys())
print(f"Tree depth<=4: {len(nodes)} nodes\n")

F = {
    '':       '[]',
    '[]':     '[]#',
    '[]#':    '[[]#]',
    '[[]#]':  '[[]#]',    # fixed point at depth 3
    '#':      '#',
    '#[]':    '[#[]]',
    '#[]#':   '#[]#',
    '[#[]]':  '[[#[]]]',
    '[#[]#]': '[#[]#]',
    '[[[]]#]': '[[[]]#]',
    '[[]#]#': '[[]#]',
    '#[[]#]': '[[]#]',
    '[#[]]#': '[#[]]#',
    '#[#[]]': '[#[]]',
    '[[#[]]]': '[#[]]',
}

# 1. Well-defined
ok = all(k in tree and v in tree for k, v in F.items())
print(f"[1] All images in TREE: {ok}")

# 2. Pair-by-pair non-expansiveness (ALL 105 pairs)
print("\n[2] Pair-by-pair non-expansiveness audit:")
viol = []
for i, a in enumerate(nodes):
    for b in nodes[i+1:]:
        d_ab = dist(a, b, tree)
        d_f = dist(F[a], F[b], tree)
        if d_f > d_ab + 1e-12:
            viol.append((a, b, d_ab, d_f))
print(f"    Pairs checked: {len(nodes)*(len(nodes)-1)//2}")
print(f"    Violations: {len(viol)}")
for v in viol:
    print(f"      {v[0]!r},{v[1]!r}: dist={v[2]:.4f} F->dist={v[3]:.4f} ***")

# 3. Trajectory from ROOT
print("\n[3] Trajectory from ROOT:")
cur = EMPTY
traj = []
seen = set()
for i in range(20):
    traj.append(cur)
    if cur in seen:
        break
    seen.add(cur)
    cur = F[cur]
print(f"    {' -> '.join(repr(t) for t in traj)}")
fp = traj[-1]
fd = tree[fp][2] if fp in tree else 0
print(f"    Fixed point: {fp!r} at depth {fd}")
print(f"    Non-trivial (not ROOT, not '#', not '[]'): {fp not in (EMPTY, '#', '[]')}")

print("\n" + "="*60)
if not viol:
    print("VERDICT: NON-EXPANSIVE CONFIRMED (0/105 violations)")
else:
    print(f"VERDICT: NOT NON-EXPANSIVE ({len(viol)} violations) — hit INVALID")
if fd == 3 and not viol:
    print("=> DEPTH-3 FIXED POINT EXISTS at tree depth<=4 — open sub-question 8.4 RESOLVED")
print("="*60)
