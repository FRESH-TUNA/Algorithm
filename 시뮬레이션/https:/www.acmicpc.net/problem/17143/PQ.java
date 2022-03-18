import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PQ {
    private static int N, M, SHARKS_N;
    private static int[][][] GRAPH;
    private static PriorityQueue<int[]>[][] MOVED;
    private static Set<int[]> SHARKS;

    private static final int R = 0, C = 1, S = 2, D = 3, Z = 4;
    private static final int SHARKS_M = 5;
    private static final int[] DI = {0, -1, 1, 0, 0}, DJ = {0, 0, 0, 1, -1};
    private static final int[] NEWD = {0, 2, 1, 4, 3};

    public static void main(String[] args) throws IOException {
        input();
        moved_init();
        fishing();
    }

    private static void fishing() {
        int res = 0;
        for (int pos = 1; pos < M+1; ++pos) {
            res += catch_shark(pos);
            move_sharks();
            eat_sharks();
        }
        System.out.println(res);
    }

    private static int catch_shark(int col) {
        for(int row = 1; row < N+1; ++row)
            if(GRAPH[row][col] != null) {
                int[] shark = GRAPH[row][col];
                int res = shark[Z];
                SHARKS.remove(shark);
                GRAPH[row][col] = null;
                return res;
            }
        return 0;
    }

    private static void move_sharks() {
        for (int[] shark : SHARKS) { move_shark(shark); }
    }

    private static void eat_sharks() {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < M+1; ++j) {
                PriorityQueue<int[]> q = MOVED[i][j];
                if(q.isEmpty()) GRAPH[i][j] = null;
                else {
                    GRAPH[i][j] = q.poll();
                    SHARKS.removeAll(q);
                    q.clear();
                }
            }
        }
    }

    private static void move_shark(int[] f) {
        int r=f[R], c=f[C], s=f[S], d=f[D];
        r += s * DI[d]; c += s * DJ[d];

        while (true) {
            if(r < 1) { r = r*(-1) + 2; d = NEWD[d]; }
            else if(r > N) { r = N-(r-N); d = NEWD[d]; }
            else if(c < 1) { c = c*(-1) + 2; d = NEWD[d];}
            else if(c > M) { c = M-(c-M); d = NEWD[d]; }
            else break;
        }
        f[R]=r; f[C]=c; f[D]=d;
        MOVED[r][c].offer(f);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        SHARKS_N = Integer.parseInt(st.nextToken());

        GRAPH = new int[N+1][M+1][];
        SHARKS = new HashSet();
        for (int i = 0; i < SHARKS_N; ++i) {
            st = new StringTokenizer(br.readLine());
            int[] fish = new int[SHARKS_M];
            for (int j = 0; j < SHARKS_M; ++j)
                fish[j] = Integer.parseInt(st.nextToken());
            GRAPH[fish[R]][fish[C]] = fish;
            SHARKS.add(fish);
        }
        br.close();
    }

    private static void moved_init() {
        MOVED = new PriorityQueue[N+1][M+1];
        for (int i = 1; i < N+1; ++i)
            for (int j = 1; j < M+1; ++j)
                MOVED[i][j] = new PriorityQueue<>((a, b) -> compareQ(a, b));
    }
    private static int compareQ(int[] a, int[] b) { return b[Z] - a[Z]; }


    /*
     * tests
     */
    private static void graph_init_test() {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < M+1; ++j) {
                if(GRAPH[i][j] == null)
                    System.out.print(0 + " ");
                else
                    System.out.print(GRAPH[i][j][Z] + " ");
            }
            System.out.println();
        }
        System.out.println("------------");
    }

    private static void sharks_init_test() {
        for (int[] fish : SHARKS) {
            System.out.print(fish[R] + " ");
            System.out.print(fish[C] + " ");
            System.out.print(fish[S] + " ");
            System.out.print(fish[D] + " ");
            System.out.print(fish[Z] + "\n");
        }
    }
}
