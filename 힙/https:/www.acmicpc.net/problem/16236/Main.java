import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class Main {
    private static int SI, SJ;
    private static int S = 2, EXP = 0;
    private static int N;
    private static int[][] graph;
    private static boolean[][] traced;
    private static final int[] DI = {-1, 0, 0, 1}, DJ = {0, -1, 1, 0};
    private static final int DN = 4;

    public static void main(String[] args) throws IOException {
        input();
        find_shark();
        solution();
    }

    private static void solution() {
        int res = 0;
        while (true) {
            int _res = trace();
            if(_res == -1) break;
            res += _res;
            traced_init();
        }
        System.out.println(res);
    }

    private static int trace() {
        PriorityQueue<int[]> Q = new PriorityQueue<int[]>(Main::compare);
        Q.add(new int[]{0, SI, SJ});
        traced[SI][SJ] = true;

        while (!Q.isEmpty())  {
            int[] ijd = Q.poll();
            int i = ijd[1], j = ijd[2], d = ijd[0];
            int type = graph[i][j];

            if(type != 0 && type != 9 && type < S) {
                eat_fish(i, j);
                return d;
            }

            for (int direction = 0; direction < DN; ++direction) {
                int ni = i+DI[direction], nj = j+DJ[direction];
                if(ni == -1 || ni == N || nj == -1 || nj == N)
                    continue;
                if(traced[ni][nj] || graph[ni][nj] > S)
                    continue;
                traced[ni][nj] = true;
                Q.offer(new int[] {d+1, ni, nj});
            }
        }
        return -1;
    }

    private static int bfs() {
        LinkedList<Integer> iQ, jQ, dQ;
        iQ=new LinkedList<>(); jQ=new LinkedList<>(); dQ=new LinkedList<>();
        iQ.addLast(SI); jQ.addLast(SJ); dQ.addLast(0);
        traced[SI][SJ] = true;

        while (dQ.size() > 0) {
            int i = iQ.removeFirst(), j = jQ.removeFirst(), d = dQ.removeFirst();
            for (int direction = 0; direction < DN; ++direction) {
                int ni = i+DI[direction], nj = j+DJ[direction];
                if(ni == -1 || ni == N || nj == -1 || nj == N)
                    continue;
                if(traced[ni][nj] || graph[ni][nj] > S)
                    continue;
                if(graph[ni][nj] != 0 && graph[ni][nj] < S) {
                    eat_fish(ni, nj);
                    return d+1;
                }
                traced[ni][nj] = true;
                iQ.addLast(ni); jQ.addLast(nj); dQ.addLast(d+1);
            }
        }
        return -1;
    }

    private static void find_shark() {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                if (graph[i][j] == 9) {
                    SI = i;
                    SJ = j;
                    return;
                }
        }
    }

    private static void eat_fish(int i, int j) {
        graph[i][j] = 9;
        graph[SI][SJ] = 0;
        EXP = (EXP + 1) % S;
        if(EXP == 0) S += 1;
        SI = i; SJ = j;
    }

    private static void traced_init() {
        for (int i = 0; i < N; ++i) Arrays.fill(traced[i], false);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new int[N][];
        for (int i = 0; i < N; ++i) {
            graph[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(x -> Integer.parseInt(x)).toArray();
        }
        traced = new boolean[N][N];
        br.close();
    }

    private static int compare(int[] a, int[] b) {
        if(a[0] != b[0]) return a[0]-b[0];
        if(a[1] != b[1]) return a[1]-b[1];
        if(a[2] != b[2]) return a[2]-b[2];
        return 0;
    }
}
