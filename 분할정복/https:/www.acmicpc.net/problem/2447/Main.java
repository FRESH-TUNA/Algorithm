import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2447 {
    private static int N;
    private static char[][] graph;

    public static void main(String[] args) throws IOException {
        init();
        draw(0, 0, N);
        print();
    }

    private static void draw(int i, int j, int w) {
        if(w != 3) {
            int nw = w/3;
            for (int ni = i; ni < i+w; ni += nw)
                for (int nj = j; nj < j+w; nj += nw)
                    if(!(ni == i+nw && nj == j+nw)) draw(ni, nj, nw);
        }
        else {
            for (int ni = i; ni < i+w; ni++)
                for (int nj = j; nj < j+w; nj++)
                    graph[ni][nj] = '*';
            graph[i+1][j+1] = ' ';
        }
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new char[N][N];
        for(char[] row : graph) Arrays.fill(row, ' ');
        br.close();
    }

    private static void print() {
        StringBuilder res = new StringBuilder();
        for(char[] row : graph) { res.append(row); res.append('\n'); }
        System.out.print(res);
    }
}
