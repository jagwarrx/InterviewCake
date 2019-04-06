def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    
    if tree_root is None:
        return True
    
    nodeQ = [(tree_root, 0)]
    depths = []
    
    while len(nodeQ):
        
        last_node, depth = nodeQ.pop()
        
        if( not last_node.left ) and (not last_node.right ):
            if depth not in depths:
                depths.append(depth)
        
            if ((len(depths) > 1) and (max(depths) - min(depths) > 1)):
                return False
        else:
            
            if(last_node.left):
                nodeQ.append((last_node.left, depth + 1))
            if(last_node.right):
                nodeQ.append((last_node.right, depth + 1))
        
    return True
        
        
# store node pointer and depth as tuples
# pop together and store in variables node, depth
# append node.right, node.left
# put in while loop until list is empty
