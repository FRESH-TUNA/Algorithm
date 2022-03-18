import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M;
    private static long[] TREES;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        long min = 0, max = Arrays.stream(TREES).max().getAsLong()-1, res = min;
        while (min <= max) {
            long mid = min + (max-min) / 2;
            long cres = Arrays.stream(TREES)
                    .map(t -> (t > mid ? t-mid : 0)).sum();

            if(cres >= M) {
                res = Math.max(res, mid);
                min = mid + 1;
            }
            else max = mid - 1;
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        TREES = new long[N];
        for (int i = 0; i < N; ++i)
            TREES[i] = Long.parseLong(st.nextToken());
        br.close();
    }
}
