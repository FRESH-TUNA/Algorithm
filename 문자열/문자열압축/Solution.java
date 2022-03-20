public class Solution {
    public int solution(String s) {
        int res = s.length();
        for (int i = 1; i <= s.length() / 2; ++i) 
            res = Math.min(res, compress(s, i));
        return res;
    }

    private int compress(String s, int length) {
        int count = 1, i = length;
        String compareTO = s.substring(0, length);
        StringBuilder sb = new StringBuilder();

        while (i <= s.length()-length) {
            String compareFrom = s.substring(i, i+length);
            if (compareFrom.equals(compareTO)) count += 1;
            else {
                if(count > 1) sb.append(count);
                sb.append(compareTO);
                count = 1;
                compareTO = compareFrom;
            }
            i += length;
        }
        if(count > 1) sb.append(count);
        sb.append(compareTO);
        return sb.length() + s.substring(i, s.length()).length();
    }
}
