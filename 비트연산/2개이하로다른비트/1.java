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


//A = 10111111
//B = A+1 = 11000000

//A xor B
//01111111

//(A xor B) >>> 2
//00011111 만큼 채워준다.
