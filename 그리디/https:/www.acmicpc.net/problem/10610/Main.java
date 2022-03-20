import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static char[] N;
    private static int[] IN;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        if(IN[0] == 0 && Arrays.stream(IN).sum() % 3 == 0) {
            StringBuilder sb = new StringBuilder(new String(N));
            System.out.println(sb.reverse());
        }
        else System.out.println(-1);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = br.readLine().toCharArray();
        Arrays.sort(N);

        IN = new int[N.length];
        for (int i = 0; i < N.length; ++i)
            IN[i] = Character.getNumericValue(N[i]);
        br.close();
    }
}
