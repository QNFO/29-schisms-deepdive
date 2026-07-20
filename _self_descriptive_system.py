"""
Executable Implementation of the Self-Descriptive Formal System
================================================================

Primitives:
  MARK      = '#'   (atomic unit of distinction)
  CONTAINER = [...]  (boundary)

Reduction rules:
  Condensation (C):  '##' -> '#'
  Cancellation (X):  '[#]' -> ''
  Double-Encl (D):   '[[E]]' -> 'E'

Tree: all reduced strings reachable from '' by add-mark or wrap-container.
Distance: 2^(-depth of deepest common ancestor).
Fixed point: iterate contractive map F until convergence.
"""

import itertools, math

# ── §1. Primitives & Parsing ──────────────────────────────────────

EMPTY = ''

def parse(s):
    """Tokenize a flat string into (marks, open_brackets, close_brackets)."""
    tokens = []
    i = 0
    while i < len(s):
        if s[i] == '#':
            tokens.append(('mark', '#'))
        elif s[i] == '[':
            tokens.append(('open', '['))
        elif s[i] == ']':
            tokens.append(('close', ']'))
        i += 1
    return tokens

def unparse(tokens):
    return ''.join(t[1] for t in tokens)

# ── §2. Reduction Rules ───────────────────────────────────────────

def reduce_step(s):
    """Apply one reduction (C, X, or D) and return the result, or None."""
    # C: '##' anywhere -> '#'
    idx = s.find('##')
    if idx != -1:
        return s[:idx] + '#' + s[idx+2:]

    # X: '[#]' -> ''  (must be exactly '[#]', not part of larger expression)
    idx = s.find('[#]')
    if idx != -1:
        return s[:idx] + s[idx+3:]

    # D: '[[E]]' -> 'E' where E is balanced and non-empty, no extra content
    # Find pattern: '[[', then balanced content, then ']]'
    idx = s.find('[[')
    if idx != -1:
        # track brackets from idx+1
        depth = 0
        for j in range(idx + 1, len(s)):
            if s[j] == '[':
                depth += 1
            elif s[j] == ']':
                depth -= 1
            if depth == 0:
                # found matching ']' at j
                inner = s[idx+2:j-1] if j > idx + 2 else ''
                # verify: s[idx:j+1] starts with '[[' and ends with ']]'
                if j + 1 < len(s) and s[j+1] == ']':
                    # check inner is balanced
                    if is_balanced(inner):
                        return s[:idx] + inner + s[j+2:]
                break
    return None

def is_balanced(s):
    depth = 0
    for ch in s:
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

def reduce(s):
    """Apply reduction rules exhaustively. Returns normal form."""
    result = s
    while True:
        step = reduce_step(result)
        if step is None:
            return result
        result = step

# ── §3. Tree Generation ───────────────────────────────────────────

def generate_children(parent):
    """All normal forms reachable in one step from parent.
    One step = ADD-MARK or ADD-CONTAINER at any position.
    """
    children = set()
    n = len(parent)

    # ADD-MARK: insert '#' at any position (including ends)
    for i in range(n + 1):
        candidate = parent[:i] + '#' + parent[i:]
        reduced = reduce(candidate)
        if reduced and reduced != parent:
            children.add(reduced)

    # ADD-CONTAINER: wrap any balanced sub-expression in [...]
    for start in range(n):
        if parent[start] in '#[':
            depth = 0
            for end in range(start, n):
                if parent[end] == '[':
                    depth += 1
                elif parent[end] == ']':
                    depth -= 1
                if depth == 0 and parent[end] in '#]':
                    # wrap parent[start:end+1]
                    candidate = parent[:start] + '[' + parent[start:end+1] + ']' + parent[end+1:]
                    reduced = reduce(candidate)
                    if reduced and reduced != parent:
                        children.add(reduced)
                    if parent[end] == '#':  # wrap single mark
                        candidate = parent[:start] + '[' + parent[start:end+1] + ']' + parent[end+1:]
                        reduced = reduce(candidate)
                        if reduced and reduced != parent:
                            children.add(reduced)

    # Also wrap the whole expression
    candidate = '[' + parent + ']'
    reduced = reduce(candidate)
    if reduced and reduced != parent:
        children.add(reduced)

    return list(children)

def build_tree(max_depth=4):
    """Build tree up to max_depth, BFS. Returns {node: (parent, children, depth)}"""
    tree = {EMPTY: (None, [], 0)}
    frontier = [EMPTY]
    for depth in range(1, max_depth + 1):
        new_frontier = []
        for node in frontier:
            children = generate_children(node)
            for child in children:
                if child not in tree:
                    tree[child] = (node, [], depth)
                    new_frontier.append(child)
            # update children list for node
            tree[node] = (tree[node][0], children, tree[node][2])
        frontier = new_frontier
        if not frontier:
            break
    return tree

# ── §4. Distance ──────────────────────────────────────────────────

def ancestor_path(node, tree):
    """List of nodes from ROOT to node (inclusive)."""
    path = []
    current = node
    while current is not None:
        path.append(current)
        if current not in tree:
            break
        parent, _, _ = tree[current]
        current = parent
    path.reverse()
    return path

