import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    private static final int MAX_N = 50;
    private static final HashSet<String>[] DB = new HashSet[MAX_N];
    private static final int[] PHONES_N = new int[MAX_N];
    private static final String[][] PHONES = new String[MAX_N][10000];
    private static int N;

    public static void main(String[] args) throws IOException {
        inputs();
        DB_init();
        solutions();
    }

    private static void solutions() {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < N; ++i) res.append(solution(i) ? "YES\n" : "NO\n");
        System.out.print(res);
    }
    private static boolean solution(int i) {
        for (int j = 0; j < PHONES_N[i]; ++j)
            if(DB[i].contains(PHONES[i][j])) return false;
        return true;
    }

    private static void DB_init() { for (int i = 0; i < N; ++i) data_init(i); }
    private static void data_init(int i) {
        DB[i] = new HashSet<>();

        for (int j = 0; j < PHONES_N[i]; ++j) {
            char[] data = PHONES[i][j].toCharArray();
            StringBuilder sb = new StringBuilder();

            for(int k = 0; k < data.length-1; ++k) {
                sb.append(data[k]);
                DB[i].add(sb.toString());
            }
        }
    }

    private static void inputs() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; ++i) input(br, i);
        br.close();
    }
    private static void input(BufferedReader br, int i) throws IOException {
        PHONES_N[i] = Integer.parseInt(br.readLine());
        for (int j = 0; j < PHONES_N[i]; ++j) PHONES[i][j] = br.readLine();
    }
}
