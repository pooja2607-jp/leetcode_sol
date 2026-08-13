class SegmentTree:

  def __init__(self, s: str):
    self.n = len(s)
    self.s = list(s)

    # Tree arrays
    self.max_len = [0] * (4 * self.n)
    self.prefix_len = [0] * (4 * self.n)
    self.suffix_len = [0] * (4 * self.n)
    self.left_char = [''] * (4 * self.n)
    self.right_char = [''] * (4 * self.n)

    self._build(1, 0, self.n - 1)

  def _merge(self, node: int, l_len: int, r_len: int):
    left_child = 2 * node
    right_child = 2 * node + 1

    self.left_char[node] = self.left_char[left_child]
    self.right_char[node] = self.right_char[right_child]

    # Base maximum from both halves
    self.max_len[node] = max(
        self.max_len[left_child], self.max_len[right_child]
    )

    # Defaults for prefix and suffix
    self.prefix_len[node] = self.prefix_len[left_child]
    self.suffix_len[node] = self.suffix_len[right_child]

    # Cross-boundary condition
    if self.right_char[left_child] == self.left_char[right_child]:
      cross_len = self.suffix_len[left_child] + self.prefix_len[right_child]
      self.max_len[node] = max(self.max_len[node], cross_len)

      # Extend prefix if left child is entirely uniform
      if self.prefix_len[left_child] == l_len:
        self.prefix_len[node] = l_len + self.prefix_len[right_child]

      # Extend suffix if right child is entirely uniform
      if self.suffix_len[right_child] == r_len:
        self.suffix_len[node] = r_len + self.suffix_len[left_child]

  def _build(self, node: int, start: int, end: int):
    if start == end:
      char = self.s[start]
      self.max_len[node] = 1
      self.prefix_len[node] = 1
      self.suffix_len[node] = 1
      self.left_char[node] = char
      self.right_char[node] = char
      return

    mid = (start + end) // 2
    self._build(2 * node, start, mid)
    self._build(2 * node + 1, mid + 1, end)

    l_len = mid - start + 1
    r_len = end - mid
    self._merge(node, l_len, r_len)

  def update(self, node: int, start: int, end: int, idx: int, ch: str):
    if start == end:
      self.s[idx] = ch
      self.left_char[node] = ch
      self.right_char[node] = ch
      return

    mid = (start + end) // 2
    if idx <= mid:
      self.update(2 * node, start, mid, idx, ch)
    else:
      self.update(2 * node + 1, mid + 1, end, idx, ch)

    l_len = mid - start + 1
    r_len = end - mid
    self._merge(node, l_len, r_len)


class Solution:

  def longestRepeating(
      self, s: str, queryCharacters: str, queryIndices: list[int]
  ) -> list[int]:
    tree = SegmentTree(s)
    ans = []

    for char, idx in zip(queryCharacters, queryIndices):
      tree.update(1, 0, len(s) - 1, idx, char)
      # Root node (node 1) holds the max length for the full range [0, n - 1]
      ans.append(tree.max_len[1])

    return ans