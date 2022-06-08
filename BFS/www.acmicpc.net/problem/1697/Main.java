import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int START, TARGET;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        Queue<Integer> Q = new LinkedList<>();
        boolean[] traced = new boolean[100001];
        int[] d = new int[100001];
        traced[START] = true; d[START] = 0; Q.add(START);

        while (!Q.isEmpty()) {
            int node = Q.poll();
            if(node == TARGET) break;

            for(int new_node : new int[] {node-1, node+1, node*2}) {
                if(new_node < 0 || new_node > 100000) continue;
                if(traced[new_node]) continue;

                traced[new_node] = true; d[new_node] = d[node]+1;
                Q.offer(new_node);
            }
        }
        System.out.println(d[TARGET]);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        START = Integer.parseInt(st.nextToken());
        TARGET = Integer.parseInt(st.nextToken());
    }
}
