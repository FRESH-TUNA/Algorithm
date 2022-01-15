
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
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
