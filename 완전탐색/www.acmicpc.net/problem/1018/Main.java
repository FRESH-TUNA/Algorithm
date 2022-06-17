import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int WHITE = 0, BLACK = 1;
    private static final int CHESS_N = 8, CHESS_NxN = 64;
    private static int ROW, COL;
    private static int[][] BOARD;
    private static final int[][] NORMAL_CHESS = {
            {1, 0, 1, 0, 1, 0, 1, 0},
            {0, 1, 0, 1, 0, 1, 0, 1},
            {1, 0, 1, 0, 1, 0, 1, 0},
            {0, 1, 0, 1, 0, 1, 0, 1},
            {1, 0, 1, 0, 1, 0, 1, 0},
            {0, 1, 0, 1, 0, 1, 0, 1},
            {1, 0, 1, 0, 1, 0, 1, 0},
            {0, 1, 0, 1, 0, 1, 0, 1}
    };
    private static int answer = CHESS_NxN;


    public static void main(String[] args) throws IOException {
        input();
        checks();
        System.out.println(answer);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] r_c = br.readLine().split(" ");
        ROW = Integer.parseInt(r_c[0]); COL = Integer.parseInt(r_c[1]);
        BOARD = new int[ROW][COL];

        for (int i = 0; i < ROW; ++i) {
            String row = br.readLine();
            for(int j = 0; j < COL; ++j)
                BOARD[i][j] = row.charAt(j) == 'W' ? WHITE : BLACK;
        }
    }

    private static void checks() {
        for(int i = 0; i <= ROW - CHESS_N; ++i)
            for(int j = 0; j <= COL - CHESS_N; ++j)
                check(i, j);
    }

    private static void check(int i, int j) {
        int X = i + CHESS_N, Y = j + CHESS_N;
        int res = 0;
        for(int x = i; x < X; ++x) {
            for(int y = j; y < Y; ++y)
                if(BOARD[x][y] != NORMAL_CHESS[x-i][y-j]) res += 1;
        }
        answer = Math.min(answer, Math.min(res, CHESS_NxN-res));
    }

    /*
     * tests
     */
    private static void input_test() {
        for (int i = 0; i < ROW; ++i) {
            for(int j = 0; j < COL; ++j)
                System.out.print(BOARD[i][j]);
            System.out.println();
        }
    }
}
