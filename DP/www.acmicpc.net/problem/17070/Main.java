import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static boolean[][] graph;
    private static int[][][] db;

    public static void main(String[] args) throws IOException {
        input(); init(); solution();
    }

    private static void solution() {
        for (int i = 1; i < N; ++i) {
            for (int j = 1; j < N; ++j) {
                if(graph[i][j]) continue;
                db[i][j][0] = db[i][j - 1][0] + db[i][j - 1][1];
                if(!graph[i-1][j] && !graph[i][j-1])
                    db[i][j][1] = db[i-1][j-1][0] + db[i-1][j-1][1] + db[i-1][j-1][2];
                db[i][j][2] = db[i - 1][j][1] + db[i - 1][j][2];
            }
        }

        System.out.println(Arrays.stream(db[N-1][N-1]).sum());
    }

    private static void init() {
        for (int i = 1; i < N; ++i) {
            if(!graph[0][i]) db[0][i][0] = 1;
            else break;
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new boolean[N][N]; db = new int[N][N][3];
        for (int i = 0; i < N; ++i) {
            StringTokenizer row = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; ++j)
                graph[i][j] = row.nextToken().equals("1");
        }
        br.close();
    }
}
