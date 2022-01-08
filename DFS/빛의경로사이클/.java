import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;

class Solution {
    private HashMap<String, Boolean>[][] traced;
    private LinkedList<Integer> answers;
    
    public int[] solution(String[] grid) {
        this.init(grid.length, grid[0].length());
        String[] ways = new String[] {"U", "R", "D", "L"};
        
        for(int i = 0; i < grid.length; ++i) {
            for(int j = 0; j < grid[i].length(); ++j) {
                HashMap<String, Boolean> node = traced[i][j];
                for(String way : ways) {
                    if(!node.get(way)) {
                        this.answers.add(dfs(i, j, i, jway)); 
                    }
                }
            }
        }

        return new int[] {answers.size()};
    }
    
    private void init(int rows, int cols) {
        this.traced = new HashMap[rows][cols];
        this.answers = new LinkedList();
        
        HashMap<String, Boolean> based_map = new HashMap() {{
            put("U", false); put("R", false);
            put("D", false); put("L", false); }};
        
        for(HashMap<String, Boolean>[] row : this.traced) {
            for(int i = 0; i < cols; ++i) {
                row[i] = new HashMap();
                for (Map.Entry<String, Boolean> e : based_map.entrySet())
                    row[i].put(e.getKey(), e.getValue());
            }
        }
    }
    
    private static int dfs(int i, int j, int r_i, int r_j, String way)     {

    }
}
