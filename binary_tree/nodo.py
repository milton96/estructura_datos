class Nodo:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)
    
def insert(nodo: Nodo, valor: any) -> Nodo:
    if nodo is None:
        return Nodo(valor)
    else:
        if valor < nodo.val:
            nodo.left = insert(nodo.left, valor)
        elif valor > nodo.val:
            nodo.right = insert(nodo.right, valor)

    return nodo

def search(nodo: Nodo, valor: any) -> Nodo | None:
    if nodo is None or nodo.val == valor:
        return nodo
    
    if valor < nodo.val:
        return search(nodo.left, valor)
    
    return search(nodo.right, valor)

def preorder(nodo: Nodo) -> None:
    if nodo is not None:
        print(nodo.val, end=" ")
        preorder(nodo.left)
        preorder(nodo.right)

def postorder(nodo: Nodo) -> None:
    if nodo is not None:
        postorder(nodo.left)
        postorder(nodo.right)
        print(nodo.val, end=" ")

def inorder(nodo: Nodo) -> None:
    if nodo is not None:
        inorder(nodo.left)
        print(nodo.val, end=" ")
        inorder(nodo.right)

def levelorder(nodo: Nodo) -> None:
    h = height(nodo)
    for l in range(1, h + 1):
        currentLevel(nodo, l)

def currentLevel(nodo: Nodo, level: int) -> None:
    if nodo is None:
        return None
    elif level == 1:
        print(nodo.val, end=" ")
    elif level > 1:
        currentLevel(nodo.left, level - 1)
        currentLevel(nodo.right, level - 1)

def height(root: Nodo) -> int:
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
def height_hacker_rank(root: Nodo) -> int:
    if root is None or (root.left is None and root.right is None):
        return 0
    else:
        lheight = height_hacker_rank(root.left)
        rheight = height_hacker_rank(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        