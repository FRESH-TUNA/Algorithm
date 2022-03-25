import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    private static final int MAX_NUM = 8;
    private static final List<Character>[] DB = new List[MAX_NUM+1];
    private static final Map<Character, Integer> MAP = new HashMap<>();

    private static int N;
    private static char[][] WORDS_RAW;

    public static void main(String[] args) throws IOException {
        input();
        init();
        solution();
    }

    private static void solution() {
        int next_put = 9, res = 0;
        List<Integer> result = MAP.values().stream().collect(Collectors.toList());
        result.sort(Comparator.reverseOrder());
        for(int r : result) res += (next_put--) * r;
        System.out.println(res);
    }

    private static void init() {
        for (int i = 1; i <= MAX_NUM; ++i) DB[i] = new LinkedList<>();
        for (int i = 0; i < N; ++i) {
            int MAX_LEN = WORDS_RAW[i].length;

            for(int j = 0; j < MAX_LEN; j++) {
                char key = WORDS_RAW[i][j];
                MAP.put(key, (int) (MAP.getOrDefault(key,0)
                        + Math.pow(10, MAX_LEN-j-1)));
            }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        WORDS_RAW = new char[N][];
        for (int i = 0; i < N; ++i) WORDS_RAW[i] = br.readLine().toCharArray();
        br.close();
    }
}
