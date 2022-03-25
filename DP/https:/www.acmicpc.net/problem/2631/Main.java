import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int N;
    private static int[] HUMANS, DB;

    public static void main(String[] args) throws IOException {
        init();
        solution();
    }

    private static void solution() {
        int res = 0;
        DB[0] = 1;
        for (int i = 1; i < N; ++i) {
            DB[i] = 1;
            for (int j = 0; j < i; ++j)
                if (HUMANS[i] > HUMANS[j]) DB[i] = Math.max(DB[i], DB[j]+1);
            res = Math.max(res, DB[i]);
        }
        System.out.println(N-res);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        HUMANS = new int[N]; DB = new int[N];
        for (int i = 0; i < N; ++i) HUMANS[i] = Integer.parseInt(br.readLine());
        br.close();
    }
}
