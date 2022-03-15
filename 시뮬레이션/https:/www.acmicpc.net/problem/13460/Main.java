import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import static java.util.Map.entry;

public class Main {
    // NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
    private static final int[] DX = {-1, 0, 1, 0}, DY = {0, 1, 0, -1};
    private static final int[][] D_FRONT = {{0, -1}, {1, 1}, {0, 1}, {1, -1}};
    private static final int[][] ND = {{1, 3}, {0, 2}, {1, 3}, {0, 2}};
    private static final int MAX_RES = 10, D = 4;

    private static char[][] GRAPH;
    private static int ROW, COL;
    private static int res = MAX_RES + 1;

    //for test
    private static final Map<Integer, String> IDX_TO_D = Map.ofEntries(
            entry(0, "NORTH"), entry(1, "EAST"),
            entry(2, "SOUTH"), entry(3, "WEST")
    );


    public static void main(String[] args) throws IOException {
        input();
        find_red_blue_balls();
        calc();
        System.out.println(res == MAX_RES+1 ? -1 : res);
    }

    private static int[] find_red_blue_balls() {
        int[] rb_idxs = {-1, -1, -1, -1};

        for (int i = 0; i < ROW; ++i) {
            for (int j = 0; j < COL; ++j) {
                if(GRAPH[i][j] == 'R') { rb_idxs[0] = i; rb_idxs[1] = j; }
                if(GRAPH[i][j] == 'B') { rb_idxs[2] = i; rb_idxs[3] = j; }
                if(rb_idxs[0]+rb_idxs[1] >= 0 && rb_idxs[2]+rb_idxs[3] >= 0)
                    return rb_idxs;
            }
        }
        return rb_idxs;
    }

    private static void calc() {
        int[] ijs = find_red_blue_balls();
        for(int i = 0; i < D; ++i)
            dfs(i, 1, ijs, copy_graph(GRAPH));
    }

    private static void dfs(int d, int count, int[] ijs, char[][] graph) {
        if(count == MAX_RES | count >= res) return;
        int[] rij = {ijs[0], ijs[1]}, bij = {ijs[2], ijs[3]};
        int idx = D_FRONT[d][0], mpy = D_FRONT[d][1];
        int r_priority = rij[idx] * mpy, b_priority = bij[idx] * mpy;

        if(r_priority >= b_priority) {
            boolean rij_res = move(rij, d, graph);
            boolean bij_res = move(bij, d, graph);

            if(!rij_res && bij_res) {
                res = Math.min(count, res);
                return;
            }
            if(!bij_res) return;
        }
        else {
            boolean bij_res = move(bij, d, graph);
            boolean rij_res = move(rij, d, graph);

            if(!bij_res) return;
            if(!rij_res) {
                res = Math.min(count, res);
                return;
            }
        }

        // adjusting
        if (rij[0] == bij[0] && rij[1] == bij[1]) {
            if(r_priority >= b_priority) {
                int oi = bij[0], oj = bij[1];
                bij[0] -= DX[d]; bij[1] -= DY[d];
                swap(oi, oj, bij[0], bij[1], graph);
            }
            else {
                int oi = rij[0], oj = rij[1];
                rij[0] -= DX[d]; rij[1] -= DY[d];
                swap(oi, oj, rij[0], rij[1], graph);
            }
        }

        //dfs
        for(int nd : ND[d]) {
            dfs(nd, count + 1, new int[]{rij[0], rij[1], bij[0], bij[1]},
                    copy_graph(graph));
        }
    }



    private static boolean move(int[] ij, int d, char[][] graph) {
        int oi = ij[0], oj = ij[1];
        while(true) {
            ij[0] += DX[d]; ij[1] += DY[d];
            if(graph[ij[0]][ij[1]] == '#') {
                ij[0] -= DX[d]; ij[1] -= DY[d];
                swap(oi, oj, ij[0], ij[1], graph);
                return true;
            }
            if(graph[ij[0]][ij[1]] == 'O') return false;
        }
    }

    private static void swap(int i, int j, int x, int y, char[][] graph) {
        char temp = graph[i][j];
        graph[i][j] = graph[x][y];
        graph[x][y] = temp;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] R_AND_C = br.readLine().split(" ");

        ROW = Integer.parseInt(R_AND_C[0]); COL = Integer.parseInt(R_AND_C[1]);
        GRAPH = new char[ROW][];

        for(int i = 0; i < ROW; ++i) GRAPH[i] = br.readLine().toCharArray();
        br.close();
    }

    private static char[][] copy_graph(char[][] graph) {
        char[][] copied_graph = new char[ROW][COL];

        for(int i = 0; i < ROW; ++i)
            for(int j = 0; j < COL; ++j)
                copied_graph[i][j] = graph[i][j];
        return copied_graph;
    }

    /*
     * tests
     */
//    private static void find_red_blue_ball_test() {
//        int[] a = find_red_blue_balls();
//        for(int i = 0; i < a.length; ++i) System.out.print(a[i] + " ");
//    }
//
//    private static void print_graph(char[][] graph) {
//        for(int i = 0; i < ROW; ++i) {
//            for (int j = 0; j < COL; ++j)
//                System.out.print(graph[i][j]);
//            System.out.println();
//        }
//    }
}
