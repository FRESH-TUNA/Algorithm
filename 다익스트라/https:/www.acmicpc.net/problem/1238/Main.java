import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Dijkstra {
    private static int N, M;
    private static Set<Integer>[] E, ER;
    private static int[] D, DR;
    private static int[][] G, GR;
    private static int START;

    public static void main(String[] args) throws IOException {
        input();
        D_init();
        calc(E, D, G); calc(ER, DR, GR);
        result();
    }

    private static void calc(Set<Integer>[] E, int[] D, int[][] G) {
        D[START] = 0;
        PriorityQueue<Integer> Q = new PriorityQueue<>(
                Comparator.comparingInt(i -> D[i]));
        Q.add(START);

        while (!Q.isEmpty()) {
            int i = Q.poll();

            for(int ni : E[i]) {
                if(D[ni] > D[i] + G[i][ni]) {
                    D[ni] = D[i] + G[i][ni];
                    Q.add(ni);
                }
            }
        }
    }

    private static void result() {
        System.out.println(IntStream.range(1, N+1)
                .map(i -> D[i]+DR[i]).max().getAsInt());
    }

    private static void D_init() {
        D = new int[N+1]; DR = new int[N+1];
        Arrays.fill(D, Integer.MAX_VALUE);
        Arrays.fill(DR, Integer.MAX_VALUE);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer NMS = new StringTokenizer(br.readLine());

        N = Integer.parseInt(NMS.nextToken());
        M = Integer.parseInt(NMS.nextToken());
        START = Integer.parseInt(NMS.nextToken());

        G = new int[N+1][N+1]; GR = new int[N+1][N+1];
        E = new Set[N+1]; ER = new Set[N+1];

        for(int i = 1; i <= N; ++i) {
            E[i] = new HashSet();
            ER[i] = new HashSet();
        }
        input_edges(br);
        br.close();
    }

    private static void input_edges(BufferedReader br) throws IOException {
        for (int i = 0; i < M; ++i) {
            StringTokenizer SED = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(SED.nextToken());
            int end = Integer.parseInt(SED.nextToken());
            int d = Integer.parseInt(SED.nextToken());

            G[start][end] = d; GR[end][start] = d;
            E[start].add(end); ER[end].add(start);
        }
    }
}
