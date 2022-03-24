import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int N;
    private static char[][] G;
    private static final StringBuilder RES = new StringBuilder();

    public static void main(String[] args) throws IOException {
        init();
        compress(0, 0, N);
        print();
    }

    private static void compress(int i, int j, int w) {
        if(can_compress(i, j, w)) RES.append(G[i][j]);
        else {
            int nw = w/2;
            RES.append('(');
            for (int ni = i; ni < i+w; ni += nw)
                for (int nj = j; nj < j+w; nj += nw)
                    compress(ni, nj, nw);
            RES.append(')');
        }
    }

    private static boolean can_compress(int i, int j, int w) {
        char base = G[i][j];
        for (int ni = i; ni < i+w; ni++)
            for (int nj = j; nj < j+w; nj++)
                if(base != G[ni][nj]) return false;
        return true;
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        G = new char[N][];
        for (int i = 0; i < N; ++i) G[i] = br.readLine().toCharArray();
        br.close();
    }

    private static void print() {
        System.out.print(RES);
    }
}
