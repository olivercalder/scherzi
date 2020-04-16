public class Reverse {
    public static Node reverse(Node head) {
        if (head.next == null) {
            return head;
        } else {
            Node futureTail = head.next;
            Node newHead = reverse(futureTail);
            futureTail.next = head;
            head.next = null;
            return newHead;
        }
    }
    public static void print(Node head) {
        System.out.println(head.data);
        Node currentNode = head;
        while (currentNode.next != null) {
            currentNode = currentNode.next;
            System.out.println(currentNode.data);
        }
    }
    public static void main(String[] args) {
        Node F = new Node("F", null);
        Node E = new Node("E", F);
        Node D = new Node("D", E);
        Node C = new Node("C", D);
        Node B = new Node("B", C);
        Node A = new Node("A", B);

        System.out.println("Original:");
        print(A);

        System.out.println("\nReversed:");
        Node reversed = reverse(A);
        print(reversed);
    }
}
