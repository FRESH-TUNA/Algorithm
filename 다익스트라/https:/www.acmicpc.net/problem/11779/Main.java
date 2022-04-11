import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_D = 1000000000;
    private static int N, M, START, END;
    private static int[][] G;
    private static int[] D, ROOT;

    public static void main(String[] args) throws IOException {
        init();
        dijkstra();
        print();
    }

    private static void print() {
        Stack<Integer> cities = new Stack<>(); cities.push(END);
        StringBuilder result = new StringBuilder();

        while(cities.peek() != START) cities.push(ROOT[cities.peek()]);
        result.append(D[END] + "\n" + cities.size() + "\n");
        while(!cities.isEmpty()) result.append(cities.pop() + " ");
        System.out.println(result);
    }


    private static void dijkstra() {
        Queue<Integer> Q = new PriorityQueue<>(Comparator.comparingInt(x -> D[x]));
        Q.offer(START); D[START] = 0;

        while (!Q.isEmpty()) {
            int i = Q.poll();

            for (int ni = 1; ni <= N; ++ni)
                if (D[ni] > D[i] + G[i][ni]) {
                    D[ni] = D[i] + G[i][ni];
                    Q.offer(ni); ROOT[ni] = i;
                }
        }
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); M = Integer.parseInt(br.readLine());
        G = new int[N+1][N+1]; D = new int[N+1]; ROOT = new int[N+1];

        Arrays.fill(D, MAX_D);
        for (int i = 1; i <= N; ++i) {
            Arrays.fill(G[i], MAX_D); G[i][i] = 0; ROOT[i] = i;
        }
        input_edges(br); input_start_end(br); br.close();
    }

    private static void input_start_end(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        START = Integer.parseInt(st.nextToken());
        END = Integer.parseInt(st.nextToken());
    }

    static void input_edges(BufferedReader br) throws IOException {
        StringTokenizer st;
        for(int i = 0; i < M; ++i) {
            st = new StringTokenizer(br.readLine());
            int s=Integer.parseInt(st.nextToken());
            int e=Integer.parseInt(st.nextToken());
            int d=Integer.parseInt(st.nextToken());
            G[s][e] = Math.min(G[s][e], d);
        }
    }
}
