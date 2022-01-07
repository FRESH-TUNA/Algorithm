class Solution
{
    public int solution(int [][]board)
    {
        int ROWS = board.length, COLS = board[0].length;
        int[][] my_b = new int[ROWS + 1][COLS + 1];
        int answer = 0;
        
        for(int i = 0; i < ROWS; ++i)
            for(int j = 0; j < COLS; ++j)
                my_b[i+1][j+1] = board[i][j];
        
        for(int i = 1; i < ROWS + 1; ++i) {
            for(int j = 1; j < COLS + 1; ++j) {
                if(my_b[i][j] != 0) {
                    my_b[i][j] = Math.min(Math.min(my_b[i-1][j], my_b[i][j-1]), my_b[i-1][j-1]) + 1;
                    answer = Math.max(answer, my_b[i][j]);
                }
            }
        }
        return answer * answer;
    }
}
