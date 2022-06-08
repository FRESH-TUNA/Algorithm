import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {
    private static final int DN = 4;
    private static final int[] DI = {-1, 0, 1, 0}, DJ = {0, 1, 0, -1};
    private static int N, L, R;
    private static int[][] graph;


    public static void main(String[] args) throws IOException {
        input();
        System.out.println(solution());
    }

    private static int solution() {
        int res = 0;
        while (true) {
            boolean[][] traced = new boolean[N][N];
            int moved_peoples = 0;
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j)
                    if(!traced[i][j]) moved_peoples += bfs(traced, i, j);
            }
            if(moved_peoples == 0) return res;
            res += 1;
        }
    }

    private static int bfs(boolean[][] traced, int i, int j) {
        int traced_sum = graph[i][j];
        LinkedList<Integer> IQ = new LinkedList<>(), JQ = new LinkedList<>();
        List<Integer> TI = new ArrayList<>(), TJ = new ArrayList<>();
        IQ.add(i); JQ.add(j); TI.add(i); TJ.add(j);
        traced[i][j] = true;

        while (IQ.size() > 0) {
            int ci = IQ.removeFirst(), cj = JQ.removeFirst();

            for (int d = 0; d < DN; ++d) {
                int ni = ci+DI[d], nj = cj+DJ[d];
                if(ni == -1 || ni == N || nj == -1 || nj == N || traced[ni][nj])
                    continue;

                int difference = Math.abs(graph[ni][nj]-graph[ci][cj]);
                if(difference < L || difference > R) continue;
                traced[ni][nj] = true;
                traced_sum += graph[ni][nj];
                TI.add(ni); TJ.add(nj); IQ.add(ni); JQ.add(nj);
            }
        }
        distribute(TI, TJ, traced_sum);
        return TI.size() - 1;
    }

    private static void distribute(List<Integer> ti, List<Integer> tj, int traced_sum) {
        int value = traced_sum / ti.size();
        for(int i = 0; i < ti.size(); ++i) graph[ti.get(i)][tj.get(i)] = value;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NLR = br.readLine().split(" ");
        N = Integer.parseInt(NLR[0]);
        L = Integer.parseInt(NLR[1]);
        R = Integer.parseInt(NLR[2]);

        graph = new int[N][];
        for(int i = 0; i < N; ++i) {
            graph[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(x -> Integer.parseInt(x)).toArray();
        }
        br.close();
    }

    /*
     * tests
     */
    private static void input_test() {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                System.out.print(graph[i][j]);
            System.out.println();
        }
    }
}
