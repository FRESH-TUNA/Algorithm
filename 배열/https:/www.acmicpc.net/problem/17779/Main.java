import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, answer, MAX_HUMAN;
    static int[][] G;
    static int[] HUMANS;
    static boolean[][] BORDER;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    static void solution() {
        for(int d1 = 1; d1 < N; d1 += 1) {
            for(int d2 = 1; d2 < N; d2 += 1) {
                for(int i = 0; i < N; ++i) {
                    for (int j = 0; j < N; ++j) {
                        if(i+d1+d2 < N && j-d1 >= 0 && j+d2 < N)
                            calc(i, j, d1, d2);
                    }
                }
            }
        }
        System.out.println(answer);
    }

    private static void calc(int i, int j, int d1, int d2) {
        for (int d = 0; d <= d1; ++d)
            BORDER[i+d][j-d] = BORDER[i+d2+d][j+d2-d] = true;
        for (int d = 0; d <= d2; ++d)
            BORDER[i+d][j+d] = BORDER[i+d1+d][j-d1+d] = true;

        // one
        for (int x = 0; x < i+d1; ++x) {
            for (int y = 0; y <= j; ++y) {
                if (BORDER[x][y]) break;
                HUMANS[1] += G[x][y];
            }
        }

        // two
        for (int x = 0; x <= i+d2; ++x) {
            for (int y = N-1; y > j; --y) {
                if (BORDER[x][y]) break;
                HUMANS[2] += G[x][y];
            }
        }

        // three
        for (int x = i+d1; x < N; ++x) {
            for (int y = 0; y < j-d1+d2; ++y) {
                if (BORDER[x][y]) break;
                HUMANS[3] += G[x][y];
            }
        }

        // four
        for (int x = i+d2+1; x < N; ++x) {
            for (int y = N-1; y >= j-d1+d2; --y) {
                if (BORDER[x][y]) break;
                HUMANS[4] += G[x][y];
            }
        }

        // five
        HUMANS[5] = MAX_HUMAN-HUMANS[1]-HUMANS[2]-HUMANS[3]-HUMANS[4];

        int min = MAX_HUMAN, max = 0;
        for(int k = 1; k <= 5; ++k) {
            min = Math.min(min, HUMANS[k]); max = Math.max(max, HUMANS[k]);
        }
        answer = Math.min(answer, max-min);
        Arrays.fill(HUMANS, 0);
        for(int k = 0; k < N; ++k) Arrays.fill(BORDER[k], false);
    }

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer row;
        N = Integer.parseInt(br.readLine());
        G = new int[N][N]; HUMANS = new int[6]; BORDER = new boolean[N][N];

        for(int i = 0; i < N; ++i) {
            row = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; ++j)
                MAX_HUMAN += G[i][j] = Integer.parseInt(row.nextToken());
        }
        answer = MAX_HUMAN;
        br.close();
    }
}
