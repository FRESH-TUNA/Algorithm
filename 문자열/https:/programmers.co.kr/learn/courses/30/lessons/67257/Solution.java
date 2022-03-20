import java.util.LinkedList;
import java.util.stream.IntStream;

public class Solution {
    private final int CASES_N = 6, CASE_N = 3;
    private final String[][] CASES = new String[][] {
            {"+","-","*"}, {"+","*","-"}, {"*","+","-"},
            {"*","-","+"}, {"-","+","*"}, {"-","*","+"}
    };

    public long solution(String s) {
        return IntStream.range(0,CASES_N)
                .mapToLong(i -> calcs(s,i)).max().getAsLong();
    }

    private long calcs(String s, int ci) {
        LinkedList<String> stack = newStack(s);
        for (int i = 0; i < CASE_N; ++i) {
            LinkedList<String> next_stack = new LinkedList<>();

            while (!stack.isEmpty()) {
                String token = stack.removeFirst();
                if(token.equals(CASES[ci][i]))
                    next_stack.add(calc(next_stack.removeLast(), 
                            stack.removeFirst(), token));
                else next_stack.add(token);
            }
            stack = next_stack;
        }
        return Math.abs(Long.parseLong(stack.getFirst()));
    }

    private String calc(String a, String b, String op) {
        long na = Long.parseLong(a), nb = Long.parseLong(b);
        if(op.equals("+")) return String.valueOf(na+nb);
        else if(op.equals("-")) return String.valueOf(na-nb);
        else return String.valueOf(na*nb);
    }

    private LinkedList<String> newStack(String s) {
        String[] tokens = s.split("((?=\\+|-|\\*)|(?<=\\+|-|\\*))");
        LinkedList<String> stack = new LinkedList<>();
        for(String t : tokens) stack.add(t);
        return stack;
    }
}
