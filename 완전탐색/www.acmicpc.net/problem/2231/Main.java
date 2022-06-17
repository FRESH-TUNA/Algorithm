import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println(solution(input()));
    }

    private static int input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        br.close();
        return N;
    }

    private static int solution(int N) {
        for(int i = 1; i <= N; ++i) if(calc(i) == N) return i;
        return 0;
    }

    private static int calc(int i) {
        int res = i, divider = 10;

        while(true) {
            int a = i / divider, b = i % divider;
            if(a == 0 && b == 0) return res;
            res += b;
            i = a;
        }
    }
}