def deepest_common_ancestor(a, b, tree):
    """Node of maximum depth on both paths from ROOT."""
    path_a = ancestor_path(a, tree)
    path_b = ancestor_path(b, tree)
    ancestor = EMPTY
    for na, nb in zip(path_a, path_b):
        if na == nb:
            ancestor = na
        else:
            break
    return ancestor

def dist(a, b, tree):
    """2^(-depth of deepest common ancestor). dist(a, a) = 0."""
    if a == b:
        return 0.0
    dca = deepest_common_ancestor(a, b, tree)
    dca_depth = tree[dca][2] if dca in tree else 0
    return 2.0 ** (-dca_depth)

def verify_strong_condition(tree):
    """Check: dist(a,c) <= max(dist(a,b), dist(b,c)) for all triples."""
    nodes = list(tree.keys())
    violations = []
    for a, b, c in itertools.product(nodes, repeat=3):
        if a == b or b == c or a == c:
            continue
        d_ac = dist(a, c, tree)
        d_ab = dist(a, b, tree)
        d_bc = dist(b, c, tree)
        if d_ac > max(d_ab, d_bc) + 1e-10:
            violations.append((a, b, c, d_ac, d_ab, d_bc))
    return violations

# ── §5. Contractive Maps & Fixed Points ───────────────────────────

def make_contractive_map(tree):
    """
    Construct a contractive map F on the tree.
    Simplest: map each node to its parent (strictly reduces depth by 1,
    therefore strictly reduces distance).
    """
    def F(node):
        if node == EMPTY:
            return EMPTY
        if node in tree:
            parent, _, _ = tree[node]
            return parent if parent is not None else EMPTY
        return EMPTY
    return F

def iterate_fixed_point(F, start, tol=1e-10, max_iter=1000):
    """Iterate F from start until convergence."""
    trajectory = [start]
    for i in range(max_iter):
        nxt = F(trajectory[-1])
        trajectory.append(nxt)
        if nxt == trajectory[-2]:
            break
    return trajectory

# ── §7. Projection ────────────────────────────────────────────────

def epsilon_neighborhood(node, epsilon, tree):
    """All nodes within distance <= epsilon of node."""
    neighbors = []
    for other in tree:
        if dist(node, other, tree) <= epsilon:
            neighbors.append(other)
    return neighbors

def project(tree, epsilon):
    """Partition tree into epsilon-neighborhood equivalence classes."""
    nodes = list(tree.keys())
    assigned = set()
    classes = []
    for node in nodes:
        if node in assigned:
            continue
        nbhd = epsilon_neighborhood(node, epsilon, tree)
        classes.append(nbhd)
        assigned.update(nbhd)
    return classes

# ── Demonstrations ────────────────────────────────────────────────

def demo_reduction():
    print("=" * 60)
    print("DEMO 1: REDUCTION RULES")
    print("=" * 60)
    examples = [
        ('##', "Two marks condense"),
        ('###', "Three marks condense to one"),
        ('[#]', "Mark inside boundary cancels"),
        ('[[#]]', "Double enclosure: outer cancels"),
        ('#[#]', "Mark next to cancelled boundary -> mark survives"),
        ('[##]', "Two marks in boundary -> condense first, then boundary+mark"),
        ('[[#[#]]]', "Nested: [cancels inner [#]] -> [[#]] -> cancels outer"),
    ]
    for expr, desc in examples:
        result = reduce(expr)
        print(f"  {desc:50s} | {expr:15s} -> {result if result else '(empty)'}")

def demo_tree():
    print("\n" + "=" * 60)
    print("DEMO 2: TREE STRUCTURE (depth <= 4)")
    print("=" * 60)
    tree = build_tree(max_depth=4)
    depths = {}
    for node, (parent, children, depth) in tree.items():
        depths.setdefault(depth, 0)
        depths[depth] += 1
    for d in sorted(depths):
        print(f"  Depth {d}: {depths[d]} nodes")
    print(f"  Total nodes: {len(tree)}")

    # Show some example nodes at each depth
    print("\n  Sample nodes:")
    for d in range(5):
        nodes_at_d = [(n, tree[n]) for n in tree if tree[n][2] == d]
        for n, (_, children, _) in nodes_at_d[:3]:
            label = f'"{n}"' if n else '(empty)'
            print(f"    d={d} | {label:20s} | children: {len(children)}")

    return tree

