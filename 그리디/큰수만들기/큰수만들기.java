import java.util.*;
import java.util.stream.Collectors;

class Solution {
  public String solution(String number, int k) {
      Stack<Integer> stack = new Stack();
      List<Integer> numList = Arrays.stream(number.split(""))
          .map(Integer::valueOf).collect(Collectors.toList());

      for(Integer num : numList) { 
          if(!stack.empty() && stack.peek() < num && k > 0) k = eliminate(stack, num, k);
          stack.push(num);
      }
      
      return answer(stack, k);
  }
    
  private int eliminate(
      Stack<Integer> stack, Integer num, int k
  ) {
    while(!stack.empty() && k > 0 && stack.peek() < num) {
        stack.pop();
        k -= 1;
    }
    return k;
  }
    
   private String answer(Stack<Integer> stack, int k) {
       String answer = "";
       while(k-- > 0) stack.pop();
       for(Integer num : stack) answer += num;
       return answer;
   }
}
