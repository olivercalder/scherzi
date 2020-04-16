public class Node {
    public Node next;
    public String data;
    public Node(String name, Node nextNode) {
        this.data = name;
        this.next = nextNode;
    }
}
