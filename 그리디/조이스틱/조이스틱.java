import java.lang.Math;

class Solution {
    public int solution(String name) {
        int NAME_lEN = name.length();
        int left_shifted = NAME_lEN - 1;
        int height_shifted = 0;
        
        for(int i = 0; i < NAME_lEN; ++i) {
            // height shift
            height_shifted += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);
            
            // left shift
            int lastA = i + 1;
            while(lastA < NAME_lEN) {
                if(name.charAt(lastA) != 'A') break;
                lastA += 1;
            }
            
            left_shifted = Math.min(left_shifted, i * 2 + NAME_lEN - lastA);
        }

        return left_shifted + height_shifted;
    }
}
