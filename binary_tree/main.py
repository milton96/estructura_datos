from nodo import insert, search, preorder, postorder, inorder, height, height_hacker_rank, levelorder

if __name__== '__main__':
    #          50 
    #       /     \ 
    #     30      70 
    #    /  \    /  \ 
    #  20   40  60   80
    #               /  \
    #              79  81
    root = None

    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 81)
    insert(root, 79)

    v = 41
    encontrado = search(root, v)
    msj = "encontrado" if encontrado is not None else "no encontrado"
    print(v, msj)

    print("pre-order")
    preorder(root)

    print("\npost-order")
    postorder(root)

    print("\nin-order")
    inorder(root)

    print("\n\nheight")
    print(height(root))

    print("\nheight hacker rank")
    print(height_hacker_rank(root))

    print("\nlevel order")
    levelorder(root)