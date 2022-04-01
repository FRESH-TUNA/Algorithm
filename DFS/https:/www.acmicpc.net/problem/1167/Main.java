import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static List<Integer>[] E, D;
    private static boolean[] traced;
    private static int diameter, diameter_n;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        traced[1] = true;
        dfs(1, 0); diameter = 0;
        traced[1] = false; traced[diameter_n] = true;
        dfs(diameter_n, 0);
        System.out.println(diameter);
    }

    private static void dfs(int start, int cd) {
        Iterator<Integer> e = E[start].iterator();
        Iterator<Integer> d = D[start].iterator();

        while (e.hasNext()) {
            int ne = e.next(), nd = d.next();
            if(traced[ne]) continue;
            traced[ne] = true; cd += nd;
            if(diameter < cd) { diameter = cd; diameter_n = ne; }
            dfs(ne, cd);
            cd -= nd; traced[ne] = false;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine()); E=new List[N+1]; D=new List[N+1];

        for (int i = 1; i <= N; ++i)
            { E[i] = new LinkedList(); D[i] = new LinkedList(); }

        traced = new boolean[N+1];

        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            while(end != -1) {
                E[start].add(end);
                D[start].add(Integer.parseInt(st.nextToken()));
                end = Integer.parseInt(st.nextToken());
            }
        }
        br.close();
    }
}
