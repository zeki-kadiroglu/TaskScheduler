from typing import Any


class TreeNode:
    def __init__(self, payload: Any):
        self.payload = payload
        self.children = []

    def add_child(self, child: Any):
        self.children.append(child)