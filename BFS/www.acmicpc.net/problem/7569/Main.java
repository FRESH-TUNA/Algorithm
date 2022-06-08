import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int D_N = 6;
    private static final int[] DN = {-1, 0, 1, 0, 0, 0};
    private static final int[] DM = {0, 1, 0, -1, 0, 0};
    private static final int[] DH = {0, 0, 0, 0, 1, -1};

    private static final Queue<Integer> TN = new LinkedList<>(),
            TM = new LinkedList<>(), TH = new LinkedList<>();

    private static int M, N, H, TOMATO_N = 0, FERMENT = -1;
    private static int[][][] G;
    private static String[][] box_data;

    public static void main(String[] args) throws IOException {
        input();
        init();
        ferment();
        result();
    }

    private static void result() {
        System.out.println(TOMATO_N == 0 ? FERMENT : -1);
    }

    private static void ferment() {
        while (!TN.isEmpty()) {
            int iteration_size = TH.size();
            while (iteration_size-- > 0) trace(TH.poll(), TN.poll(), TM.poll());
            FERMENT += 1;
        }
    }

    private static void trace(int h, int n, int m) {
        for(int d = 0; d < D_N; ++d) {
            int nh = h+DH[d], nn = n+DN[d], nm = m+DM[d];

            if(nh == -1 || nh == H || nn == -1 || nn == N) continue;
            if(nm == -1 || nm == M || G[nh][nn][nm] != 0) continue;
            G[nh][nn][nm] = 1;
            --TOMATO_N;
            TH.offer(nh); TN.offer(nn); TM.offer(nm);
        }
    }

    private static void init() {
        G = new int[H][N][M];

        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < N; ++j) {
                StringTokenizer col = new StringTokenizer(box_data[i][j]);
                for (int k = 0; k < M; ++k) {
                    G[i][j][k] = Integer.parseInt(col.nextToken());
                    if(G[i][j][k] == 1) { TH.offer(i); TN.offer(j); TM.offer(k); }
                    if(G[i][j][k] == 0) TOMATO_N += 1;
                }
            }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer MNH = new StringTokenizer(br.readLine());

        M = Integer.parseInt(MNH.nextToken());
        N = Integer.parseInt(MNH.nextToken());
        H = Integer.parseInt(MNH.nextToken());

        box_data = new String[H][N];
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < N; ++j)
                box_data[i][j] = br.readLine();
        br.close();
    }
}
