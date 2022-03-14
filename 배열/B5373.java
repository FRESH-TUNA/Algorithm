import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import static java.util.Map.entry;

public class Main {
    private static final int[][][][] DB = {
            {{{5, 0, 0}, {5, 0, 1}, {5, 0, 2}}, {{1, 0, 0}, {1, 0, 1}, {1, 0, 2}},
                    {{4, 0, 0}, {4, 0, 1}, {4, 0, 2}}, {{3, 2, 2}, {3, 2, 1}, {3, 2, 0}}},
            {{{0, 2, 0}, {0, 2, 1}, {0, 2, 2}}, {{5, 0, 0}, {5, 1, 0}, {5, 2, 0}},
                    {{2, 0, 2}, {2, 0, 1}, {2, 0, 0}}, {{4, 2, 2}, {4, 1, 2}, {4, 0, 2}}},
            {{{1, 2, 0}, {1, 2, 1}, {1, 2, 2}}, {{5, 2, 0}, {5, 2, 1}, {5, 2, 2}},
                    {{3, 0, 2}, {3, 0, 1}, {3, 0, 0}}, {{4, 2, 0}, {4, 2, 1}, {4, 2, 2}}},
            {{{0, 0, 0}, {0, 0, 1}, {0, 0, 2}}, {{4, 2, 0}, {4, 1, 0}, {4, 0, 0}},
                    {{2, 2, 2}, {2, 2, 1}, {2, 2, 0}}, {{5, 0, 2}, {5, 1, 2}, {5, 2, 2}}},
            {{{0, 0, 0}, {0, 1, 0}, {0, 2, 0}}, {{1, 0, 0}, {1, 1, 0}, {1, 2, 0}},
                    {{2, 0, 0}, {2, 1, 0}, {2, 2, 0}}, {{3, 0, 0}, {3, 1, 0}, {3, 2, 0}}},
            {{{3, 0, 2}, {3, 1, 2}, {3, 2, 2}}, {{2, 0, 2}, {2, 1, 2}, {2, 2, 2}},
                    {{1, 0, 2}, {1, 1, 2}, {1, 2, 2}}, {{0, 0, 2}, {0, 1, 2}, {0, 2, 2}}}
    };
    private static final int LEFT = 0, RIGHT = 1;
    private static final int DB_IDX = 0, D = 1;
    private static final Map<Character, Integer> MYMAP = Map.ofEntries(
            entry('U', 1), entry('B', 0), entry('L', 4),
            entry('R', 5), entry('F', 2), entry('D', 3),
            entry('+', RIGHT), entry('-', LEFT)
    );
    private static char[][][] cube;

    /*
     * inputs
     */
    private static int COMMANDS_N;
    private static int[][][] COMMANDS;

    public static void main(String[] args) throws IOException {
        input();
        init_cube();
        turns();
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        COMMANDS_N = Integer.parseInt(br.readLine());
        COMMANDS = new int[COMMANDS_N][][];

        for (int i = 0; i < COMMANDS_N; ++i) {
            int TRUN_N = Integer.parseInt(br.readLine());
            COMMANDS[i] = new int[TRUN_N][2];

            String[] turns = br.readLine().split(" ");
            for (int j = 0; j < TRUN_N; ++j) {
                COMMANDS[i][j][DB_IDX] = MYMAP.get(turns[j].charAt(DB_IDX));
                COMMANDS[i][j][D] = MYMAP.get(turns[j].charAt(D));
            }
        }
    }

    private static void turns() {
        for(int i = 0; i < COMMANDS_N; ++i) {
            for (int j = 0; j < COMMANDS[i].length; ++j) {
                turn_edge(COMMANDS[i][j][DB_IDX], COMMANDS[i][j][D]);
                turn_self(COMMANDS[i][j][DB_IDX], COMMANDS[i][j][D]);
            }
            result();
            init_cube();
        }
    }

    private static void turn_edge(int db_idx, int d) {
        int [][][] db = DB[db_idx];
        int turn_count = (d == RIGHT) ? 1 : 3;

        while(turn_count-- > 0) {
            // init
            char[] shifted_values = {
                    cube[db[0][0][0]][db[0][0][1]][db[0][0][2]],
                    cube[db[0][1][0]][db[0][1][1]][db[0][1][2]],
                    cube[db[0][2][0]][db[0][2][1]][db[0][2][2]]
            };
            cube[db[0][0][0]][db[0][0][1]][db[0][0][2]] = cube[db[3][0][0]][db[3][0][1]][db[3][0][2]];
            cube[db[0][1][0]][db[0][1][1]][db[0][1][2]] = cube[db[3][1][0]][db[3][1][1]][db[3][1][2]];
            cube[db[0][2][0]][db[0][2][1]][db[0][2][2]] = cube[db[3][2][0]][db[3][2][1]][db[3][2][2]];

            for(int i = 1; i < 4; ++i) {
                char[] new_shifted_values = {
                        cube[db[i][0][0]][db[i][0][1]][db[i][0][2]],
                        cube[db[i][1][0]][db[i][1][1]][db[i][1][2]],
                        cube[db[i][2][0]][db[i][2][1]][db[i][2][2]]
                };

                cube[db[i][0][0]][db[i][0][1]][db[i][0][2]] = shifted_values[0];
                cube[db[i][1][0]][db[i][1][1]][db[i][1][2]] = shifted_values[1];
                cube[db[i][2][0]][db[i][2][1]][db[i][2][2]] = shifted_values[2];
                shifted_values = new_shifted_values;
            }
        }
    }

    private static void turn_self(int db_idx, int d) {
        int turn_count = (d == RIGHT) ? 1 : 3;

        while(turn_count-- > 0) {
            char[][] new_square = new char[3][];
            char[][] square = cube[db_idx];
            new_square[0] = new char[]{square[2][0], square[1][0], square[0][0]};
            new_square[1] = new char[]{square[2][1], square[1][1], square[0][1]};
            new_square[2] = new char[]{square[2][2], square[1][2], square[0][2]};
            cube[db_idx] = new_square;
        }
    }

    private static void result() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++)
                System.out.print(cube[1][i][j]);
            System.out.println();
        }
    }

    private static void init_cube() {
        cube = new char[][][]{
                {{'o', 'o', 'o'}, {'o', 'o', 'o'}, {'o', 'o', 'o'}},
                {{'w', 'w', 'w'}, {'w', 'w', 'w'}, {'w', 'w', 'w'}},
                {{'r', 'r', 'r'}, {'r', 'r', 'r'}, {'r', 'r', 'r'}},
                {{'y', 'y', 'y'}, {'y', 'y', 'y'}, {'y', 'y', 'y'}},
                {{'g', 'g', 'g'}, {'g', 'g', 'g'}, {'g', 'g', 'g'}},
                {{'b', 'b', 'b'}, {'b', 'b', 'b'}, {'b', 'b', 'b'}}
        };
    }
}
