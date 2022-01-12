import java.util.LinkedList;
import java.util.HashMap;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.regex.MatchResult;

class Solution {
    public int solution(String d) {
        String[] tokens = Pattern.compile("[SDT*#]|\\d+")
            .matcher(d).results()
            .map(MatchResult::group)
            .toArray(String[]::new);
        LinkedList<Integer> answers = new LinkedList(Arrays.asList(0));
        HashMap<String, Integer> bonus = new HashMap() {{
           put("S", 1); put("D", 2); put("T", 3);
           put("*", 2); put("#", -1); }};
        
        for(int i = 0; i < tokens.length;) {
            int score = Integer.parseInt(tokens[i]);
            int pow = bonus.get(tokens[i+1]);
            int multiplier = 1;
                
            if(i+2 < tokens.length && bonus.containsKey(tokens[i+2])) {
                multiplier = bonus.get(tokens[i+2]);
                if(multiplier == 2) 
                    answers.add(answers.removeLast() * multiplier);
                i += 1;
            }
            answers.add((int) Math.pow(score, pow) * multiplier);
            i += 2;
        }
                                                     
        return answers.stream().mapToInt(x -> x).sum();
    }
}
