## 297. Serialize and Deserialize Binary Tree

## Source code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def traversal(self, root, string_tree: List[str]) -> None:
        if root == None:
            string_tree.append('#')
            return None

        string_tree.append(str(root.val))
        
        self.traversal(root.left, string_tree)
        
        self.traversal(root.right, string_tree)


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string_tree_list: List[str] = []
        self.traversal(root, string_tree_list)
        string_tree = ' '.join(string_tree_list)

        return string_tree
        

    def traversal_to_tree(self, data: List[str]) -> TreeNode:
        if len(data) == 0:
            return None
        
        val = data.pop(0)
        if val == '#':
            return None

        node: TreeNode = TreeNode(int(val))
        node.left = self.traversal_to_tree(data)
        node.right = self.traversal_to_tree(data)

        return node


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_split: List[str] = data.split()
        print('data_split', data_split)
        root: TreeNode = self.traversal_to_tree(data_split)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```
