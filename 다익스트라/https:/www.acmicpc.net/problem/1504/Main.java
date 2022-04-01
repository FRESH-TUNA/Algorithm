import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_D = 10000000;

    private static int N, E, A, B;
    private static String[] EDGE_DATA;
    private static int[][] G;
    private static Set<Integer>[] EDGE;

    public static void main(String[] args) throws IOException {
        input(); init(); solution();
    }

    private static void solution() {
        int[] one_start_d = distance(1), a_start_d = distance(A);
        int[] n_start_d = distance(N);

        int result = Math.min( one_start_d[A]+a_start_d[B]+n_start_d[B],
                               one_start_d[B]+a_start_d[B]+n_start_d[A] );
        System.out.println(result >= MAX_D ? -1 : result);
    }

    private static int[] distance(int start) {
        int[] nd = new int[N+1];
        Arrays.fill(nd, MAX_D); nd[start] = 0;
        Queue<Integer> Q = new PriorityQueue<>(Comparator.comparing(x -> nd[x]));
        Q.offer(start);

        while (!Q.isEmpty()) {
            start = Q.poll();

            for(int end : EDGE[start]) {
                if(nd[end] > nd[start]+G[start][end]) {
                    nd[end] = nd[start]+G[start][end];
                    Q.offer(end);
                }
            }
        }
        return nd;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer NE = new StringTokenizer(br.readLine());

        N=Integer.parseInt(NE.nextToken()); E=Integer.parseInt(NE.nextToken());
        EDGE_DATA = new String[E];
        for (int i = 0; i < E; ++i) EDGE_DATA[i] = br.readLine();

        StringTokenizer AB = new StringTokenizer(br.readLine());
        A=Integer.parseInt(AB.nextToken()); B=Integer.parseInt(AB.nextToken());
        br.close();
    }

    private static void init() {
        G = new int[N+1][N+1]; EDGE = new Set[N+1];
        for (int i = 1; i <= N; ++i) {
            Arrays.fill(G[i], MAX_D); G[i][i] = 0;
            EDGE[i] = new HashSet<>();
        }

        int s, e, d; StringTokenizer sed;
        for(String edge : EDGE_DATA) {
            sed = new StringTokenizer(edge);
            s = Integer.parseInt(sed.nextToken()); e = Integer.parseInt(sed.nextToken());
            d = Integer.parseInt(sed.nextToken()); EDGE[s].add(e); EDGE[e].add(s);
            G[s][e] = d; G[e][s] = d;
        }
    }
}
