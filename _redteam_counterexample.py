# -*- coding: utf-8 -*-
"""
RED TEAM AUDIT — Independent pair-by-pair verification of the T6.1 counterexample.
Prints EVERY pair with original distance and image distance. No summary claims.
"""
import sys, itertools
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY

tree = build_tree(max_depth=3)
nodes = sorted(tree.keys(), key=lambda n: (tree[n][2], n))
print(f"Tree depth<=3: {len(nodes)} nodes")
for n in nodes:
    p = tree[n][0]
    print(f"  node={n!r:8s} depth={tree[n][2]} parent={p!r}")

# The claimed counterexample map
F = {
    '':       '#',
    '#':      '[]',
    '[]':     '[]#',
    '[]#':    '[]#',
    '#[]':    '[]',
    '[[]#]':  '[[]#]',
    '#[]#':   '[]#',
    '[#[]]':  '[]',
}

print("\n=== PAIR-BY-PAIR DISTANCE AUDIT ===")
violations = []
n_checked = 0
for i, a in enumerate(nodes):
    for b in nodes[i+1:]:
        n_checked += 1
        d_ab = dist(a, b, tree)
        fa, fb = F[a], F[b]
        d_f = dist(fa, fb, tree)
        ok = d_f <= d_ab + 1e-12
        flag = "" if ok else "  <<< VIOLATION"
        if not ok:
            violations.append((a, b, d_ab, fa, fb, d_f))
        print(f"  ({a!r:6s},{b!r:6s}) dist={d_ab:.4f}  F->({fa!r:6s},{fb!r:6s}) fdist={d_f:.4f}  {'OK' if ok else '*** VIOLATION ***'}")

print(f"\nPairs checked: {n_checked}")
print(f"Violations: {len(violations)}")
for v in violations:
    print(f"  {v[0]!r}->{v[4]!r}, {v[1]!r}->{v[4]!r}: dist={v[2]:.4f}, fdist={v[5]:.4f}")
