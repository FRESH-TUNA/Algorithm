import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int START = 1, MAX_D = 250000000;
    private static int TEST_N;
    private static int[] N;
    private static List<Integer>[] S, E, D;

    public static void main(String[] args) throws IOException {
        init();
        solution();
    }

    private static void solution() {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < TEST_N; ++i) {
            res.append(bf(i) ? "YES" : "NO");
            res.append('\n');
        }
        System.out.print(res);
    }

    private static boolean bf(int i) {
        int[] dists = new int[N[i]+1];
        Arrays.fill(dists, MAX_D);
        dists[START] = 0;

        for(int j = 0; j < N[i]; ++j) {
            Iterator<Integer> s = S[i].iterator();
            Iterator<Integer> e = E[i].iterator();
            Iterator<Integer> d = D[i].iterator();

            while(s.hasNext()) {
                int sv = s.next(), ev = e.next(), dv = d.next();
                if(dists[ev] > dists[sv] + dv) {
                    dists[ev] = dists[sv] + dv;
                    if (j == N[i] - 1) return true;
                }
            }
        }
        return false;
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        TEST_N = Integer.parseInt(br.readLine());
        S = new List[TEST_N]; D = new List[TEST_N];
        E = new List[TEST_N]; N = new int[TEST_N];

        for(int i = 0; i < TEST_N; ++i) {
            D[i] = new LinkedList<>(); E[i] = new LinkedList<>();
            S[i] = new LinkedList<>(); init_test(br, i);
        }
        br.close();
    }

    private static void init_test(BufferedReader br, int i) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N[i] = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int s, e, d;

        while(m-- > 0) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            S[i].add(s); E[i].add(e); D[i].add(d);
            S[i].add(e); E[i].add(s); D[i].add(d);
        }

        while (w-- > 0) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            S[i].add(s); E[i].add(e); D[i].add(d*(-1));
        }
    }
}
