import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_NM = 20;
    private static final char[][] G = new char[MAX_NM][];
    private static final boolean[][] TRACED = new boolean[MAX_NM][MAX_NM];
    private static final boolean[] A_TRACED = new boolean[100];
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
        for (int i = 0; i < N; ++i) G[i] = br.readLine().toCharArray();
        br.close();
    }

    private static void solution() {
        A_TRACED[G[0][0]] = true; TRACED[0][0] = true;
        dfs(0, 0, 1);
        System.out.println(RES);
    }

    private static void dfs(int i, int j, int c) {
        RES = Math.max(RES, c);

        for (int d = 0; d < DN; ++d) {
            int ni = i+DI[d], nj = j+DJ[d];

            if(ni == -1 || ni == N || nj == -1 || nj == M)
                continue;
            if(A_TRACED[G[ni][nj]] || TRACED[ni][nj])
                continue;

            //dfs
            A_TRACED[G[ni][nj]] = true; TRACED[ni][nj] = true;
            dfs(ni, nj, c+1);
            A_TRACED[G[ni][nj]] = false; TRACED[ni][nj] = false;
        }
    }
}
