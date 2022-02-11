import java.util.LinkedList;

class Solution {
    public int solution(int m, int n, int[][] cityMap) {
        LinkedList<int[]> stack = new LinkedList();
        int MOD = 20170805;
        int answer = 0;
        boolean[][] traced = new boolean[m][n]; 
        
        stack.push(new int[] {0, 0, -1});
        traced[0][0] = true;
        
        while(!stack.isEmpty()) {
            while(true) {
                int[] node = stack.getLast();
                int r=node[0], c=node[1], d=node[2];
                int[][] new_nodes = new int[][] {
                    {r+1,c, 0}, {r-1,c,1}, {r,c+1,2}, {r,c-1,3}};
                
                for(int[] new_node : new_nodes) {
                    int nr=new_node[0], nc=new_node[1], nd=new_node[2];
                    
                    if(nr == -1 || nr == m) continue;
                    if(nc == -1 || nc == n) continue;
                    if(traced[nr][nc] || cityMap[nr][nc] == 1) continue;
                    if(cityMap[nr][nc] == 2 && d != nd && r != 0 && c != 0)
                        continue;
                    traced[nr][nc] = true;
                    if(nr == m-1 && nc == n-1) answer += 1;
                    stack.push(new int[]{nr, nc, nd});
                    break;
                }
                if(node == stack.getLast()) break;
            }
            
            int[] popped = stack.pop();
            int pr=popped[0], pc=popped[1];
            traced[pr][pc] = false;
        }

        return answer;
    }
}