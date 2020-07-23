import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.left = None
        self.right = None 
        
def search(ptr,key):
    if(ptr is None):
        print("Key not found")
    elif(ptr<root.info):
        return search(ptr.left,key)
    elif(key>ptr.info):
        return search(ptr.right,key)
    else:
        return ptr
    
def insert(ptr,key):
    if(ptr is None):
        ptr=node(value)
    elif(key<=ptr.info):
        ptr.left=insert(ptr.left,key)
    elif(key>ptr.info):
        ptr.right=insert(ptr.right,key)
    return ptr

def delete(ptr,key):
    if(ptr is None):
        print("Key not found")
        return
    if(key<ptr.info):
        ptr.left=delete(ptr.left,key)
    elif(key>ptr.info):
        ptr.right=delete(ptr.right,key)
    else:
        if ptr.left is not None and ptr.right is not None:
            succ=ptr.right
            while succ.left:
                succ=succ.left
            ptr.info=succ.info
            ptr.right = delete(ptr.right, succ.info)
        else:
            if(ptr.right is not None):
                ptr=ptr.right
            elif(ptr.left is not None):
                ptr=ptr.left
            else:
                ptr=None
    return ptr

def preorder(ptr):
    if(ptr==None):
        return
    print(ptr.info)
    preorder(ptr.left)
    preorder(ptr.right)
        
def inorder(ptr):
    if(ptr==None):
        return
    inorder(ptr.left)
    print(ptr.info)
    inorder(ptr.right)
    
def postorder(ptr):
    if(ptr==None):
        return
    postorder(ptr.left)
    postorder(ptr.right)
    print(ptr.info)

def height(ptr):
    if ptr is None:
        return 0;
    
    lheight=height(ptr.left)
    rheight=height(ptr.right)
    if lheight>rheight:
        return 1+lheight
    else:
        return 1+rheight
def Min(ptr):
    if ptr is None:
        return None
    elif ptr.left is None:
        return ptr
    else:
        return Min(ptr.left)
    
def Max(ptr):
    if ptr is None:
        return None
    elif ptr.right is None:
        return ptr
    else:
        return Max(ptr.right)
    
    
if __name__=='__main__':
    root=None
    while(1):
        print("1.Search\n");
        print("2.Insert\n");
        print("3.Delete\n");
        print("4.Preorder Travaersal\n");
        print("5.Inorder Traversal\n");
        print("6.Postorder Traversal\n");
        print("7.Height of tree\n");
        print("8.Find minimum and maximum\n");
        print("9.Quit\n\n");
        print("Enter your choice : ");
        choice=int(input())
        if(choice==1):
            print("Enter key to be searhced")
            value=int(input())
            ptr=search(root,value)
            if ptr is not None:
                print("key found")
        elif(choice==2):
            print("Enter key to be inserted")
            value=int(input())
            root=insert(root,value)
        elif(choice==3):
            print("Enter key to be deleted")
            value=int(input())
            root=delete(root,value)
        elif(choice==4):
            preorder(root)
        elif(choice==5):
            inorder(root)
        elif(choice==6):
            postorder(root)
        elif(choice==7):
            h=height(root)
            print("height=",h)
        elif(choice==8):
            ptr=Min(root)
            print("min value is",ptr.info)
            ptr=Max(root)
            print("max value is",ptr.info)
        elif(choice==9):
            sys.exit(0)
        else:
            sys.exit(0)
        
        


