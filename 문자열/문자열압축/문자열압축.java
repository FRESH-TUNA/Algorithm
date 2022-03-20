import java.util.stream.IntStream;

class Solution {
    public int solution(String s) {
        return IntStream.range(1, s.length() / 2 + 1)
            .map(x -> compressed(s, x)).min().orElse(s.length());
    }

    private int compressed(String s, int w) {
        int i = w, sub_answer = 1;
        String compare_from = s.substring(0, w);
        StringBuilder result = new StringBuilder();

        while(i + w <= s.length()) {
            String compare_to = s.substring(i, i+w);
            if(compare_from.equals(compare_to)) sub_answer += 1;
            else {
                if(sub_answer != 1) result.append(sub_answer);
                result.append(compare_from);
                compare_from = compare_to;
                sub_answer = 1;
            }
            i += w;
        }

        if(sub_answer != 1) result.append(sub_answer);
        result.append(compare_from + s.substring(i, s.length()));
        return result.length();
    }
}
