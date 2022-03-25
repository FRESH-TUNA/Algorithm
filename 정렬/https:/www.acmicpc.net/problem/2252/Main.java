import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M;
    private static List<Short>[] G;
    private static String[] EDGE_RAW_DATA;
    private static final StringBuilder RES = new StringBuilder();

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution();
    }

    private static void solution() {
        Queue<Short> Q = new LinkedList<>();
        for (short i = 1; i <= N; ++i) if(G[i].isEmpty()) Q.add(i);

        while (!Q.isEmpty()) {
            short node = Q.poll();
            RES.append(node); RES.append(' ');

            for (short i = 1; i <= N; ++i) {
                if(G[i].isEmpty()) continue;
                Iterator<Short> it = G[i].iterator();
                while (it.hasNext()) {if(node == it.next()) {it.remove(); break;}}
                if(G[i].isEmpty()) Q.offer(i);
            }
        }
        System.out.println(RES);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer NM = new StringTokenizer(br.readLine());
        N = Integer.parseInt(NM.nextToken()); M = Integer.parseInt(NM.nextToken());
        EDGE_RAW_DATA = new String[M];
        for (int i = 0; i < M; ++i) EDGE_RAW_DATA[i] = br.readLine();
        br.close();
    }

    private static void init() {
        G = new LinkedList[N+1];
        for(short i = 1; i <= N; ++i) G[i] = new LinkedList<>();

        for (String data : EDGE_RAW_DATA) {
            StringTokenizer st = new StringTokenizer(data);
            short start = Short.parseShort(st.nextToken());
            short end = Short.parseShort(st.nextToken());
            G[end].add(start);
        }
    }
}
