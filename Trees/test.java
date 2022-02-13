package Trees;
class MyBinaryTree{
    class Node{
        int data;
        Node left;
        Node right;
        public Node(int val){ data = val; left = right = null; }
    }
    class Pair{
        Node h;
        Node t;
        public Pair(){h=null;t=null;}
    }

    Node r;
    public MyBinaryTree(){ r = null; }
    public void createSampleTree()
    {
        r = new Node(5);
        r.left = new Node(3);
        r.right = new Node(10);
        r.left.left = new Node(1);
        r.left.right = new Node(4);

        r.right.left = new Node(8);
        r.right.right = new Node(20);
    }
    private void preOrder(Node root)
    {
        if(root == null){ return; }
        System.out.print(root.data +" ");
        preOrder(root.left);
        preOrder(root.right);

    }

    public void preOrder()
    {
        preOrder(r);
    }

    private boolean printallanc(Node root, int val){
        if(root == null){
            return false;
        }
        if(root.data == val){
            return true;
        }
        if( printallanc(root.left, val) || printallanc(root.right, val) ){
            System.out.println(root.data+" ");
            return true;
        }
        else
            return false;
    }
    public void printallanc(int val){
        printallanc(r, val);
    }

    private Pair treetolist(Node r){
        if(r==null){
            return null ;
        }
        Pair p=new Pair();
        if(r.left==null){
            p.h=r;
        }
        else{
            Pair l=treetolist(r.left);
            l.t.right=r;
            r.left=l.t;
            p.h=l.h;
        }
    if(r.right==null){
            p.t=r;
        }
        else{
            Pair R=treetolist(r.right);
            R.h.left=r;
            r.right=R.h;
            p.t=R.h;
        }
        return p;

    }
    public void treetolist(){
        Pair ans=treetolist(r);
        Node curr=ans.h;
        while(curr!=null){
            System.out.println(curr.data);
            curr=curr.right;
        }
    }
    private int treesum(Node r){
        if(r==null){
            return 0;
        }
        return treesum(r.left)+treesum(r.right)+r.data;
    }
    public int treesum(){
        return treesum(r);
    }
}
class test{
public static void main(String[] args) {
        MyBinaryTree tree = new MyBinaryTree();
        tree.createSampleTree();
        //tree.preOrder();
        //tree.printallanc(8);
        //tree.treetolist();
        System.out.println(tree.treesum());
    }
}