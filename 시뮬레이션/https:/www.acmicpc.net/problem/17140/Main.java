import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int MAX_N = 100;
    private static final int[][] STATUS = new int[MAX_N+1][MAX_N+1];

    private static int R, C, T;
    private static int MAX_R = 3, MAX_C = 3;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        int RES = -1;
        for (int i = 0; i <= MAX_N; ++i) {
            if(STATUS[R][C] == T) { RES = i; break; }
            if(MAX_R >= MAX_C) rcalc(); else ccalc();
        }
        System.out.println(RES);
    }

    private static void rcalc() {
        short NEW_MAX_C = 0;

        for(short i = 1; i <= MAX_R; ++i) {
            Map<Integer, Integer> map = new TreeMap<>();

            for (short j = 1; j <= MAX_C; ++j) {
                if(STATUS[i][j] == 0) continue;
                map.put(STATUS[i][j], (map.getOrDefault(STATUS[i][j], 0) + 1));
                STATUS[i][j] = 0;
            }

            List<Map.Entry<Integer, Integer>> entries = new LinkedList(map.entrySet());
            Collections.sort(entries, Comparator.comparing(Map.Entry::getValue));

            short j = 1;
            for (Map.Entry<Integer, Integer> entry : entries) {
                STATUS[i][j++] = entry.getKey();
                STATUS[i][j++] = entry.getValue();
            }
            NEW_MAX_C = (short) Math.max(NEW_MAX_C, j-1);
        }
        MAX_C = (short) Math.max(NEW_MAX_C, MAX_C);
    }

    private static void ccalc() {
        short NEW_MAX_R = 0;

        for(short j = 1; j <= MAX_C; ++j) {
            Map<Integer, Integer> map = new TreeMap<>();

            for (int i = 1; i <= MAX_R; ++i) {
                if (STATUS[i][j] == 0) continue;
                map.put(STATUS[i][j], (map.getOrDefault(STATUS[i][j], 0) + 1));
                STATUS[i][j] = 0;
            }
            List<Map.Entry<Integer, Integer>> entries = new LinkedList(map.entrySet());
            Collections.sort(entries, Comparator.comparing(Map.Entry::getValue));

            short i = 1;
            for (Map.Entry<Integer, Integer> entry : entries) {
                STATUS[i++][j] = entry.getKey();
                STATUS[i++][j] = entry.getValue();
            }
            NEW_MAX_R = (short) Math.max(NEW_MAX_R, i-1);
        }
        MAX_R = (short) Math.max(NEW_MAX_R, MAX_R);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Short.parseShort(st.nextToken());
        C = Short.parseShort(st.nextToken());
        T = Short.parseShort(st.nextToken());
        for(int i = 1; i <= MAX_R; ++i) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= MAX_C; ++j)
                STATUS[i][j] = Short.parseShort(st.nextToken());
        }
        br.close();
    }
}
