import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_NM = 20;
    private static final int[][] G = new int[MAX_NM][MAX_NM];
    private static final int[][] TRACED = new int[MAX_NM][MAX_NM];

    private static final int DN = 4;
    private static final int[] DI = {-1,0,1,0}, DJ = {0,1,0,-1};
    private static int N, M;
    private static int RES = 1;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer NM = new StringTokenizer(br.readLine());
        N = Integer.parseInt(NM.nextToken());
        M = Integer.parseInt(NM.nextToken());

        for (int i = 0; i < N; ++i) {
            char[] row = br.readLine().toCharArray();
            for (int j = 0; j < M; ++j) G[i][j] = row[j] - 'A';
        }
        br.close();
    }

    private static void solution() {
        dfs(0, 0, 1, 1 << G[0][0]);
        System.out.println(RES);
    }

    private static void dfs(int i, int j, int c, int bit) {
        if(TRACED[i][j] == bit) return;

        TRACED[i][j] = bit;
        RES = Math.max(RES, c);

        for (int d = 0; d < DN; ++d) {
            int ni = i+DI[d], nj = j+DJ[d];

            if(ni == -1 || ni == N || nj == -1 || nj == M)
                continue;
            if((bit & (1 << G[ni][nj])) != 0)
                continue;
            //dfs
            dfs(ni, nj, c+1, (bit | (1 << G[ni][nj])));
        }
    }
}
