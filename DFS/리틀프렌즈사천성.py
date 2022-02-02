import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

class Solution {
    private final int MAX_WIDTH = 100;
    private Map<Character, List<int[]>> db = new HashMap<>();
    private char[][] graph = new char[MAX_WIDTH][MAX_WIDTH];
    private StringBuilder ans = new StringBuilder();
    
    public String solution(int m, int n, String[] board) {
        init(m, n, board);
        return pung() ? ans.toString() : "IMPOSSIBLE";
    }
    
    private boolean pung() {
        while(!db.isEmpty()) {
            Iterator<Character> it = db.keySet().iterator();
            List<Character> _ans = new ArrayList();
            
            while(it.hasNext()) {
                char key = it.next();
                if(check(key)) _ans.add(key); 
            }
            
            if(_ans.isEmpty()) return false;
            
            Collections.sort(_ans);
            it = _ans.iterator();
            while(it.hasNext()) {
                char key = it.next();
                ans.append(key);
                traced_apply(key); 
            }
        }
        return true;
    }
    
    private void init(int m, int n, String[] board) {
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                char key = board[i].charAt(j);
                graph[i][j] = key;
                
                if(key == '*' || key == '.') continue;
                
                if(!db.containsKey(key))
                    db.put(key, new ArrayList(2));
                db.get(key).add(new int[] {i, j});
            }
        }
    }
    
    private boolean check(char key) {
        List<int[]> idxs = db.get(key);
        int[] idx_s = idxs.get(0), idx_e = idxs.get(1);
        int s_i = idx_s[0], s_j = idx_s[1];
        int e_i = idx_e[0], e_j = idx_e[1];
        
        boolean up = up_test(s_i, s_j, e_i, e_j);
        boolean down = down_test(s_i, s_j, e_i, e_j);
        System.out.println(key);
        System.out.println(up);
        System.out.println(down);
        return up || down;
    }
    
    private void traced_apply(char key) {
        List<int[]> idxs = db.get(key);
        int[] idx_s = idxs.get(0), idx_e = idxs.get(1);
        int s_i = idx_s[0], s_j = idx_s[1];
        int e_i = idx_e[0], e_j = idx_e[1];
        
        graph[s_i][s_j] = '.';
        graph[e_i][e_j] = '.';
    }
    
    private boolean up_test(int s_i, int s_j, int e_i, int e_j) {
        int alias = s_j <= e_j ? 1 : -1;
        
        if(s_j != e_j) {
            s_j += 1;
            while (s_j != e_j) {
                if(graph[s_i][s_j] != '.' ) return false;
                s_j += alias;
            }
        }
        if(s_i != e_i) {
            s_i += 1;
            while (s_i != e_i) {
                if(graph[s_i][s_j] != '.') return false;
                s_i += 1;
            }
        }
        return true;
    }
    
    private boolean down_test(int s_i, int s_j, int e_i, int e_j) {   
        int alias = s_j <= e_j ? 1 : -1;
        
        if(s_i != e_i) {
            s_i += 1;
            while (s_i != e_i) {
                if(graph[s_i][s_j] != '.') return false;
                s_i += 1;
            }
        }
        if(s_j != e_j) {
            s_j += alias;
            while (s_j != e_j) {
                if(graph[s_i][s_j] != '.') return false;
                s_j += alias;
            }
        }
        return true;
    }
}