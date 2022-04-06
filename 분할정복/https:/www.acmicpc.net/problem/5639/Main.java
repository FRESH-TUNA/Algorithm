import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B5639 {
    private static final int MAX_N = 10000;
    private static final int[] pre = new int[MAX_N], post = new int[MAX_N];
    private static int N = 0;

    public static void main(String[] args) throws IOException {
        input();
        postorder(0, N-1, 0, N-1);
        print();
    }

    private static void print() {
        for (int i = 0; i < N; ++i) System.out.println(post[i]);
    }

    private static void postorder(int pre_s, int pre_e, int post_s, int post_e) {
        if(pre_s > pre_e || post_s > post_e) return;

        post[post_e] = pre[pre_s];
        int idx = pre_s;
        while(idx <= pre_e) {
            if(pre[idx] > pre[pre_s]) break;
            idx += 1;
        }
        postorder(pre_s+1, idx-1, post_s, post_s+(idx-pre_s-2));
        postorder(idx, pre_e, post_s+(idx-pre_s-1), post_e-1);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";

        while ((input = br.readLine()) != null) {
            pre[N++] = Integer.parseInt(input);
        }
        br.close();
    }
}
