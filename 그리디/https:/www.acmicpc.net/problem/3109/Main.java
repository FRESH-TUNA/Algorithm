import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_N = 10000;
    private static final char[][] G = new char[MAX_N][];
    private static final int DN = 3;
    private static final int[] DI = {-1,0,1}, DJ = {1,1,1};
    private static int N, M, RES;

    public static void main(String[] args) throws IOException {
        input();
        construct();
    }

    private static void construct() {
        for (int i = 0; i < N; ++i) if(dfs(i, 0)) RES += 1;
        System.out.println(RES);
    }

    private static boolean dfs(int i, int j) {
        if(j == M-1) return true;
        for (int d = 0; d < DN; ++d) {
            int ni = i+DI[d], nj = j+DJ[d];
            if (ni == -1 || ni == N) continue;
            if (G[ni][nj] == 'o' || G[ni][nj] == 'x') continue;
            G[ni][nj] = 'o';
            if (dfs(ni, nj)) return true;
        }
        return false;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer sb = new StringTokenizer(br.readLine());

        N = Integer.parseInt(sb.nextToken());
        M = Integer.parseInt(sb.nextToken());

        for (int i = 0; i < N; ++i) { G[i] = br.readLine().toCharArray(); }
    }
}
