import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        final int LINE_NUM = line.length;
        ArrayList<long[]> intersects 
            = new ArrayList(LINE_NUM * (LINE_NUM - 1));
        
        for(int i = 0; i < line.length; ++i)
            for(int j = i; j < line.length; ++j)
                pushIntersect(line, intersects, i, j);

        // intersect testcode
        for(long[] a : intersects) {
            for(int i = 0; i < a.length; ++i)
                System.out.print(a[i] + " ");
            System.out.println();
        }

        return new String[2];
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
}
