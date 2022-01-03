import java.util.LinkedList;
import java.util.HashSet;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        LinkedList<String> recent = new LinkedList();
        HashSet<String> db = new HashSet();
        int answer = 0;
        
        for(String city : cities) {
            city = city.toUpperCase();
            
            if(db.contains(city)) {
                answer += 1;
                recent.remove(city);
                recent.offerFirst(city);
            }
            else {
             	answer += 5;
                db.add(city);
                recent.offerFirst(city);
                if(db.size() > cacheSize)
                    db.remove(recent.removeLast());
            }
        }
        return answer;
    }
}
