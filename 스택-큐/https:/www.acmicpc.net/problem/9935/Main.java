import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    private static char[] S;
    private static char[] BOMB;

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        StringBuilder res = new StringBuilder();
        Stack<Integer> stack = new Stack<>();

        for(char c : S) {
            if(stack.isEmpty())
                stack.add((c == BOMB[0]) ? 0 : -1);
            else {
                int next_p = stack.peek()+1;
                if (c == BOMB[next_p]) stack.add(next_p);
                else stack.add((c == BOMB[0]) ? 0 : -1);
            }
            res.append(c);
            if(stack.peek().equals(BOMB.length-1)) pung(res, stack);
        }
        System.out.println( res.length()==0 ? "FRULA" : res );
    }

    private static void pung(StringBuilder res, Stack<Integer> stack) {
        res.delete(res.length()-BOMB.length, res.length());
        for(int i = 0; i < BOMB.length; ++i) stack.pop();
    }


    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine().toCharArray(); BOMB = br.readLine().toCharArray();
        br.close();
    }
}
