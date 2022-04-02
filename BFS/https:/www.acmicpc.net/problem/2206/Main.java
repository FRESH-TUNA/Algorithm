import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class DFS {
    private static final int MAX_D = 10000000;
    private static final char WALL = '1';
    private static final int DN = 4;
    private static final int[] DI = {-1, 0, 1, 0}, DJ = {0, 1, 0, -1};

    private static int N, M;
    private static char[][] G;
    private static int[][][] D;

    public static void main(String[] args) throws IOException {
        init();
        solution();
    }

    private static void solution() {
        bfs(0, 0);
        int res = Math.min(D[N-1][M-1][0], D[N-1][M-1][1]);
        System.out.println(res == MAX_D ? -1 : res);
    }

    private static void bfs(int i, int j) {
        Queue<Integer> IQ = new LinkedList<>(), JQ = new LinkedList<>();
        Queue<Integer> BQ = new LinkedList<>();
        IQ.add(i); JQ.add(j); BQ.add(0);

        D[i][j][0] = 1; D[i][j][1] = 1;
        while (!IQ.isEmpty()) {
            i = IQ.poll(); j = JQ.poll(); int b = BQ.poll();
            for (int d = 0; d < DN; ++d) {
                int ni = DI[d]+i, nj = DJ[d]+j;

                if(ni == -1 || ni == N || nj == -1 || nj == M)
                    continue;
                if(G[ni][nj] == WALL && b == 1) continue;
                if(D[ni][nj][b] != MAX_D) continue;
                int nb = G[ni][nj] == WALL || b == 1 ? 1 : 0;
                D[ni][nj][nb] = D[i][j][b]+1;
                IQ.add(ni); JQ.add(nj); BQ.add(nb);
            }
        }
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nm = new StringTokenizer(br.readLine());
        N=Integer.parseInt(nm.nextToken()); M=Integer.parseInt(nm.nextToken());

        G = new char[N][]; D = new int[N][M][2];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                D[i][j][0] = D[i][j][1] = MAX_D;
            }
            G[i] = br.readLine().toCharArray();
        }
        br.close();
    }
}
