import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    private HashMap<String, Integer> db;
    
    public int[] solution(String msg) {
        ArrayList<Integer> answers = new ArrayList(msg.length());
        int start = 0, end = 1, msg_len = msg.length();
        init_db();
        
        while(start < msg_len) {
            if(end > msg_len) {
                answers.add(this.db.get(msg.substring(start, end - 1)));
                break;
            }
            if(this.db.get(msg.substring(start, end)) == null) {
                answers.add(this.db.get(msg.substring(start, end - 1)));
                this.db.put(msg.substring(start, end), this.db.size() + 1);
                start = end - 1;
                end = start + 1;
            }
            else end += 1;
        }
        return answers.stream().mapToInt(i->i).toArray();
    }
    
    public void init_db() {
        String s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        this.db = new HashMap();
        for(int i = 0; i < s.length(); ++i)
            this.db.put(s.charAt(i) + "", i + 1);
    }
}
