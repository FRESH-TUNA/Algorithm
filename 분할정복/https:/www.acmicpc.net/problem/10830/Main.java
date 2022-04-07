import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int DIVIDER = 1000;
    private static int N;
    private static long B;
    private static int[][] M;

    public static void main(String[] args) throws IOException {
        input();
        divide(M);
        print(solution(B));
    }

    private static void print(int[][] solution) {
        for(int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                System.out.print(solution[i][j] + " ");
            System.out.println();
        }
    }

    private static int[][] mxm(int[][] x, int[][] y) {
        int[][] res = new int[N][N];
        for(int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                multipling(res, x, y, i, j);
        return res;
    }
    private static void multipling(int[][] res, int[][] x, int[][] y, int i, int j) {
        int v = 0;
        for(int k = 0; k < N; ++k) v += (x[i][k] * y[k][j]);
        res[i][j] = v;
    }

    private static int[][] divide(int[][] source) {
        for(int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                source[i][j] %= DIVIDER;
        return source;
    }

    private static int[][] solution(long b) {
        if(b == 1L) return M;

        long nb = b / 2;
        int[][] nbM = solution(nb);

        if((b & 1) == 0)
            return divide(mxm(nbM, nbM));
        else
            return divide(mxm(divide(mxm(nbM, nbM)), M));
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken()); B=Long.parseLong(st.nextToken());
        M=new int[N][N];
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; ++j)
                M[i][j] = Integer.parseInt(st.nextToken());
        }
        br.close();
    }
}
