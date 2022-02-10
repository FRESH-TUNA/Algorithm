import java.util.LinkedList;
import java.util.List;

class Solution {
    public int solution(int m, int n, int[][] cityMap) {
        List<int[]> stack = new LinkedList();
        int[] node = new int[] {0, 0, -1};
        int MOD = 20170805;
        boolean[][] traced = new boolean[m][n]; 
        
        stack.append(node);
        traced[0][0] = true;
        
        while(!stack.isEmpty()) {
            while(true) {
                int[] case = stack.getLast();
                int r=case[0], c=case[1], d=case[2];
                int[][] new_cases = new int[4][3] {
                    {r+1,c, 0}, {r-1,c,1}, {r,c+1,2}, {r,c-1,3}};
                
                for(int[] case : new_cases) {
                    int nr=case[0], nc=case[1], nd=case[2];
                    
                    if(nr == -1 || nr == m) continue
                    if(nc == -1 || nc == n) continue
                    if(traced[nr][nc] || graph[nr][nc] == 1) continue
                    if(graph[nr][nc] == 2 and )
                    traced[nr][nc] = true;
                     
                }
            }
        }s