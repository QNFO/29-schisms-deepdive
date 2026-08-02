# -*- coding: utf-8 -*-
"""
Task 1.4a/1.4b Comparative Analysis — verify branching invariance, image cardinality,
idempotent core growth, and fiber collapse patterns across both witness maps.
"""
import sys
sys.path.insert(0, r'C:\Users\LENOVO\Projects\29-schisms-task13')
from _self_descriptive_system import build_tree, dist, ancestor_path, EMPTY
from collections import defaultdict

tree2 = build_tree(max_depth=3)
tree4 = build_tree(max_depth=4)

F2 = {
    '': '#', '#': '[]', '[]': '[]#', '[]#': '[]#',
    '#[]': '[]', '[[]#]': '[[]#]', '#[]#': '[]#', '[#[]]': '[]',
}

F3 = {
    '': '[]', '[]': '[]#', '[]#': '[[]#]', '[[]#]': '[[]#]',
    '#': '#', '#[]': '[#[]]', '#[]#': '#[]#', '[#[]]': '[[#[]]]',
    '[#[]#]': '[#[]#]', '[[[]]#]': '[[[]]#]', '[[]#]#': '[[]#]',
    '#[[]#]': '[[]#]', '[#[]]#': '[#[]]#', '#[#[]]': '[#[]]',
    '[[#[]]]': '[#[]]',
}

def compute_metrics(F, tree, label):
    nodes = sorted(tree.keys(), key=lambda n: (tree[n][2], n))
    
    # T* find
    cur = EMPTY
    seen = set()
    Tstar = None
    for _ in range(50):
        if cur in seen and Tstar is None:
            Tstar = cur
            break
        seen.add(cur)
        cur = F[cur]
    if Tstar is None:
        Tstar = cur
    
    # Image
    image = set(F.values())
    
    # Preimage
    pre = defaultdict(list)
    for n in nodes:
        pre[F[n]].append(n)
    
    # Idempotent core
    idem = [n for n in nodes if F[n] == n]
    
    # Fiber collapse ratio (max)
    max_collapse = max(len(v) for v in pre.values())
    
    # Branching at T*
    Tstar_children = [n for n in nodes if tree[n][0] == Tstar]
    
    # Depth distribution of surviving nodes
    surv_depth = defaultdict(int)
    for n in image:
        surv_depth[tree[n][2]] += 1
    
    td = defaultdict(int)
    for n in nodes:
        td[tree[n][2]] += 1
    
    return {
        'label': label,
        'Tstar': Tstar,
        'Tstar_depth': tree[Tstar][2],
        'nodes': len(nodes),
        'image': len(image),
        'idempotent': len(idem),
        'max_collapse': max_collapse,
        'branching': len(Tstar_children),
        'surv_depth': dict(sorted(surv_depth.items())),
        'tree_depth': dict(sorted(td.items())),
        'preimage_sizes': {k: len(v) for k, v in sorted(pre.items(), key=lambda x: (tree[x[0]][2], x[0]))},
    }

m2 = compute_metrics(F2, tree2, "Depth-2 Witness (T*='[]#')")
m3 = compute_metrics(F3, tree4, "Depth-3 Witness (T*='[[]#]')")

for m in [m2, m3]:
    print(f"\n{m['label']}")
    print(f"  T*={m['Tstar']!r} depth={m['Tstar_depth']}")
    print(f"  Nodes: {m['nodes']} | Image: {m['image']} ({100.0*m['image']/m['nodes']:.1f}%)")
    print(f"  Idempotent core: {m['idempotent']} ({100.0*m['idempotent']/m['nodes']:.1f}%)")
    print(f"  Max fiber collapse: {m['max_collapse']}:1")
    print(f"  T* branching: {m['branching']}")
    print(f"  Surviving by depth: {m['surv_depth']}")
    print(f"  Preimage sizes: {m['preimage_sizes']}")

print(f"\n=== COMPARISON ===")
print(f"Branching invariance: {m2['branching']} == {m3['branching']} = {m2['branching'] == m3['branching']}")
print(f"Max collapse invariance: {m2['max_collapse']} == {m3['max_collapse']} = {m2['max_collapse'] == m3['max_collapse']}")
print(f"Image ratio scaling: {m2['image']/m2['nodes']:.2f} -> {m3['image']/m3['nodes']:.2f}")
print(f"Idempotent ratio scaling: {m2['idempotent']/m2['nodes']:.2f} -> {m3['idempotent']/m3['nodes']:.2f}")
print(f"\nDone.")
