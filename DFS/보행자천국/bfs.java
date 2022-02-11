import java.util.LinkedList;

class Solution {
    final int MOD = 20170805;
    LinkedList<int[]> stack = new LinkedList();
    int answer = 0;

    public int solution(int m, int n, int[][] cityMap) {
        bfs(m, n, cityMap);
        return answer;
    }
    
    private void bfs(int m, int n, int[][] cityMap) {
        stack.offerFirst(new int[] {0, 0, -1});
        
        while(!stack.isEmpty()) {
            int[] node = stack.pop();
            int r=node[0], c=node[1], d=node[2];
            int[][] new_nodes = new int[][] {{r+1,c,0}, {r,c+1,1}};
            
            for(int[] new_node : new_nodes) {  
                int nr=new_node[0], nc=new_node[1], nd=new_node[2];

                if(nr == -1 || nr == m || nc == -1 || nc == n) continue;
                if(cityMap[nr][nc] == 1) continue;
                if(cityMap[r][c] == 2 && d != nd && !(r == 0 && c == 0))
                    continue;
                if(nr == m-1 && nc == n-1) answer = (answer + 1) % MOD;
                
                stack.push(new int[] {nr, nc, nd});
            }
        }
    }
}