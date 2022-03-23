import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_CHANNEL = 1000000, CUR_CHANNEL = 100;
    private static final int N = 10;
    private static final boolean[] REMOTE = new boolean[10];
    private static final int[] DB = new int[MAX_CHANNEL];

    private static int TARGET, M;
    private static StringTokenizer BROKEN_DATA;

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution();
    }

    private static void solution() {
        if(REMOTE[0]) DB[0] = 1;
        for (int i = 1; i < MAX_CHANNEL; ++i) {
            if(DB[i-1] != MAX_CHANNEL) DB[i] = Math.min(DB[i], DB[i-1]+1);
            int result = go_without_adjust(i);
            if(result != -1) DB[i] = Math.min(result, DB[i]);
        }
        for (int i = MAX_CHANNEL-2; i >= 0; i--) DB[i] = Math.min(DB[i], DB[i+1]+1);
        System.out.println(DB[TARGET]);
    }

    private static int go_without_adjust(int i) {
        int res = 0;
        while (i > 0) {
            if (!REMOTE[i % 10]) return -1;
            i = i / 10; res += 1;
        }
        return res;
    }

    private static void init() {
        Arrays.fill(REMOTE, true);
        if(M > 0)
            while (BROKEN_DATA.hasMoreTokens())
                REMOTE[Integer.parseInt(BROKEN_DATA.nextToken())] = false;
        Arrays.fill(DB, MAX_CHANNEL);
        DB[CUR_CHANNEL] = 0;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TARGET = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        if(M == 0) return;
        BROKEN_DATA = new StringTokenizer(br.readLine());
    }
}
