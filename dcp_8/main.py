class Node:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def get_num_unival_subtree(self):
        return self.get_num_unival_subtree_h(self, self.val)

        pass
    def get_num_unival_subtree_h(self, node, last_val):
        if node is None:
            return 0;
        elif node.val != last_val:
            return  self.get_num_unival_subtree_h(node.left,node.val) + self.get_num_unival_subtree_h(node.right,node.val)
        else:
            return 1 + self.get_num_unival_subtree_h(node.left,node.val) + self.get_num_unival_subtree_h(node.right,node.val)

        return 0;






    def __str__(self):
        return ""
        pass


nodito2 =  Node('0',
                Node('1',
                     Node('a1'),
                     Node('a2'),
                     ),
                Node('b2',
                     Node('a3'),
                     Node('a4'),
                     ),
                )
nodito = Node (0,
               Node(1),
               Node(0, 
                    Node(1,
                         Node(1),
                         Node(1)
                         ),
                    Node(0)
                    )
               )
print(nodito.get_num_unival_subtree())

