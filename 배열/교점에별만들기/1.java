import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        final int LINE_NUM = line.length;
        
        ArrayList<long[]> intersects 
            = new ArrayList(LINE_NUM * (LINE_NUM - 1));
        
        for(int i = 0; i < line.length; ++i)
            for(int j = i; j < line.length; ++j)
                pushIntersect(line, intersects, i, j);
    
        //adjustments testcode
        //for(long a: adjustments) System.out.println(a);
        long[] border = adjust_and_get_border(
            intersects, adjust_values(intersects));
        
        //intersect testcode
        // for(long[] a : intersects) {
        //     for(int i = 0; i < a.length; ++i)
        //         System.out.print(a[i] + " ");
        //     System.out.println();
        // }
        return get_answer(intersects, border);
    }
    
    private void pushIntersect(
        int[][] line, List<long[]> intersects, int i, int j
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
        
        intersects.add(
            new long[] {(long) intersect[0], (long) intersect[1]});
    }
    
    private boolean is_integer(double[] intersect) {
        for(int i = 0; i < intersect.length; ++i)
            if(intersect[i] - (long)intersect[i] != 0) return false;
        return true;
    }
    
    private long[] adjust_values(ArrayList<long[]> intersects) {
        long x_min = 0, y_max = 0;
        for(long[] intersect : intersects) {
            x_min = Math.min(x_min, intersect[0]);
            y_max = Math.max(y_max, intersect[1]);
        }
        return new long[] {x_min, y_max};
    }
    
    private long[] adjust_and_get_border(
        ArrayList<long[]> intersects, long[] values
    ) {
        long[] border = new long[2];
        
        for(long[] intersect : intersects) {
            long intersect_0 = Math.abs(intersect[1] - values[1]);
            long intersect_1 = intersect[0] - values[0];
            intersect[0] = intersect_0; intersect[1] = intersect_1;
            border[0] = Math.max(border[0], intersect[0]);
            border[1] = Math.max(border[1], intersect[1]);
        }
        
        return border;
    }
    
    private String[] get_answer(
        ArrayList<long[]> intersects, long[] border
    ) {
        int MAX_X = (int) border[0] + 1, MAX_Y = (int) border[1] + 1;
        String[] answer = new String[MAX_X];
        char[][] _answer = new char[MAX_X][MAX_Y];
        
        for(int i = 0; i < MAX_X; ++i) {
            _answer[i] = new char[MAX_Y];
            Arrays.fill(_answer[i], '.');
        }
        
        for(long[] i : intersects)
            _answer[(int)i[0]][(int)i[1]] = '*';
        
        for(int i = 0; i < MAX_X; ++i)
            answer[i] = String.valueOf(_answer[i]);
        
        return answer;
    }
}
