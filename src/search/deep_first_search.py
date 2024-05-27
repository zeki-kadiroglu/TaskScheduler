from typing import Any

from src.node_tree import TreeNode
from src.search.base import BaseTree

class DeepFirstSearch(BaseTree):
    def __init__(self, root_payload: Any):
        self.root = TreeNode(root_payload)

    def iterate_tasks(self):
        def dfs(node):
            # visited node
            yield node.payload
            # iterate children of current node
            for child in node.children:
                # continues through the children of current node
                yield from dfs(child)
        return dfs(self.root)