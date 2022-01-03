import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        final int LINE_NUM = line.length;
        Set<String> intersects = new HashSet<String>();
        
        for(int i = 0; i < line.length; ++i)
            for(int j = i; j < line.length; ++j)
                pushIntersect(line, intersects, i, j);
        
        return get_answer(intersects, min_max(intersects));
    }
    
    private void pushIntersect(
        int[][] line, Set<String> intersects, int i, int j
    ) {
        int[] case_i = line[i], case_j = line[j]; 
        long r = case_i[0] * case_j[1] - case_j[0] * case_i[1];
        
        if(r == 0) return;
        
        long[][] revert = {
            {case_j[1], (-1) * case_i[1]}, 
            {(-1) * case_j[0], case_i[0]}};
        long[] inter = new long[] { 
            (revert[0][0] * case_i[2] * (-1)
                    + revert[0][1] * case_j[2] * (-1)),
            (revert[1][0] * case_i[2] * (-1) 
                    + revert[1][1] * case_j[2] * (-1))};
        
        if(inter[0] % r == 0 && inter[1] % r == 0)
            intersects.add(inter[0] / r + "," + inter[1] / r);
    }
    
    private long[] min_max(Set<String> intersects) {
        long x_min = Long.MAX_VALUE, y_min = Long.MAX_VALUE;
        long x_max = Long.MIN_VALUE, y_max = Long.MIN_VALUE;
        for(String intersect : intersects) {
            String[] xy = intersect.split(",");
            long x = Long.parseLong(xy[0]);
            long y = Long.parseLong(xy[1]);
            
            x_max = Math.max(x_max, x);
            x_min = Math.min(x_min, x);
            y_max = Math.max(y_max, y);
            y_min = Math.min(y_min, y);
        }
        return new long[] {x_min, x_max, y_min, y_max};
    }
    
    private String[] get_answer(
        Set<String> intersects, long[] min_max
    ) {
        long MIN_X = min_max[0], MAX_X = min_max[1];
        long MIN_Y = min_max[2], MAX_Y = min_max[3];
        String[] answer = new String[(int) Math.abs(MAX_Y - MIN_Y) + 1];
        
        for(long i = 0, _i = MAX_Y; _i >= MIN_Y; ++i, --_i) {
            StringBuilder sb = new StringBuilder();
            for(long _j = MIN_X; _j <= MAX_X; ++_j) 
                sb.append(intersects.contains(_j + "," + _i) ? "*" : ".");
            answer[(int) i] = sb.toString();
        }

        return answer;
    }
}
