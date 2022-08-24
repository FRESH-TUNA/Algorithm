import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int[] BOXES;
    private static int[][] DB;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        Arrays.fill(DB[0], 1);
        for(int t = 1; t < N; ++t) {
            DB[t][0] = 1;
            for (int i = 1; i < N; ++i)
                DB[t][i] = determine(t-1, i);
        }
        System.out.println(Arrays.stream(DB[N-1]).max().getAsInt());
    }

    private static int determine(int t, int i) {
        int res = 0;
        for (int x = 0; x < i; ++x)
            if(BOXES[i] > BOXES[x]) res = Math.max(res, DB[t][x]);
        return res+1;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        BOXES = new int[N];
        DB = new int[N][N];

        StringTokenizer boxes = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) BOXES[i] = Integer.parseInt(boxes.nextToken());
        br.close();
    }
}
