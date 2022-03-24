import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_HEIGHT = 256;
    private static int N, M, B;
    private static int[][] G;
    private static String[] R_DATAS;

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution();
    }

    private static void solution() {
        int res_time = Integer.MAX_VALUE, res_h = 0;

        for (int h = 0; h <= MAX_HEIGHT; ++h) {
            int _time = time(h);
            if(_time == -1) continue;
            if(_time <= res_time) { res_h = h; res_time = _time; }
        }
        System.out.print(res_time + " ");
        System.out.print(res_h);
    }

    private static int time(int h) {
        int removed = 0, added = 0;

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int difference = G[i][j]-h;

                if (difference >= 0) removed += (G[i][j]-h);
                else added -= difference;
            }
        }
        return ((removed+B) >= added) ? removed*2 + added : -1;
    }

    private static void init() {
        G = new int[N][M];

        for (int i = 0; i < N; ++i) {
            StringTokenizer row = new StringTokenizer(R_DATAS[i]);
            for (int j = 0; j < M; ++j)
                G[i][j] = Integer.parseInt(row.nextToken());
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer MNH = new StringTokenizer(br.readLine());

        N = Integer.parseInt(MNH.nextToken());
        M = Integer.parseInt(MNH.nextToken());
        B = Integer.parseInt(MNH.nextToken());

        R_DATAS = new String[N];
        for (int i = 0; i < N; ++i) R_DATAS[i] = br.readLine();
        br.close();
    }
}
