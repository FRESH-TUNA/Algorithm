import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

class Solution {
    private final int MAX_NODES = 200;
    private final int MAX_TRY = 100;
    private Set<Integer>[] graph = new Set[MAX_NODES+1];
    private int[][] ans = new int[MAX_TRY+1][MAX_NODES+1];
    
    public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
        init_graph(n, edge_list);
        adjustment(k, n, gps_log);
        return ans[k][n] >= k ? -1 : ans[k][n];
    }
    
    private void init_graph(int n, int[][] edge_list) {
        while(n > 0) {
            graph[n] = new HashSet();
            graph[n].add(n--);
        }
        
        for(int[] edge: edge_list) {
            int start = edge[0], end = edge[1];
            graph[start].add(end); graph[end].add(start);
        }
    }
    
    private void adjustment(int k, int n, int[] gps_log) {
        for(int j = 1; j <= n; ++j) ans[1][j] = k;
        ans[1][gps_log[0]] = 0;
        
        for(int i = 2; i <= k; ++i) {
            int[] prev = ans[i-1];
            for(int j = 1; j <= n; ++j) {
                int _ans = graph[j].stream()
                    .map(x -> prev[x])
                    .min(Integer::compare).get();
                ans[i][j] = gps_log[i-1] == j ? _ans : _ans+1;
            }
        }       
    }
}