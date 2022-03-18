import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N, M, T;
    private static int[][] graph;
    private static int[][] propagetes;

    private static final int[] DI = {-1, 0, 0, 1}, DJ = {0, -1, 1, 0};
    private static final int L = 0, R = 1;
    private static final int[][] CI = {{0, -1, 0, 1}, {0, 1, 0, -1}};
    private static final int[][] CJ = {{1, 0, -1, 0}, {1, 0, -1, 0}};
    private static final int DN = 4;

    public static void main(String[] args) throws IOException {
        input();
        cleaning();
        print();
    }

    private static void cleaning() {
        int CLEANER_START_ROW = find_cleaner_start_row();
        while (T-- > 0) {
            propagate();
            circulate(CLEANER_START_ROW, 0, L);
            circulate(CLEANER_START_ROW+1, 0, R);
        }
    }

    private static int find_cleaner_start_row() {
        for (int i = 0; i < N; ++i)
            if(graph[i][0] == -1) return i;
        return 0;
    }

    private static void propagate() {
        for (int i = 0; i < N; ++i){
            for (int j = 0; j < M; ++j){
                if (graph[i][j] == 0 || graph[i][j] == -1) continue;
                int propagated = graph[i][j] / 5, count = 0;
                for(int d = 0; d < DN; ++d) {
                    int ni = i + DI[d], nj = j + DJ[d];
                    if(ni == -1 || ni == N || nj == -1 || nj == M)
                        continue;
                    if(graph[ni][nj] == -1) continue;
                    propagetes[ni][nj] += propagated;
                    count += 1;
                }
                graph[i][j] -= propagated * count;
            }
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                graph[i][j] += propagetes[i][j];
                propagetes[i][j] = 0;
            }
        }
    }

    private static void circulate(int i, int j, int c) {
        int d = 0;
        int ni = i + CI[c][d], nj = j + CJ[c][d];
        int prev = 0;

        while(ni != i || nj != j) {
            int next_prev = graph[ni][nj];
            graph[ni][nj] = prev;
            prev = next_prev;

            ni += CI[c][d]; nj += CJ[c][d];
            if(ni == -1 || ni == N || nj == -1 || nj == M) {
                ni -= CI[c][d]; nj -= CJ[c][d];
                d += 1;
                ni += CI[c][d]; nj += CJ[c][d];
            }
        }
    }

    private static void print() {
        int res = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (graph[i][j] == -1) continue;
                res += graph[i][j];
            }
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        graph = new int[N][];
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            graph[i] = new int[M];
            for(int j = 0; j < M; ++j)
                graph[i][j] = Integer.parseInt(st.nextToken());
        }
        propagetes = new int[N][M];
        br.close();
    }
}
