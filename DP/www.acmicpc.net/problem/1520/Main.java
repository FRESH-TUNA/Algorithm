import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_N = 500, MAX_M = 500, DN = 4;
    private static final int[][] G = new int[MAX_N][MAX_M];
    private static final int[][] DB = new int[MAX_N][MAX_M];
    private static final int[] DI = {-1,0,1,0}, DJ = {0,1,0,-1};

    private static int N, M;

    public static void main(String[] args) throws IOException {
        input();
        db_init();
        System.out.println(dfs(0, 0));
    }


    private static void db_init() {
        for (int i = 0; i < N; ++i) Arrays.fill(DB[i], -1);
        DB[N-1][M-1] = 1;
    }

    private static int dfs(int i, int j) {
        int res = 0;

        for (int d = 0; d < DN; ++d) {
            int ni = i+DI[d], nj = j+DJ[d];
            //in range
            if(ni==-1 || ni==N || nj==-1 || nj==M) continue;
            //내리막길 여부
            if(G[ni][nj] >= G[i][j]) continue;
            //기록 여부
            res += (DB[ni][nj] != -1) ? DB[ni][nj] : dfs(ni, nj);
        }

        DB[i][j] = res;
        return res;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer sb = new StringTokenizer(br.readLine());

        N = Integer.parseInt(sb.nextToken());
        M = Integer.parseInt(sb.nextToken());

        for (int i = 0; i < N; ++i) {
            sb = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; ++j)
                G[i][j] = Integer.parseInt(sb.nextToken());
        }
    }
}
