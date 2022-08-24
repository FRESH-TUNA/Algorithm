import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int BORDER = 48;
    private static final int[][] DI = {{0, 1}, {0, 1, 2}, {1, 2}};

    private static int N, M = 3;
    private static char[][] G;
    private static final int[] MAX = new int[3], MIN = new int[3];

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        int[] MAX_TEMP = new int[M], MIN_TEMP = new int[M];
        for (int i = 0; i < M; ++i)
            MIN[i] = MAX[i] = G[0][i]-BORDER;

        for(int i = 1; i < N; ++i) {
            for (int k = 0; k < M; ++k) {
                MAX_TEMP[k] = Arrays.stream(DI[k]).map(x -> MAX[x]).max().getAsInt();
                MIN_TEMP[k] = Arrays.stream(DI[k]).map(x -> MIN[x]).min().getAsInt();
            }
            for (int k = 0; k < M; ++k) {
                MAX[k] = MAX_TEMP[k] + (G[i][k]-BORDER);
                MIN[k] = MIN_TEMP[k] + (G[i][k]-BORDER);
            }
        }
        System.out.println(Arrays.stream(MAX).max().getAsInt() +
                " " + Arrays.stream(MIN).min().getAsInt());
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        G = new char[N][M];
        for (int i = 0; i < N; ++i) {
            StringTokenizer row = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; ++j)
                G[i][j] = row.nextToken().charAt(0);
        }
        br.close();
    }
}
