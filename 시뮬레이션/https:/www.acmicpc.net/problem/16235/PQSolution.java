import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PQSolution {
    private static final int INIT_NUTIRENT = 5, DN = 8;
    private static final int[] DI = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static final int[] DJ = {0, 1, 1, 1, 0, -1, -1, -1};
    private static int N, M, K;
    private static int[][] FEED, nutirent;
    private static PriorityQueue<Integer>[][] graph;

    public static void main(String[] args) throws IOException {
        input();
        aging();
        result();
    }

    private static void aging() {
        while (K > 0) {
            spring_summer();
            autumn();
            winter();
            K -= 1;
        }
    }

    private static void spring_summer() {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < N+1; ++j) {
                PriorityQueue<Integer> newQ = new PriorityQueue<>();
                while (!graph[i][j].isEmpty() && nutirent[i][j] >= graph[i][j].peek()) {
                    int age = graph[i][j].remove();
                    newQ.offer(age + 1);
                    nutirent[i][j] -= age;
                }
                FEED[i][j] += graph[i][j].stream().mapToInt(x -> x/2).sum();
                graph[i][j] = newQ;
            }
        }
    }

    private static void autumn() {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < N+1; ++j) {
                int new_tree_count = (int) graph[i][j].stream()
                        .filter(x -> x % 5 == 0).count();
                for(int d = 0; d < DN; ++d) {
                    int ni = i+DI[d], nj = j+DJ[d];
                    if (ni == 0 || ni == N+1 || nj == 0 || nj == N+1)
                        continue;
                    for(int k = 0; k < new_tree_count; ++k)
                        graph[ni][nj].add(1);
                }
            }
        }
    }

    private static void winter() {
        for (int i = 1; i < N+1; ++i)
            for (int j = 1; j < N+1; ++j)
                nutirent[i][j] += FEED[i][j];
    }

    private static void result() {
        int res = 0;
        for (int i = 1; i < N+1; ++i)
            for (int j = 1; j < N+1; ++j)
                res += graph[i][j].size();
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NLR = br.readLine().split(" ");
        N = Integer.parseInt(NLR[0]);
        M = Integer.parseInt(NLR[1]);
        K = Integer.parseInt(NLR[2]);

        FEED = new int[N+1][]; nutirent = new int[N+1][];
        for(int i = 1; i < N+1; ++i) {
            FEED[i] = new int[N+1];
            int[] feed_data = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(x -> Integer.parseInt(x)).toArray();
            for(int j = 1; j < N+1; ++j) FEED[i][j] = feed_data[j-1];

            nutirent[i] = new int[N+1];
            Arrays.fill(nutirent[i], INIT_NUTIRENT);
        }

        graph = new PriorityQueue[N+1][];
        for (int i = 1; i < N+1; ++i) {
            graph[i] = new PriorityQueue[N+1];
            for (int j = 1; j < N+1; ++j) graph[i][j] = new PriorityQueue<>();
        }

        for (int it = 0; it < M; ++it) {
            String[] ijy = br.readLine().split(" ");
            graph[Integer.parseInt(ijy[0])][Integer.parseInt(ijy[1])]
                    .add(Integer.parseInt(ijy[2]));
        }
        br.close();
    }

    /*
     * tests
     */
    private static void input_test() {
        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < N+1; ++j)
                System.out.print(nutirent[i][j] + " ");
            System.out.println();
        }
    }
}
