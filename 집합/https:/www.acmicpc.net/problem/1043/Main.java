import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class B1149 {
    private static final Set<Integer> NOPE = new HashSet<>();
    private static int N, M;
    private static Set<Integer>[] PARTY;

    public static void main(String[] args) throws IOException {
        input();
        nope();
        solution();
    }

    private static void nope() {
        for (int i = 0; i < M; ++i)
            for (Set<Integer> s : PARTY) {
                for (int n : NOPE) {
                    if (s.contains(n)) {
                        NOPE.addAll(s);
                        break;
                    }
                }
            }
    }

    private static void solution() {
        for (Set<Integer> s : PARTY) {
            for(int n : NOPE) {
                if(s.contains(n)) {
                    M -= 1;
                    break;
                }
            }
        }
        System.out.println(M);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nm = new StringTokenizer(br.readLine());

        N=Integer.parseInt(nm.nextToken()); M=Integer.parseInt(nm.nextToken());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int nope_n = Integer.parseInt(st.nextToken());
        while (nope_n-- > 0) NOPE.add(Integer.parseInt(st.nextToken()));

        PARTY = new Set[M];
        for(int i = 0; i < M; ++i) {
            PARTY[i] = new HashSet<>();
            st = new StringTokenizer(br.readLine());
            int set_n = Integer.parseInt(st.nextToken());
            while (set_n-- > 0) PARTY[i].add(Integer.parseInt(st.nextToken()));
        }
        br.close();
    }
}
