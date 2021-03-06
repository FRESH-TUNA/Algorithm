import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M, SHARKS_N;
    private static int[][][] GRAPH, MOVED;
    private static Set<int[]> SHARKS;

    private static final int R = 0, C = 1, S = 2, D = 3, Z = 4;
    private static final int SHARKS_M = 5;
    private static final int[] DI = {0, -1, 1, 0, 0}, DJ = {0, 0, 0, 1, -1};
    private static final int[] NEWD = {0, 2, 1, 4, 3};

    public static void main(String[] args) throws IOException {
        input();
        fishing();
    }

    private static void fishing() {
        int res = 0;
        for (int pos = 1; pos < M+1; ++pos) {
            res += catch_shark(pos);
            move_eat_sharks();
            apply_to_graph();
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

    private static void move_eat_sharks() {
        Set<int[]> eaten = new HashSet<>();

        for (int[] shark : SHARKS) {
            move_shark(shark);
            int r = shark[R], c = shark[C];
            int[] premoved = MOVED[r][c];

            if(premoved == null) MOVED[r][c] = shark;
            else if(shark[Z] > premoved[Z]) {
                MOVED[r][c] = shark;
                eaten.add(premoved);
            } else { eaten.add(shark); }
        }

        SHARKS.removeAll(eaten);
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
    }

    private static void apply_to_graph() {
        for(int i = 1; i < N+1; ++i) {
            for(int j = 1; j < M+1; ++j) {
                GRAPH[i][j] = MOVED[i][j];
                MOVED[i][j] = null;
            }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        SHARKS_N = Integer.parseInt(st.nextToken());

        GRAPH = new int[N+1][M+1][];
        MOVED = new int[N+1][M+1][];
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
}
