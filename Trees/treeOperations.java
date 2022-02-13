// do it insertion in binary tree , deletion  
package Trees;
class Tree{

    class Node{
        int data;
        Node left;
        Node right;

        public Node(int data){
            this.data = data;
            this.left=null;
            this.right = null;
        }
    }
    Node root;
    public Tree(){
        root = null;
    }
    void insert(int val){
        root = insert(root, val);
    }
    Node insert(Node r, int val){
        if(r == null)
            return new Node(val);
        if(val <= r.data)
            r.left = insert(r.left, val);
        else 
            r.right = insert(r.right, val);
        return r;
    }
    void preOrder(Node r){
        if(r == null){
            return;
        }
        System.out.print(r.data+" ");
        preOrder(r.left);
        preOrder(r.right);
    }
    void preOrder(){
        preOrder(root);
    }
    void inOrder(Node r){
        if(r == null){
            return;
        }
        
        inOrder(r.left);
        System.out.print(r.data+" ");
        inOrder(r.right);
    }
    void inOrder(){
        inOrder(root);
    }

    Node deleteNode(Node r,int val){
        if(r == null){
            return null;
        }
        else if(r.data > val){ 
            r.left = deleteNode(r.left, val);
        }
        else if(r.data < val){ 
            r.right = deleteNode(r.right, val);
        }
        else{
            if(r.left==null && r.right==null){
                return null;
            }
            else if(r.left==null){
                return r.right;
            }
            else if(r.right == null){
                return r.left;
            }
            else{
                int maxv = findMax(r.left);
                r.data = maxv;
                r.left = deleteNode(r.left,maxv);
            }
        }
        
        return r;
    }
    void deleteNode(int val){
        root = deleteNode(root, val);
    }
    int findMax(Node r){
        while(r.right!=null){
            r=r.right;
        }
        return r.data;
    }

    int childSum(Node r){
        if(r==null){
            return 0;
        }
        r.data = childSum(r.left) + childSum(r.right) + r.data;
        return r.data;
    }
    void childSum(){
        childSum(root);
    }
}
public class treeOperations{
    public static void main(String[] args) {
        Tree obj = new Tree();
        obj.insert(5);
        obj.insert(1);
        obj.insert(3);
        obj.insert(2);
        obj.insert(6);
        obj.insert(4);
        obj.insert(7);
        obj.preOrder();
        System.out.println();
        obj.inOrder();
        //obj.deleteNode(5);
        System.out.println();
        obj.childSum();
        obj.inOrder();
        
    }
}