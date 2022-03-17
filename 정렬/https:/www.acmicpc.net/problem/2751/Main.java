import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int N;
    private static final int MAX_N = 2000001;
    private static final int MOD = 1000000;
    private static final int[] DB = new int[MAX_N];

    public static void main(String[] args) throws IOException {
        input();
        print();
    }

    private static void print() {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (int i = 0; i < MAX_N; ++i) {
            if(count == N) break;
            if(DB[i] == 0) continue;
            count += 1;
            sb.append(i-MOD);
            sb.append('\n');
        }
        System.out.println(sb);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; ++i)
            DB[Integer.parseInt(br.readLine()) + MOD] += 1;
        br.close();
    }
}
