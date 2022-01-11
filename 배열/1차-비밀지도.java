import java.util.stream.IntStream;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        return IntStream.range(0, n)
            .mapToObj(x -> get_map_row(n, arr1[x] | arr2[x]))
            .toArray(String[]::new);
    }

    private String get_map_row(int n, int x) {
        String row = Integer.toBinaryString(x);
        StringBuilder sb = new StringBuilder(n);

        for(int i = 0; i < n - row.length(); ++i) sb.append(' ');
        for(int i = 0; i < row.length(); ++i)
            sb.append(row.charAt(i) == '1' ? '#':' ');
        return sb.toString();
    }
}
