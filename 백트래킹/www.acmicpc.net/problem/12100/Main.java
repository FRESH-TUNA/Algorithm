import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[][] G;
    private static int RES = 0;
    private static final short DN = 4;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        for (int d = 0; d < DN; ++d) {
            dfs(d, 0, Arrays.stream(G)
                    .map(int[]::clone).toArray(int[][]::new));
        }
        System.out.println(RES);
    }

    private static void dfs(int d, int count, int[][] G) {
        int cur = calc(G);

        if(count == 5) { RES = Math.max(RES, cur); return; }
        else if(cur * Math.pow(2, 5-count) <= RES) return;

        if (d == 0) {
            for (int j = 0; j < N; ++j) {
                int top = 0;
                for(int i = 1; i < N; ++i) {
                    if(G[i][j] == 0) continue;
                    else if (G[i][j] == G[top][j]){
                        G[top][j] *= 2; G[i][j] = 0; top += 1;
                    } else if(G[top][j] == 0) {
                        G[top][j] = G[i][j]; G[i][j] = 0;
                    } else {
                        top += 1;
                        G[top][j] = G[i][j];
                        if(top != i) G[i][j] = 0;
                    }
                }
            }
        } else if(d == 1) {
            for (int i = 0; i < N; ++i) {
                int top = N-1;
                for(int j = N-2; j >= 0; j--) {
                    if(G[i][j] == 0) continue;
                    else if (G[i][j] == G[i][top]){
                        G[i][top] *= 2; G[i][j] = 0; top -= 1;
                    } else if(G[i][top] == 0) {
                        G[i][top] = G[i][j]; G[i][j] = 0;
                    } else {
                        top -= 1;
                        G[i][top] = G[i][j];
                        if(top != j) G[i][j] = 0;
                    }
                }
            }
        } else if(d == 2) {
            for (int j = 0; j < N; ++j) {
                int top = N-1;
                for(int i = N-2; i >= 0; --i) {
                    if(G[i][j] == 0) continue;
                    else if (G[i][j] == G[top][j]){
                        G[top][j] *= 2; G[i][j] = 0; top -= 1;
                    } else if(G[top][j] == 0) {
                        G[top][j] = G[i][j]; G[i][j] = 0;
                    } else {
                        top -= 1;
                        G[top][j] = G[i][j];
                        if(top != i) G[i][j] = 0;
                    }
                }
            }
        } else {
            for (int i = 0; i < N; ++i) {
                int top = 0;
                for(int j = 1; j < N; j++) {
                    if(G[i][j] == 0) continue;
                    else if (G[i][j] == G[i][top]){
                        G[i][top] *= 2; G[i][j] = 0; top += 1;
                    } else if(G[i][top] == 0) {
                        G[i][top] = G[i][j]; G[i][j] = 0;
                    } else {
                        top += 1;
                        G[i][top] = G[i][j];
                        if(top != j) G[i][j] = 0;
                    }
                }
            }
        }

        for (int nd = 0; nd < DN; ++nd) {
            dfs(nd, count + 1, Arrays.stream(G)
                    .map(int[]::clone).toArray(int[][]::new));
        }
    }

    private static int calc(int[][] G) {
        int res = 0;
        for (int[] row : G) { for (int x : row) res = Math.max(res, x); }
        return res;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        G = new int[N][N];
        for(int i = 0; i < N; ++i) {
            StringTokenizer row = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; ++j) G[i][j] = Integer.parseInt(row.nextToken());
        }
        br.close();
    }
}