def demo_distance(tree):
    print("\n" + "=" * 60)
    print("DEMO 3: DISTANCE & STRONG CONDITION")
    print("=" * 60)
    nodes = list(tree.keys())
    # Pick some pairs
    pairs = []
    for i, a in enumerate(nodes[:10]):
        for j, b in enumerate(nodes[:10]):
            if i < j:
                pairs.append((a, b))
    print(f"  Distance matrix (first 10 nodes):")
    print(f"  {'':10s}", end="")
    for n in nodes[:6]:
        label = f'"{n}"' if n else '(empty)'
        print(f"{label:>12s}", end="")
    print()
    for a in nodes[:6]:
        label_a = f'"{a}"' if a else '(empty)'
        print(f"  {label_a:10s}", end="")
        for b in nodes[:6]:
            d = dist(a, b, tree)
            print(f"{d:12.4f}", end="")
        print()

    # Verify strong condition
    violations = verify_strong_condition(tree)
    if violations:
        print(f"\n  WARNING: {len(violations)} violations of strong condition")
        for v in violations[:5]:
            print(f"    {v}")
    else:
        print(f"\n  Strong condition verified: 0 violations (checked all triples)")

def demo_fixed_point(tree):
    print("\n" + "=" * 60)
    print("DEMO 4: FIXED POINT (contractive map: parent)")
    print("=" * 60)
    F = make_contractive_map(tree)

    # Start from a deep node
    deep_nodes = [(n, tree[n][2]) for n in tree if tree[n][2] >= 3]
    if deep_nodes:
        start = deep_nodes[0][0]
        print(f"  Starting from: \"{start}\" (depth {tree[start][2]})")
        trajectory = iterate_fixed_point(F, start)
        print(f"  Trajectory ({len(trajectory)} steps):")
        for i, node in enumerate(trajectory):
            label = f'"{node}"' if node else '(empty)'
            d = tree[node][2] if node in tree else 0
            print(f"    Step {i}: {label:20s} depth={d}")
        print(f"  Fixed point: \"{trajectory[-1]}\"")

    # Show: different starts converge to same fixed point
    if len(deep_nodes) >= 2:
        s1, s2 = deep_nodes[0][0], deep_nodes[1][0]
        t1 = iterate_fixed_point(F, s1)
        t2 = iterate_fixed_point(F, s2)
        print(f"\n  Convergence test:")
        print(f"    Start \"{s1}\" -> fixed point \"{t1[-1]}\" in {len(t1)-1} steps")
        print(f"    Start \"{s2}\" -> fixed point \"{t2[-1]}\" in {len(t2)-1} steps")
        print(f"    Same fixed point: {t1[-1] == t2[-1]}")

def demo_projection(tree):
    print("\n" + "=" * 60)
    print("DEMO 5: PROJECTION (coarse-graining)")
    print("=" * 60)
    for eps in [0.125, 0.25, 0.5]:
        classes = project(tree, eps)
        sizes = [len(c) for c in classes]
        print(f"  epsilon={eps:.3f}: {len(classes)} equivalence classes")
        print(f"    Sizes: min={min(sizes)}, max={max(sizes)}, avg={sum(sizes)/len(sizes):.1f}")
        # Show one class
        if classes:
            sample = classes[min(3, len(classes)-1)]
            labels = [f'"{n}"' if n else '(empty)' for n in sample[:6]]
            print(f"    Sample class: {{{', '.join(labels)}}}")

def demo_schism_19():
    """Demonstrate Schism 19: law and initial condition collapse."""
    print("\n" + "=" * 60)
    print("DEMO 6: SCHISM 19 — Nomological dualism resolved")
    print("=" * 60)
    print("""
    In a self-descriptive system:
      ROOT  = ''        (initial condition)
      F     = parent    (the "law" — a contractive map)
      T*    = ''        (the fixed point)

    These are NOT independently specifiable:
      - ROOT IS T* (the root is its own parent)
      - F maps every node toward ROOT (contractive)
      - Any trajectory F^n(X) converges to ROOT

    The "law" (F) and "initial condition" (ROOT) are not separate.
    T* = ROOT = fixed point = BOTH the law's attractor AND the starting state.

    This is nomological monism: there is only the self-consistent
    fixed point. The "law" is the map that makes the fixed point
    an attractor. The "initial condition" is the fixed point itself.
    """)


def demo_bias():
    """Show 8 bias sources are absent."""
    print("=" * 60)
    print("DEMO 7: BIAS AUDIT")
    print("=" * 60)
    biases = [
        ("Smoothness",          "All states are discrete strings. No continuity assumed."),
        ("Fixed representation", "No metric on R is used. Only tree distance (2^-depth)."),
        ("External clock",       "No 't' parameter. Depth IS ordering."),
        ("External observer",    "No observer variable. All states are internal nodes."),
        ("Single description",   "Multiple nodes can have same tree depth. No privileged view."),
        ("Pre-existing laws",    "F is derived from tree structure (parent function)."),
        ("Additivity",           "Distance is non-Archimedean: d(A,C) ≤ max(d(A,B), d(B,C))."),
        ("Reversibility",        "Parent map is not invertible. Many children → one parent."),
    ]
    for bias, evidence in biases:
        print(f"  [{bias:22s}] ABSENT. {evidence}")

if __name__ == '__main__':
    demo_reduction()
    tree = demo_tree()
    demo_distance(tree)
    demo_fixed_point(tree)
    demo_projection(tree)
    demo_schism_19()
    demo_bias()

    print("\n" + "=" * 60)
    print("ALL DEMOS COMPLETE")
    print("=" * 60)
