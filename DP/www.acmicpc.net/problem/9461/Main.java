import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int N = 100;
    private static final long[] DB = new long[N+1];

    public static void main(String[] args) throws IOException {
        init();
        solution();
    }

    private static void init() {
        DB[1] = 1; DB[2] = 1; DB[3] = 1;
        for (int i = 4; i <= N; ++i) DB[i] = DB[i-2]+DB[i-3];
    }

    private static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            ans.append(DB[Integer.parseInt(br.readLine())]);
            ans.append('\n');
        }
        System.out.print(ans);
    }
}
