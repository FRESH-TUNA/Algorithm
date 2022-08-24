import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int DIVIDER = 1000000000;
    private static int N, K;
    private static int[][] G;

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution();
    }

    private static void solution() {
        G[0][0] = 1;
        for(int i = 1; i <= K; ++i) {
            G[i][0] = 1;
            for (int j = 1; j <= N; ++j) G[i][j] = sum(i-1, j);
        }
        System.out.println(G[K][N]);
    }

    private static int sum(int i, int j) {
        int res = 0;
        for(int n = 0; n <= j; ++n) res = (res+G[i][n]) % DIVIDER;
        return res;
    }

    private static void init() {
        G = new int[K+1][N+1];
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer MNH = new StringTokenizer(br.readLine());

        N = Integer.parseInt(MNH.nextToken());
        K = Integer.parseInt(MNH.nextToken());
        br.close();
    }
}
