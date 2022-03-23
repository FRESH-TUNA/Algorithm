import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int[][] G;
    private static String[] G_RAW_DATA;
    private static final int[] RES = {0, 0, 0};

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution(0, 0, N);
        result();
    }

    private static void result() {
        StringBuilder sb = new StringBuilder();
        sb.append(RES[0]); sb.append('\n');
        sb.append(RES[1]); sb.append('\n');
        sb.append(RES[2]); sb.append('\n');
        System.out.print(sb);
    }

    private static void solution(int i, int j, int W) {
        if(check(i, j, W)) RES[G[i][j]+1] += 1;
        else {
            int NW = W / 3;
            for (int ni = i; ni < i+W; ni += NW) {
                for (int nj = j; nj < j+W; nj += NW)
                    solution(ni, nj, NW);
            }
        }
    }

    private static boolean check(int i, int j, int W) {
        int base = G[i][j];
        for (int ni = i; ni < i+W; ++ni) {
            for (int nj = j; nj < j+W; ++nj) {
                if(G[ni][nj] != base) return false;
            }
        }
        return true;
    }

    private static void init() {
        G = new int[N][N];
        for (int i = 0; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(G_RAW_DATA[i]);
            for (int j = 0; j < N; ++j)
                G[i][j] = Integer.parseInt(st.nextToken());
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        G_RAW_DATA = new String[N];
        for (int i = 0; i < N; ++i) G_RAW_DATA[i] = br.readLine();
    }
}
