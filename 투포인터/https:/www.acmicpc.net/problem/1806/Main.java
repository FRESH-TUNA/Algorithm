import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    int N, S;
    int[] NUMS;

    public static void main(String[] args) throws IOException {
        new Main().call();
    }

    void call() throws IOException {
        init();
        solution();
    }

    void solution() {
        int left = 0, right = 1;
        int sum = NUMS[left], res = 1000000;

        if(sum >= S) { System.out.println(1); return; }
        while (right != N || left != N) {
            if(sum >= S) {
                res = Math.min(res, right-left);
                sum -= NUMS[left++];
            } else if (right == N) break;
            else sum += NUMS[right++];
        }
        if (sum >= S) res = Math.min(res, right-left);
        System.out.println(res == 1000000 ? 0 : res);
    }

    void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken()); S=Integer.parseInt(st.nextToken());
        NUMS = new int[N]; st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) NUMS[i] = Integer.parseInt(st.nextToken());
        br.close();
    }
}
