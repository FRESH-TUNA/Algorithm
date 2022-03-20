import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N, TARGET;
    private static int[] COINS;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        int res = 0;
        for (int i = N-1; i >= 0; i--) {
            if(TARGET >= COINS[i]) {
                res += TARGET / COINS[i];
                TARGET = TARGET % COINS[i];
            }
            if(TARGET == 0) break;
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        TARGET = Integer.parseInt(st.nextToken());

        COINS = new int[N];
        for (int i = 0; i < N; ++i) {
            COINS[i] = Integer.parseInt(br.readLine());
        }
        br.close();
    }
}
