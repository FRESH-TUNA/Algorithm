import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static long[][] SCHEDULES;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        long res = 0, prev = 0;
        for (int i = 0; i < N; ++i) {
            if(SCHEDULES[i][0] >= prev) {
                res += 1;
                prev = SCHEDULES[i][1];
            }
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        SCHEDULES = new long[N][2];
        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            SCHEDULES[i][0] = Long.parseLong(st.nextToken());
            SCHEDULES[i][1] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(SCHEDULES, (a, b) -> comparator(a, b));
        br.close();
    }

    private static int comparator(long[] a, long[] b) {
        if(a[1] == b[1]) {
            if(a[0] > b[0]) return 1;
            else if (a[0] < b[0]) return -1;
            else return 0;
        }
        if(a[1] > b[1]) return 1;
        else if (a[1] < b[1]) return -1;
        else return 0;
    }
}
