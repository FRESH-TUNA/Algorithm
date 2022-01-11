import java.util.stream.IntStream;

class Solution {
    public int solution(int left, int right) {
        return IntStream.range(left, right + 1).map(
            x -> (this.count(x) & 1) == 1 ? x*(-1): x).sum();
    }
    
    private int count(int num) {
        int ans = 0;
        for(int i = 1; i <= num / 2; ++i) if(num % i == 0) ans += 1;
        return ans + 1;
    }
}
