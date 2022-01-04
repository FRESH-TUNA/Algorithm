import java.util.HashSet;
import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int solution(String dirs) {
        HashSet<String> traced = new HashSet(); 
        HashMap<Character, int[]> directs = new HashMap() {{ 
            put('U', new int[]{0, 1}); put('D', new int[]{0, -1});
            put('R', new int[]{1, 0}); put('L', new int[]{-1, 0});
        }};
        int x = 0, y = 0;

        for(int i = 0; i < dirs.length(); ++i) {
            int[] d = directs.get(dirs.charAt(i));
            int n_x = x + d[0], n_y = y + d[1];
            
            if(!(n_x >= -5 && n_x <= 5 && n_y >= -5 && n_y <= 5))
                continue;
            
            String key = Arrays.toString(new int[]{x, y, n_x, n_y});
            String key_r = Arrays.toString(new int[]{n_x, n_y, x, y});
            if(!traced.contains(key)) {
                traced.add(key); traced.add(key_r);}
            x = n_x; y = n_y;
        }
        return traced.size() / 2;
    }
}
