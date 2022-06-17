import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_RES = 3;
    private static int N, M, H;
    private static boolean[][] G;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static boolean check() {
        for(int j = 1; j <= N; ++j) {
            int cur = j;
            for(int i = 1; i <= H; ++i) {
                if (G[i][cur]) cur += 1;
                else if (cur > 1 && G[i][cur - 1]) cur -= 1;
            }
            if(cur != j) return false;
        }
        return true;
    }

    private static void solution() {
        for(int res = 0; res <= MAX_RES; res += 1)
            if(dfs(1, 1, 0, res)) {
                System.out.println(res);
                return;
            }
        System.out.println(-1);
    }

    private static boolean dfs(int i, int j, int c, int max_c) {
        if(check()) return true;
        if(c == max_c) return false;

        for (int ni = i; ni <= H; ++ni) {
            for (int nj = i==ni ? j : 1; nj < N; ++nj) {
                if(G[ni][nj]) nj += 1;
                else {
                    G[ni][nj] = true;
                    if(dfs(ni, nj+2, c+1, max_c)) return true;
                    G[ni][nj] = false;
                }
            }
        }
        return false;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        H=Integer.parseInt(st.nextToken());

        G = new boolean[H+1][N+1];
        for (int i = 0; i < M; ++i) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            G[a][b] = true;
        }
        br.close();
    }
}
