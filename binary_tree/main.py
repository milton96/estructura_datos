from nodo import agregar, buscar, preorder, postorder, inorder, height, height_vertices, levelorder

if __name__== '__main__':
    #          50 
    #       /     \ 
    #     30      70 
    #    /  \    /  \ 
    #  20   40  60   80
    #               /  \
    #              79  81
    root = None

    root = agregar(root, 50)
    agregar(root, 30)
    agregar(root, 20)
    agregar(root, 40)
    agregar(root, 70)
    agregar(root, 60)
    agregar(root, 80)
    agregar(root, 81)
    agregar(root, 79)

    v = 41
    encontrado = buscar(root, v)
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
    print(height_vertices(root))

    print("\nlevel order")
    levelorder(root)