import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int NUM_N = 10, MAX_N = 100;
    private static final int DIVIDER = 1_000_000_000;
    private static int N;
    private static long[][][] DB;

    public static void main(String[] args) throws IOException {
        init();
        solution();
    }

    private static void solution() {
        long res = 0;
        for (int i = 2; i <= N; ++i) {
            for (int j = 0; j < NUM_N; ++j) {
                for(int k = 0; k < 1024; k++) {
                    int bit = k | (1 << j);
                    if(j == 0)
                        DB[i][j][bit] = (DB[i][j][bit]+DB[i-1][j+1][k]) % DIVIDER;
                    else if(j == 9)
                        DB[i][j][bit] = (DB[i][j][bit]+DB[i-1][j-1][k]) % DIVIDER;
                    else
                        DB[i][j][bit] = (DB[i][j][bit]+DB[i-1][j+1][k]+DB[i-1][j-1][k]
                            ) % DIVIDER;
                }
            }
        }

        for (int j = 0; j < NUM_N; ++j) res = (res+DB[N][j][1023]) % DIVIDER;
        System.out.println(res);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        DB = new long[MAX_N+1][NUM_N][1<<NUM_N];
        for (int i = 1; i < NUM_N; ++i) DB[1][i][1<<i] = 1;
        br.close();
    }
}
