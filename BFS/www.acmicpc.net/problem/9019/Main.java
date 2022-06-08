import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B9019 {
    private static final short MAX_NUM = 10000, DN = 4;
    private static final char[] COMMAND = {'D', 'S', 'L', 'R'};

    private static boolean[][] TRACED;
    private static String[] RES;
    private static short N;
    private static short[] CUR, TARGET;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        for (int i = 0; i < N; ++i) {
            bfs(i);
            System.out.println(RES[i]);
        }
    }

    private static void bfs(int i) {
        Queue<Short> Q = new LinkedList();
        Queue<StringBuilder> sbQ = new LinkedList();
        Q.offer(CUR[i]); sbQ.offer(new StringBuilder());
        int size = 1; TRACED[i][CUR[i]] = true;

        while (size > 0) {
            int new_size = 0;

            while (size-- > 0) {
                short cur = Q.poll();
                StringBuilder trace = sbQ.poll();

                if(cur == TARGET[i]) {
                    RES[i] = trace.toString(); return;
                }

                for (int d = 0; d < DN; ++d) {
                    short nv = command(cur, COMMAND[d]);
                    if(!TRACED[i][nv]) {
                        TRACED[i][nv] = true;
                        StringBuilder sb = new StringBuilder(trace);
                        sb.append(COMMAND[d]);
                        sbQ.offer(sb); new_size += 1; Q.offer(nv);
                    }
                }
            }
            size = new_size;
        }
    }

    private static short command(int n, char c) {
        if(c == 'D') {
            return (short) (n*2 >= 10000 ? (n*2) % 10000 : n*2);
        } else if(c == 'S') {
            return (short) (n-1 == -1 ? 9999 : n-1);
        } else if(c == 'L') {
            n *= 10;
            if(n >= 10000) n = (n % 10000) + (n / 10000);
            return (short) n;
        } else {
            int remain = n % 10; n = n / 10;
            if (remain > 0) n += remain * 1000;
            return (short) n;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Short.parseShort(br.readLine());

        CUR = new short[N]; TARGET = new short[N];
        RES = new String[N]; TRACED = new boolean[N][MAX_NUM];

        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            CUR[i] = Short.parseShort(st.nextToken());
            TARGET[i] = Short.parseShort(st.nextToken());
        }
    }
}
