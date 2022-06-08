import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_N = 100;
    private static final LinkedList<String>[] DATAS = new LinkedList[MAX_N];
    private static final char[][] COMMANDS = new char[MAX_N][];
    private static final int[] WAYS = new int[MAX_N];

    private static int N;

    public static void main(String[] args) throws IOException {
        input_cases();
        solution();
    }

    private static void solution() {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; ++i) {
            if (processing(i)) add_result(sb, i);
            else sb.append("error\n");
        }
        System.out.print(sb);
    }

    private static boolean processing(int i) {
        for (char c : COMMANDS[i]) {
            if(c == 'R') WAYS[i] = (WAYS[i] == 1) ? 0 : 1;
            else if(c != 'D' || DATAS[i].isEmpty()) return false;
            else if(WAYS[i] == 0) DATAS[i].removeFirst();
            else DATAS[i].removeLast();
        }
        return true;
    }

    private static void add_result(StringBuilder sb, int i) {
        if(DATAS[i].isEmpty()) { sb.append("[]\n"); return; }

        sb.append('[');
        Iterator<String> it = (WAYS[i] == 0 ?
                DATAS[i].iterator() : DATAS[i].descendingIterator());
        while (it.hasNext()) { sb.append(it.next()); sb.append(','); }
        sb.deleteCharAt(sb.length()-1);
        sb.append("]\n");
    }

    private static void input_cases() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; ++i) input_case(br, i);
        br.close();
    }

    private static void input_case(BufferedReader br, int i) throws IOException {
        COMMANDS[i] = br.readLine().toCharArray();
        int command_n = Integer.parseInt(br.readLine());
        String data = br.readLine();
        StringTokenizer data_tokens = new StringTokenizer(
                data.substring(1, data.length()-1), ",");

        DATAS[i] = new LinkedList<>();
        while (command_n > 0) {
            DATAS[i].add(data_tokens.nextToken());
            command_n--;
        }
    }
}
