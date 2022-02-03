import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

class Solution {
    private final int MAX_WIDTH = 100;
    private Map<Character, List<int[]>> db = new HashMap<>();
    private List<Character> keys;
    private char[][] graph = new char[MAX_WIDTH][MAX_WIDTH];
    private StringBuilder ans = new StringBuilder();
    
    public String solution(int m, int n, String[] board) {
        init(m, n, board);
        return pung() ? ans.toString() : "IMPOSSIBLE";
    }
    
    private boolean pung() {
        while(!keys.isEmpty()) {
            Iterator<Character> it = keys.iterator();
            Character punged_key = null;

            while(it.hasNext()) {
                char key = it.next();
                if(check(key)) {
                    punged_key = key;
                    break;
                }
            }
            
            if(punged_key == null) return false;
            ans.append(punged_key);
            keys.remove(punged_key);
            pung(punged_key);
        }
        return true;
    }
    
    private void init(int m, int n, String[] board) {
        Set<Character> nodes = new HashSet();
        
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                char key = board[i].charAt(j);
                graph[i][j] = key;
                
                if(key == '*' || key == '.') continue;
                
                if(!db.containsKey(key))
                    db.put(key, new ArrayList(2));
                db.get(key).add(new int[] {i, j});
                nodes.add(key);
            }
        }
        
        keys = new ArrayList(nodes);
        Collections.sort(keys);
    }
    
    private boolean check(char key) {
        List<int[]> idxs = db.get(key);
        int[] idx_s = idxs.get(0), idx_e = idxs.get(1);
        int s_i = idx_s[0], s_j = idx_s[1];
        int e_i = idx_e[0], e_j = idx_e[1];
        
        return test(s_i, s_j, e_i, e_j);
    }
    
    private boolean test(int s_i, int s_j, int e_i, int e_j) {    
        if((e_i-s_i + Math.abs(e_j-s_j)) == 1) return true;
        
        boolean row_test = (s_i == e_i ? false : 
                            test(s_i+1, s_j, e_i, e_j, true));
        boolean col_test = (s_j == e_j ? false : 
                            test(s_i, s_j < e_j ? 
                                s_j+1:s_j-1, e_i, e_j, false));
        return row_test || col_test;
    }
    
    private boolean test(int i, int j, 
                         int e_i, int e_j, boolean is_row) {
        if(graph[i][j] == graph[e_i][e_j]) return true;
        if(graph[i][j] != '.') return false;
        
        if(is_row) {
            return i != e_i ? test(i+1, j, e_i, e_j, true) :
                   test(i, j<e_j ? j+1:j-1, e_i, e_j, false);
        }
        else {
            return j != e_j ? 
                   test(i, j<e_j ? j+1:j-1, e_i, e_j, false) :
                   test(i+1, j, e_i, e_j, true);
        }
    }
    
    private void pung(char key) {
        List<int[]> idxs = db.get(key);
        int[] idx_s = idxs.get(0), idx_e = idxs.get(1);
        int s_i = idx_s[0], s_j = idx_s[1];
        int e_i = idx_e[0], e_j = idx_e[1];
        
        graph[s_i][s_j] = '.';
        graph[e_i][e_j] = '.';
    }
}