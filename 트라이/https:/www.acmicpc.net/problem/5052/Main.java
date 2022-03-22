import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    private static int CASES_N;
    private static int[] CASE_N;
    private static char[][][] CASES;
    private static Map<Character, Map>[] TRIES;

    public static void main(String[] args) throws IOException {
        inputs();
        tries();
        solutions();
    }

    private static void solutions() {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<CASES_N; ++i) sb.append(solution(i) ? "YES\n" : "NO\n");
        System.out.print(sb);
    }

    private static boolean solution(int i) {
        for (int j = 0; j < CASE_N[i]; j++) {
            Map<Character, Map> pointer = TRIES[i];
            for(char c : CASES[i][j]) pointer = pointer.get(c);
            if(!pointer.isEmpty()) return false;
        }
        return true;
    }

    private static void tries() {
        TRIES = new Map[CASES_N];
        for (int i = 0; i < CASES_N; ++i) trie(i);
    }

    private static void trie(int i) {
        TRIES[i] = new HashMap<>();
        for (int j = 0; j < CASE_N[i]; j++) {
            Map<Character, Map> pointer = TRIES[i];
            for(char c : CASES[i][j]) {
                if(!pointer.containsKey(c))
                    pointer.put(c, new HashMap<Character, Map>());
                pointer = pointer.get(c);
            }
        }
    }

    private static void inputs() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        CASES_N = Integer.parseInt(br.readLine());
        CASE_N = new int[CASES_N];
        CASES = new char[CASES_N][][];
        for (int t = 0; t < CASES_N; ++t) input(br, t);
        br.close();
    }

    private static void input(BufferedReader br, int t) throws IOException {
        CASE_N[t] = Integer.parseInt(br.readLine());
        CASES[t] = new char[CASE_N[t]][];
        for (int j = 0; j < CASE_N[t]; ++j)
            CASES[t][j] = br.readLine().toCharArray();
    }
}
