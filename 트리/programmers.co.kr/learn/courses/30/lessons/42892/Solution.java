import java.util.*;

public class Solution {
    class Node {
        int x, v;
        Node left, right;
        public Node(int v, int x) {this.v = v; this.x = x;}
    }

    int[][] nodeinfo,  answer;
    int N;
    Map<int[], Integer> map;
    Node head;

    public int[][] solution(int[][] nodeinfo) {
        init(nodeinfo); node_v_add_to_map();
        sort(); make_tree(); trace();
        return answer;
    }

    private void make_tree() {
        head = new Node(map.get(nodeinfo[0]), nodeinfo[0][0]);

        for (int i = 1; i < N; ++i) {
            Node newNode = new Node(map.get(nodeinfo[i]), nodeinfo[i][0]);
            Node curr = head;

            while(true) {
                if(newNode.x > curr.x) {
                    if(curr.right == null) {
                        curr.right = newNode;
                        break;
                    } else curr = curr.right;
                }
                else {
                    if(curr.left == null) {
                        curr.left = newNode;
                        break;
                    } else curr = curr.left;
                }
            }
        }
    }

    private void trace() {
        List<Integer> pre = new ArrayList(N), post = new ArrayList<>(N);
        preorder(head, pre); postorder(head, post);
        answer[0] = pre.stream().mapToInt(i->i).toArray();
        answer[1] = post.stream().mapToInt(i->i).toArray();
    }

    private void preorder(Node node, List<Integer> pre) {
        pre.add(node.v);
        if(node.left != null) preorder(node.left, pre);
        if(node.right != null) preorder(node.right, pre);
    }

    private void postorder(Node node, List<Integer> post) {
        if(node.left != null) postorder(node.left, post);
        if(node.right != null) postorder(node.right, post);
        post.add(node.v);
    }

    private void sort() {
        Arrays.sort(nodeinfo, (a, b) -> node_compare(a, b));
    }

    private int node_compare(int[] a, int[] b) {
        if(a[1] != b[1]) return b[1] - a[1];
        else return a[0] - b[0];
    }

    private void init(int[][] nodeinfo) {
        this.nodeinfo = nodeinfo;
        N = this.nodeinfo.length;
        answer = new int[2][];
        map = new HashMap();
    }

    private void node_v_add_to_map() {
        for(int i = 0; i < N; ++i) map.put(nodeinfo[i], i+1);
    }
}
