import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static char[] S;
    private static char[] BOMB;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        StringBuilder res = new StringBuilder();
        for(char c : S) {
            res.append(c);
            if(res.length() >= BOMB.length && can_pung(res))
                pung(res);
        }
        System.out.println( res.length()==0 ? "FRULA" : res );
    }

    private static boolean can_pung(StringBuilder res) {
        for (int i = 0; i < BOMB.length; ++i)
            if(BOMB[i] != res.charAt(res.length() - BOMB.length + i))
                return false;
        return true;
    }

    private static void pung(StringBuilder res) {
        res.delete(res.length()-BOMB.length, res.length());
    }


    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine().toCharArray(); BOMB = br.readLine().toCharArray();
        br.close();
    }
}
