import java.util.*;
import java.util.stream.IntStream;

class Solution {
    private final static int MAX_NODES = 20000;
    private final static int START_NODE = 1;
    private static HashSet<Integer> traced = new HashSet<>();
    private static int[] distances = new int[MAX_NODES + 1];
    private static LinkedList<Integer>[] graph = new LinkedList[MAX_NODES + 1];
    private static PriorityQueue<int[]> queue = new PriorityQueue<>(
        new Comparator<int[]>() {
            public int compare(int[] x, int[] y) { return x[1] - y[1]; }});

    public int solution(int n, int[][] edge) {
        init_distances(n);
        init_graphs(edge, n);
        calculate_distances();
        return answer(n);
    }

    private void init_graphs(int[][] edges, int n) {
        for(int i = 1; i <= n; ++i) graph[i] = new LinkedList<>();
        for(int[] edge : edges) {
            int x = edge[0], y = edge[1];
            graph[x].add(y); graph[y].add(x);
        }
    }

    private void calculate_distances() {
        queue.add(new int[] {1, 0});

        while(!queue.isEmpty()) {
            int node = queue.poll()[0];

            if(traced.contains(node)) continue;
            traced.add(node);

            Iterator<Integer> it = graph[node].iterator();
            while(it.hasNext()) {
                int connected = it.next();
                if(distances[connected] > distances[node] + 1)
                    distances[connected] = distances[node] + 1;
                queue.add(new int[] {connected, distances[connected]});
            }
        }
    }

    private void init_distances(int n) {
        for(int i = 1; i <= n; ++i) distances[i] = Integer.MAX_VALUE;
        distances[START_NODE] = 0;
    }

    private int answer(int n) {
        int max = IntStream.range(1, n+1).map(x -> distances[x]).max().getAsInt();
        return (int) IntStream.range(1, n+1).filter(x -> distances[x] == max).count();
    }
}
