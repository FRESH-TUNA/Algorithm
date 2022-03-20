import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[] HUMANS;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        for (int i = 1; i < N; ++i) HUMANS[i] += HUMANS[i-1];
        for (int i = 1; i < N; ++i) HUMANS[i] += HUMANS[i-1];
        System.out.println(HUMANS[N-1]);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        HUMANS = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) HUMANS[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(HUMANS);
        br.close();
    }
}
