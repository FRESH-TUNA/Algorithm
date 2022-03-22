import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main2 {
    private static final int MAX_D = 10000;
    private static int N, M;
    private static String[] E_RAW_DATA;
    private static int[][] D;

    public static void main(String[] args) throws IOException {
        input();
        init();
        distance();
        solution();
    }

    private static void distance() {
        for (int n = 1; n <= N; ++n) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j)
                    D[i][j] = Math.min(D[i][j], D[i][n]+D[n][j]);
            }
        }
    }

    private static void solution() {
        int res = 0, prev = MAX_D*2;
        for (int n = 1; n <= N; ++n) {
            int candidate = Arrays.stream(D[n]).sum();
            if (candidate < prev) {
                prev = candidate;
                res = n;
            }
        }
        System.out.println(res);
    }

    private static void init() {
        D = new int[N+1][N+1];
        for (int i = 1; i <= N; ++i) {
            Arrays.fill(D[i], MAX_D);
            D[i][i] = 0;
        }

        for (int i = 0; i < M; ++i) {
            StringTokenizer st = new StringTokenizer(E_RAW_DATA[i]);
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            D[s][e] = 1; D[e][s] = 1;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer NRC = new StringTokenizer(br.readLine());

        N = Integer.parseInt(NRC.nextToken()); M = Integer.parseInt(NRC.nextToken());
        E_RAW_DATA = new String[M];

        for (int i = 0; i < M; ++i) E_RAW_DATA[i] = br.readLine();
    }
}
