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
        
        double[][] revert = {
            {(double) case_j[1] / r, (-1.0) * case_i[1] / r}, 
            {(-1.0) * case_j[0] / r, (double) case_i[0] / r}};
        double[] intersect = new double[] { 
            (revert[0][0] * case_i[2] * (-1)
                    + revert[0][1] * case_j[2] * (-1)),
            (revert[1][0] * case_i[2] * (-1) 
                    + revert[1][1] * case_j[2] * (-1))};
        if(!is_integer(intersect)) return;
        
        intersects.add((int) intersect[1] + "," + (int) intersect[0]);
    }
    
    private boolean is_integer(double[] intersect) {
        for(int i = 0; i < intersect.length; ++i)
            if(intersect[i] - (long)intersect[i] != 0) return false;
        return true;
    }
    
    private int[] min_max(Set<String> intersects) {
        int x_min = Integer.MAX_VALUE, y_min = Integer.MAX_VALUE;
        int x_max = Integer.MIN_VALUE, y_max = Integer.MIN_VALUE;
        for(String intersect : intersects) {
            String[] xy = intersect.split(",");
            int x = Integer.parseInt(xy[0]);
            int y = Integer.parseInt(xy[1]);
            
            x_max = Math.max(x_max, x);
            x_min = Math.min(x_min, x);
            y_max = Math.max(y_max, y);
            y_min = Math.min(y_min, y);
        }
        return new int[] {x_min, x_max, y_min, y_max};
    }
    
    private String[] get_answer(
        Set<String> intersects, int[] min_max
    ) {
        int MIN_X = min_max[0], MAX_X = min_max[1];
        int MIN_Y = min_max[2], MAX_Y = min_max[3];
        String[] answer = new String[Math.abs(MAX_Y - MIN_Y) + 1];
        
        for(int i = 0, _i = MAX_Y; _i >= MIN_Y; ++i, --_i) {
            StringBuilder sb = new StringBuilder();
            for(int _j = MIN_X; _j <= MAX_X; ++_j) 
                sb.append(intersects.contains(_i + "," + _j) ? "*" : ".");
            answer[i] = sb.toString();
        }

        return answer;
    }
}
