import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int DN = 4;
    private static final int[] DI = {-1, 0, 1, 0}, DJ = {0, 1, 0, -1};
    private static int T;
    private static int[] N, M;
    private static int[][][] G;

    public static void main(String[] args) throws IOException {
        inputs();
        solutions();
    }

    private static void solutions() {
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; ++t) { sb.append(solution(t)); sb.append('\n'); }
        System.out.print(sb);
    }

    private static int solution(int t) {
        int res = 0;
        boolean[][] traced = new boolean[N[t]][M[t]];

        for(int i = 0; i < N[t]; ++i)
            for (int j = 0; j < M[t]; ++j)
                if(!traced[i][j] && G[t][i][j] == 1)
                    res += bfs(i, j, t, traced);
        return res;
    }

    private static int bfs(int i, int j, int t, boolean[][] traced) {
        LinkedList<Integer> IQ = new LinkedList<>(), JQ = new LinkedList<>();
        IQ.add(i); JQ.add(j);
        traced[i][j] = true;

        while (IQ.size() > 0) {
            int ci = IQ.removeFirst(), cj = JQ.removeFirst();

            for (int d = 0; d < DN; ++d) {
                int ni = ci+DI[d], nj = cj+DJ[d];
                if(ni == -1 || ni == N[t] || nj == -1 || nj == M[t])
                    continue;
                if(traced[ni][nj] || G[t][ni][nj] == 0)
                    continue;
                traced[ni][nj] = true;
                IQ.add(ni); JQ.add(nj);
            }
        }
        return 1;
    }

    private static void inputs() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        G = new int[T][][];
        N = new int[T]; M = new int[T];

        for (int t = 0; t < T; ++t) input(br, t);

        br.close();
    }

    private static void input(BufferedReader br, int t) throws IOException {
        StringTokenizer NMK = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(NMK.nextToken());
        int m = Integer.parseInt(NMK.nextToken());
        int k = Integer.parseInt(NMK.nextToken());

        N[t] = n; M[t] = m;
        G[t] = new int[n][m];

        while(k > 0) {
            StringTokenizer ij = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(ij.nextToken());
            int j = Integer.parseInt(ij.nextToken());
            G[t][i][j] = 1;
            k--;
        }
    }
}
