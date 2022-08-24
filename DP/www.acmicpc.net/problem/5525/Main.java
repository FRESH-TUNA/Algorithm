import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int N, M;
    private static char[] S;

    public static void main(String[] args) throws IOException {
        input();
        int res = 0;
        int[] memo = new int[M];
        for (int i = 1; i < M-1; ++i) {
            if(S[i] == 'O' && S[i+1] == 'I') {
                memo[i+1] = memo[i-1] + 1;
                if(memo[i+1] >= N && S[i - 2*N + 1] == 'I')
                    res += 1;
            }
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine()); M=Integer.parseInt(br.readLine());
        S = br.readLine().toCharArray();
        br.close();
    }
}
