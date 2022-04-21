class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if node == None:
        return '*'
    return node.val + '#'  + serialize( node.left) + "#" +  serialize( node.right)
    

    # return Node(None)
def deserialize(strs):
    return deserialize_aux(strs)[0]

def deserialize_aux(strs):
    if strs == "*":
        return None,None
    else :
        pos = strs.find('#')
        val = strs[0:pos]
        if val == '*':
            # this is the end of athe branch
            return None,strs[( pos + 1  ):]
        else: 
            (leftBranch, restStrs )=  deserialize_aux(strs[( pos + 1  ):])
            (rightBranch, restStrs) = deserialize_aux(restStrs)
            newNode = Node(val, leftBranch, rightBranch)
            return newNode,restStrs



node = Node('root', Node('left', Node('left.left')), Node('right'))

print('S--')
print(serialize( None))
print(serialize( Node('root')))
print(serialize( Node('root', Node('left'))))
print(serialize( Node('root', None , Node('right'))))
print(serialize( Node('root', Node('left'),  Node('right') )))
print(serialize( node))

print('D--')
print(serialize( deserialize (serialize( None))))
print(serialize( deserialize (serialize( Node('root')))))
print(serialize( deserialize ( serialize( Node('root', Node('left'))))))
print(serialize( deserialize (serialize( Node('root', None , Node('right'))))))
print(serialize( deserialize (serialize( Node('root', Node('left'),  Node('right') )))))
print(serialize( deserialize (serialize( node))))

