import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    private static final int LOTTO = 6;
    private static final boolean[] TRACED = new boolean[13];
    private static final StringBuilder RES = new StringBuilder();
    private static final Stack<Integer> SUB_RES = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer c = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(c.nextToken());
            if(n == 0) break;

            int[] nums = new int[n];
            for (int i = 0; i < n; ++i) nums[i] = Integer.parseInt(c.nextToken());
            add_cases(n, nums);
            RES.append('\n');
        }
        br.close();

        System.out.print(RES);
    }

    private static void add_cases(int n, int[] nums) {
        for (int i = 0; i <= n - LOTTO; ++i) {
            SUB_RES.push(nums[i]);
            TRACED[i] = true;
            dfs(i, nums, n);
            TRACED[i] = false;
            SUB_RES.pop();
        }
    }

    private static void dfs(int i, int[] nums, int n) {
        if(SUB_RES.size() == LOTTO) {
            add_case();
            return;
        }

        for (int ni = i+1; ni < n; ++ni) {
            if(TRACED[ni]) continue;

            SUB_RES.push(nums[ni]);
            TRACED[ni] = true;
            dfs(ni, nums, n);
            TRACED[ni] = false;
            SUB_RES.pop();
        }
    }

    private static void add_case() {
        for(Integer x : SUB_RES) {
            RES.append(x);
            RES.append(' ');
        }
        RES.deleteCharAt(RES.length()-1);
        RES.append('\n');
    }
}
