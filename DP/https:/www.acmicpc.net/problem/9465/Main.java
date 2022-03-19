import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int CARDS_N;
    private static int[] MS;
    private static int[][][] CARDS;
    private static int[][][] DB;
    private static final int N = 2;
    private static final int MAX_M = 100000;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < CARDS_N; ++i) {
            ans.append(max_score(i));
            ans.append('\n');
        }
        System.out.print(ans);
    }

    private static int max_score(int card) {
        int C = MS[card];
        for (int c = 1; c <= C; ++c) {
            int zero = DB[card][0][c-1];
            int one = DB[card][1][c-1];
            int two = DB[card][2][c-1];
            DB[card][0][c] = Math.max(Math.max(zero, one), two);
            DB[card][1][c] = Math.max(zero, two) + CARDS[card][1][c];
            DB[card][2][c] = Math.max(zero, one) + CARDS[card][2][c];
        }
        return Math.max(Math.max(DB[card][0][C], DB[card][1][C]), DB[card][2][C]);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        CARDS_N = Integer.parseInt(br.readLine());
        MS = new int[CARDS_N];
        CARDS = new int[CARDS_N][N+1][MAX_M+1];
        DB = new int[CARDS_N][N+1][MAX_M+1];
        for (int i = 0; i < CARDS_N; ++i) {
            MS[i] = Integer.parseInt(br.readLine());
            input_cards(br, i);
        }
        br.close();
    }

    private static void input_cards(BufferedReader br, int i) throws IOException {
        for (int r = 1; r <= N; r++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int c = 1; c <= MS[i]; ++c)
                CARDS[i][r][c] = Integer.parseInt(st.nextToken());
        }
    }

    /*
     * tests
     */
    private static void test() {
        for (int i = 0; i < CARDS_N; ++i) {
            for (int r = 1; r <= N; r++) {
                for (int c = 1; c <= MS[i]; ++c)
                    System.out.print(CARDS[i][r][c]  + "/" + DB[i][r][c] + " ");
                System.out.println();
            }
            System.out.println("----------");
        }
    }
}
