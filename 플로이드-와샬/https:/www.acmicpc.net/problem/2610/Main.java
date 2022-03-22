import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_D = 10000;
    private static int N, M;
    private static String[] input_edges;
    private static int[][] D;
    private static List<List<Integer>> GROUPS = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        input();
        init();
        sets();
        dist_calc();
        solution();
    }

    private static void solution() {
        StringBuilder sb = new StringBuilder();
        List<Integer> answer = new ArrayList(GROUPS.size());

        for(List<Integer> g : GROUPS) {
            answer.add(g.stream().min(Comparator.comparingInt(
                    n -> maxtime_of_node(n))).get());
        }
        Collections.sort(answer);
        sb.append(GROUPS.size()); sb.append('\n');
        for(int a : answer) {sb.append(a); sb.append('\n');}
        System.out.print(sb);
    }

    private static int maxtime_of_node(int i) {
        int res = 0;
        for (int j = 1; j <= N; ++j) {
            if (D[i][j] == MAX_D) continue;
            res = Math.max(res, D[i][j]);
        }
        return res;
    }

    private static void sets() {
        boolean[] traced = new boolean[N+1];
        for(int i = 1; i <= N; ++i)
            if(!traced[i]) GROUPS.add(set(i, traced));
    }

    private static List<Integer> set(int i, boolean[] traced) {
        List<Integer> list = new LinkedList<>();
        LinkedList<Integer> Q = new LinkedList<>();
        list.add(i); Q.add(i); traced[i] = true;

        while (!Q.isEmpty()) {
            int node = Q.removeFirst();

            for(int ni = 1; ni <= N; ++ni)
                if(D[node][ni] < MAX_D && !traced[ni]) {
                    Q.add(ni); traced[ni] = true; list.add(ni);
                }
        }
        return list;
    }

    private static void dist_calc() {
        for(int i = 1; i <= N; ++i) {
            for (int s = 1; s <= N; ++s) {
                for (int e = 1; e <= N; ++e) {
                    D[s][e] = Math.min(D[s][e], D[s][i] + D[i][e]);
                }
            }
        }
    }

    private static void init() {
        D = new int[N+1][N+1];
        for (int i = 1; i <= N; ++i) {
            Arrays.fill(D[i], MAX_D);
            D[i][i] = 0;
        }

        for (String edge : input_edges) {
            StringTokenizer st = new StringTokenizer(edge);
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            D[start][end] = 1; D[end][start] = 1;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); M = Integer.parseInt(br.readLine());
        input_edges = new String[M];
        for(int i = 0; i < M; ++i) { input_edges[i] = br.readLine(); }
        br.close();
    }
}
