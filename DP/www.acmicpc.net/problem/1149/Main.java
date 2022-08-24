import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int R = 0, B = 1, G = 2, CN = 3;

    private static int[][] COSTS, DB;
    private static int N;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        DB[0][R] = COSTS[0][R]; DB[0][G] = COSTS[0][G]; DB[0][B] = COSTS[0][B];
        for (int i = 1; i < N; ++i) {
            DB[i][R] = Math.min(DB[i-1][G], DB[i-1][B]) + COSTS[i][R];
            DB[i][G] = Math.min(DB[i-1][R], DB[i-1][B]) + COSTS[i][G];
            DB[i][B] = Math.min(DB[i-1][R], DB[i-1][G]) + COSTS[i][B];
        }
        System.out.println(Arrays.stream(DB[N-1]).min().getAsInt());
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        COSTS = new int[N][CN]; DB = new int[N][CN];
        
        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < CN; ++j)
                COSTS[i][j] = Integer.parseInt(st.nextToken());
        }
        br.close();
    }
}
