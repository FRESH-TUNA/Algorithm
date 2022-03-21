import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main2 {
    private static final Set<Character> left = new HashSet<>() {{add('['); add('(');}};
    private static final Set<Character> right = new HashSet<>() {{add(']'); add(')');}};
    private static final HashMap<Character, Character> SWITCH = new HashMap<>() {{
        put(']','['); put(')','(');
    }};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            char[] line = br.readLine().toCharArray();
            if(line.length == 1 && line[0] == '.') break;
            sb.append(solution(line) ? "yes\n" : "no\n");
        }
        System.out.print(sb);
    }

    private static boolean solution(char[] line) {
        Stack<Character> stack = new Stack<>();

        for(char c : line) {
            if (left.contains(c)) stack.add(c);
            else if(right.contains(c)) {
                if(stack.isEmpty() || !SWITCH.get(c).equals(stack.peek()))
                    return false;
                else stack.pop();
            }
        }

        return stack.isEmpty();
    }
}
