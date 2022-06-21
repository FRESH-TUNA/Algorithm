import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static List<Integer>[] E, D;
    private static boolean[] traced;
    private static int N;
    private static int DEST = 1, LEN;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        traced[1] = true;
        dfs(1, 0);
        traced[1] = false; traced[DEST] = true;
        dfs(DEST, 0);
        System.out.println(LEN);
    }

    private static void dfs(int i, int len) {
        Iterator<Integer> ni_it = E[i].iterator();
        Iterator<Integer> nd_it = D[i].iterator();

        while(ni_it.hasNext()) {
            int ni = ni_it.next(), nd = nd_it.next();
            if(traced[ni]) continue;
            traced[ni] = true;
            if(len + nd > LEN) {
                LEN = nd + len; DEST = ni;
            }
            dfs(ni, len + nd);
            traced[ni] = false;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        E = new List[N+1]; D = new List[N+1]; traced = new boolean[N+1];

        for(int i = 1; i <= N; ++i) {
            E[i] = new LinkedList<>(); D[i] = new LinkedList<>();
        }

        input_edges(br);
        br.close();
    }

    private static void input_edges(BufferedReader br) throws IOException {
        StringTokenizer t;
        for(int i = 0; i < N-1; ++i) {
             t = new StringTokenizer(br.readLine());
             int n1 = Integer.parseInt(t.nextToken());
             int n2 = Integer.parseInt(t.nextToken());
             int d = Integer.parseInt(t.nextToken());

             E[n1].add(n2); E[n2].add(n1);
             D[n1].add(d); D[n2].add(d);
        }
    }
}
