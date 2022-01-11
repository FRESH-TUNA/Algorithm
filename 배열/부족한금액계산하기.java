import java.util.stream.LongStream;

class Solution {
    public long solution(int price, int money, int count) {
        long result = LongStream.range(1, count+1).map(x -> x * price).sum();
        return result < money ? 0 : result - money;
    }
}
