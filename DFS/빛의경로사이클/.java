import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    private boolean traced[][][];
    private int[][][] nexts;
    private HashMap<Character, Integer> node_types;
    private int ROWS; private int COLS;
    
    public int[] solution(String[] grid) {
        ArrayList<Integer> answers = new ArrayList();
        int ROWS = grid.length, COLS = grid[0].length(), DS = 4;
        
        this.init(ROWS, COLS);
        for(int i = 0; i < ROWS; ++i)
            for(int j = 0; j < COLS; ++j)
                for(int k = 0; k < DS; ++k)
                    if(!this.traced[i][j][k]) 
                        answers.add(dfs(grid, i, j, k, i, j, k));
        return answers.stream().mapToInt(i->i).sorted().toArray();
    }
    
    // S, L, R = 0, 1, 2
    // 상: 0, 우: 1, 하: 2, 좌: 3
    // 다음 노드 결정 / 다음 방향 결정
    private void init(int rows, int cols) {
        this.traced = new boolean[rows][cols][4];
        this.nexts = new int[][][] {
            { {1, 0, 0}, {0, -1, 1}, {-1, 0, 2}, {0, 1, 3} },
            { {0, 1, 3}, {1, 0, 0}, {0, -1, 1}, {-1, 0, 2} },
            { {0, -1, 1}, {-1, 0, 2}, {0, 1, 3}, {1, 0, 0} } };
        this.node_types = new HashMap() {{
            put('S', 0); put('L', 1); put('R', 2); }};
        this.ROWS = rows; this.COLS = cols;
    }
    
    private int dfs(
        String[] grid, int r_r, int r_c, int r_d, int r, int c, int d
    ) {
        int answer = 0;
        while(!(r == r_r && c == r_c && d == r_d && this.traced[r][c][d])) {
            this.traced[r][c][d] = true;

            int node_type = this.node_types.get(grid[r].charAt(c));
            int[] next = this.nexts[node_type][d];
            r = r + next[0]; c = c + next[1]; d = next[2];

            r = (r == -1) ? this.ROWS-1 : ((r == this.ROWS ? 0 : r));
            c = (c == -1) ? this.COLS-1 : ((c == this.COLS ? 0 : c));
            answer += 1;
        }
        return answer;
    }
}
