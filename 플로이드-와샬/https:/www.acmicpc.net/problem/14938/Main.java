import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_D = 2000;
    private static int N, M;
    private static int[][] G;
    private static int[] ITEMS;

    public static void main(String[] args) throws IOException {
        input();
        fw();
        solution();
    }

    private static void solution() {
        int res = 0;

        for(int i = 1; i <= N; ++i) {
            int sub_res = 0;
            for(int j = 1; j <= N; ++j)
                if (G[i][j] <= M) sub_res += ITEMS[j];
            res = Math.max(res, sub_res);
        }
        System.out.println(res);
    }

    private static void fw() {
        for (int n = 1; n <= N; ++n) {
            for (int i = 1; i <= N; ++i)
                for (int j = 1; j <= N; ++j) {
                    if(G[i][j] > G[i][n]+G[n][j])
                        G[i][j] = G[i][n]+G[n][j];
                }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken()); M=Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        G=new int[N+1][N+1]; ITEMS=new int[N+1];
        for (int i = 1; i <= N; ++i) {
            Arrays.fill(G[i], MAX_D); G[i][i] = 0;
        }
        input_items(br); input_edges(R, br); br.close();
    }

    private static void input_items(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; ++i)
            ITEMS[i] = Integer.parseInt(st.nextToken());
    }

    private static void input_edges(int R, BufferedReader br) throws IOException {
        StringTokenizer st;
        while(R-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            G[n1][n2] = G[n2][n1] = Math.min(d, G[n1][n2]);
        }
    }
}
