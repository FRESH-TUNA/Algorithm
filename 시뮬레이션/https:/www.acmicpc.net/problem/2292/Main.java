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
        int res = 1, count = 1, mpy = 6;
        while(count < N) {
            res += 1;
            count += mpy;
            mpy += 6;
        }
        return res;
    }
}
