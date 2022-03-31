import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    private static int[] parent, rank;
    private static int N, M;
    private static Set<Integer>[] PARTY;
    private static boolean NOPE[];

    public static void main(String[] args) throws IOException {
        input();
        init_parent();
        make_union();
        make_none();
        solution();
    }

    private static void make_none() {
        for(int i=1; i <= N; ++i) {
            if(NOPE[i]) NOPE[find(i)] = true;
        }
    }

    private static void make_union() {
        for (int i = 0; i < M; ++i) {
            Iterator<Integer> it = PARTY[i].iterator();
            int a = it.next();
            while(it.hasNext()) {
                int b = it.next();
                union(a, b);
                a = b;
            }
        }
    }

    private static void init_parent() {
        for(int i = 1; i <= N; ++i) parent[i] = i;
    }

    private static void solution() {
        int res = M;
        for (int i = 0; i < M; ++i) {
            Iterator<Integer> it = PARTY[i].iterator();
            if(NOPE[find(it.next())]) res -= 1;
        }
        System.out.println(res);
    }

    private static int find(int x) {
        if(x == parent[x]) return x;
        else return find(parent[x]);
    }

    private static void union(int x, int y) {
        int px = find(x), py = find(y);
        if(px != py) {
            if(px > py) parent[px] = py;
            else parent[py] = px;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nm = new StringTokenizer(br.readLine());

        N=Integer.parseInt(nm.nextToken()); M=Integer.parseInt(nm.nextToken());
        parent = new int[N+1]; rank = new int[N+1];
        NOPE = new boolean[N+1]; PARTY = new Set[N+1];

        StringTokenizer nope = new StringTokenizer(br.readLine());
        int NOPE_N = Integer.parseInt(nope.nextToken());
        while(NOPE_N-- > 0) NOPE[Integer.parseInt(nope.nextToken())] = true;

        for(int i = 0; i < M; ++i) {
            PARTY[i] = new HashSet<>();
            StringTokenizer party = new StringTokenizer(br.readLine());
            int party_n = Integer.parseInt(party.nextToken());

            while(party_n-- > 0)
                PARTY[i].add(Integer.parseInt(party.nextToken()));
        }
        br.close();
    }
}
