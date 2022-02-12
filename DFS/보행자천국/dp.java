import java.util.LinkedList;

class Solution {
    final int MOD = 20170805;
    int[][][] answer = new int[300][300][2];

    public int solution(int m, int n, int[][] cityMap) {
        for(int i = 0; i < m; i++) {
            if(cityMap[i][0] == 1) break;
            answer[i][0][0] = 1;
        }
        
        for(int j = 0; j < n; j++) {
            if(cityMap[0][j] == 1) break;
            answer[0][j][1] = 1;
        }
        
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                if(cityMap[i][j] == 1) continue;
                
                answer[i][j][0] += answer[i-1][j][0];
                answer[i][j][1] += answer[i][j-1][1];
                
                if(cityMap[i-1][j] != 2)
                    answer[i][j][0] += answer[i-1][j][1];
                if(cityMap[i][j-1] != 2)
                    answer[i][j][1] += answer[i][j-1][0];
                
                answer[i][j][0] = answer[i][j][0] % MOD;
                answer[i][j][1] = answer[i][j][1] % MOD;
            }
        }

        return (answer[m-1][n-1][0] + answer[m-1][n-1][1]) % MOD;
    }
}
