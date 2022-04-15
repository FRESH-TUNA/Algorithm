import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    int N;
    int[] NUMS;

    public static void main(String[] args) throws IOException {
        new Main().call();
    }

    void call() throws IOException {
        init();
        solution();
    }

    void solution() {
        int left = 0, right = N-1;
        int ans_left = 0, ans_right = N-1;
        int min = Math.abs(NUMS[left] + NUMS[right]);

        while(left < right) {
            int sum = NUMS[left] + NUMS[right];

            if (min > Math.abs(sum)) {
                min = Math.abs(sum);
                ans_left = left;
                ans_right = right;
            }

            if (sum == 0) break;
            else if (sum > 0) right -= 1;
            else left += 1;
        }
        System.out.println(NUMS[ans_left] + " " + NUMS[ans_right]);
    }

    void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        NUMS = new int[N]; st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) NUMS[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(NUMS);
        br.close();
    }
}
