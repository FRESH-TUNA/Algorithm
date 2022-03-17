import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static int N, M;
    private static int[] CARDS;

    public static void main(String[] args) throws IOException {
        input();
        solve();
    }

    private static void solve() {
        int res = 0;
        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                if(i == j) continue;
                for(int k = 0; k < N; ++k) {
                    if(k == i || k == j) continue;
                    int candidate = CARDS[i]+CARDS[j]+CARDS[k];
                    if(candidate <= M)
                        res = Math.max(res, candidate);
                }
            }
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");

        N = Integer.parseInt(nm[0]); M = Integer.parseInt(nm[1]);

        CARDS = Arrays.stream(br.readLine().split(" "))
                .mapToInt(x -> Integer.parseInt(x)).toArray();
        br.close();
    }
}
