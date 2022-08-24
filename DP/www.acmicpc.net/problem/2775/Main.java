import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int N = 15;
    private static final int[][] db = new int[N][N];

    public static void main(String[] args) throws IOException {
        solve();
        input_and_solve();
    }

    private static void solve() {
        for(int i = 0; i < N; ++i) db[0][i] = i;
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < N; j++) db[i][j] = db[i-1][j] + db[i][j-1];
        }
    }

    private static void input_and_solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        while (n > 0) {
            int r = Integer.parseInt(br.readLine());
            int c = Integer.parseInt(br.readLine());
            sb.append(db[r][c]);
            sb.append('\n');
            n--;
        }
        br.close();
        System.out.print(sb);
    }
}
