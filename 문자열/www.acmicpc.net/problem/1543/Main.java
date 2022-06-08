import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;

public class Main {
    private static char[] S;
    private static char[] BOMB;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        LinkedList<Character> s = new LinkedList<>();
        int res = 0;
        for(char c : S) {
            s.add(c);
            if(s.size() >= BOMB.length && can_pung(s)) {
                s.clear();
                res += 1;
            }
        }
        System.out.println(res);
    }

    private static boolean can_pung(LinkedList s) {
        Iterator<Character> it = s.descendingIterator();
        for (int i = BOMB.length-1; i >= 0; --i)
            if(BOMB[i] != it.next())
                return false;
        return true;
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine().toCharArray(); BOMB = br.readLine().toCharArray();
        br.close();
    }
}
