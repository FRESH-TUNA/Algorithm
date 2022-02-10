import java.util.LinkedList;
import java.util.List;

class Solution {
    public int solution(int m, int n, int[][] cityMap) {
        List<int[]> stack = new LinkedList();
        int[] node = new int[] {0, 0, -1};
        int MOD = 20170805;
        int answer
        boolean[][] traced = new boolean[m][n]; 
        
        stack.append(node);
        traced[0][0] = true;
        
        while(!stack.isEmpty()) {
            while(true) {
                int[] node = stack.getLast();
                int r=node[0], c=node[1], d=node[2];
                int[][] new_nodes = new int[4][3] {
                    {r+1,c, 0}, {r-1,c,1}, {r,c+1,2}, {r,c-1,3}};
                
                for(int[] new_node : new_nodes) {
                    int nr=new_node[0], nc=new_node[1], nd=new_node[2];
                    
                    if(nr == -1 || nr == m) continue;
                    if(nc == -1 || nc == n) continue;
                    if(traced[nr][nc] || graph[nr][nc] == 1) continue;
                    if(graph[nr][nc] == 2 && d != nd && r != 0 && c != 0)
                        continue;
                    traced[nr][nc] = true;
                    stack.push(new int{nr, nc, nd});
                    break;
                }
                if(case == stack.getLast()) break;
            }
        }
        
        int answer = 0;
        return answer;
    }
}