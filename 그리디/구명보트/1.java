import java.util.Arrays;
import java.util.LinkedList;
import java.util.stream.Collectors;

class Solution {
    private LinkedList<Integer> list = null;
    private int answer = 0;
    
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        list = Arrays.stream(people).boxed().collect(
            Collectors.toCollection(LinkedList::new));

        while(list.size() > 0) {
            if(list.getFirst() * 2 > limit) return list.size() + answer;
    
            int weight = list.getFirst() + list.getLast();
            if(list.size() >= 2 && weight <= limit) list.removeFirst();
            list.removeLast();
            answer += 1;
        }

        return answer;
    }
}
