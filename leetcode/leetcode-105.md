## 105. Construct Binary Tree From Preorder and Inorder Traversal

[leetcode link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### Notes

use the first element on the `preorder` as the Tree root and pop it from the `preorder` list to do not
consider it on future iterations

use the `inorder` array to know which elements are on the left side of root and also on the right
side of the root, e. g., if `7` is the Tree root and the `inorder` array looks like this `[3, 7, 9]`
then:

- `3` is on the left side of `7`
- `9` is on the right side of `7`

we calculate the left subtree and the right subtree in function of `i`, which is the index
from the current node in the iteration (root)

before travel to the rest of the nodes using the recursive functions, we remove the node from the
`inorder` list

### Source code (watch it only if we can't find the solution)

<details>
    <summary>Solution </summary>

```python
class Solution:
    def build_bst(self, preorder: List[int], inorder: List[int], subtree: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return

        node = preorder.pop(0)
        n_n: TreeNode = TreeNode(node)

        if len(subtree) == 1:
            inorder.remove(node)

            return n_n

        i: int = inorder.index(node)

        t_left: List[int] = subtree[:i]
        t_right: List[int] = subtree[i+1:]
        inorder.remove(node)

        if len(t_left) > 0:
            n_n.left = self.build_bst(preorder, inorder, t_left)

        if len(t_right) > 0:
            n_n.right = self.build_bst(preorder, inorder, t_right)

        return n_n
        
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        subtree: List = inorder

        return self.build_bst(preorder, inorder, subtree)
```

</details>
