import java.util.LinkedList;
import java.util.HashMap;
import java.util.regex.Pattern;
import java.util.regex.MatchResult;
import java.util.Arrays;

class Solution {
    public int solution(String dartResult) {
        LinkedList<Integer> answers = new LinkedList();
        HashMap<Character, Integer> ex = new HashMap() {{
           put('*', 2); put('#', -1); 
           put('S', 1); put('D', 2); put('T', 3);}};
        int answer = 0, i = 0;
        String[] scores = Pattern.compile("[SDT*#]|\\d+")
                          .matcher(dartResult).results()
                          .map(MatchResult::group)
                          .toArray(String[]::new);
        
        answers.add(0);
        while(i < scores.length) {
            int score = Integer.parseInt(scores[i]);
            int pow = ex.get(scores[i+1].charAt(0)), multiplier = 1;
            if(i+2 < scores.length && 
               ex.containsKey(scores[i+2].charAt(0))) {
                multiplier = ex.get(scores[i+2].charAt(0));
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
