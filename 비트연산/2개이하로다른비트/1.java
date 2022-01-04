import java.util.Arrays;

class Solution {
    public long[] solution(long[] numbers) {
        return Arrays.stream(numbers).map((long n) -> {
            long answer = n + 1;
            return answer += (answer ^ n) >>> 2;
        }).toArray();
    }
}

// import java.util.Arrays;

// class Solution {
//     public long[] solution(long[] numbers) {
//         return Arrays.stream(numbers).map(Solution::function).toArray();
//     }
    
//     private static long function(long number) {
//         long answer = number + 1;
//         return answer += (answer ^ number) >>> 2;
//     }
// }
