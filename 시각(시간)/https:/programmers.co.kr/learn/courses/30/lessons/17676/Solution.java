import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Collections;

class Solution {
    private LinkedList<Integer> start_times = new LinkedList<>();
    private LinkedList<Integer> end_times = new LinkedList<>();

    public int solution(String[] lines) {
        init_times(lines);
        return calculate();
    }

    private int calculate() {
        int res = 0, cur = 0;
        while (!start_times.isEmpty() && !end_times.isEmpty()) {
            if(start_times.getFirst() - 1000 < end_times.getFirst()) {
                start_times.removeFirst();
                cur += 1;
                res = Math.max(res, cur);
                System.out.println(cur);
            }
            else {
                end_times.removeFirst();
                cur -= 1;
            }
        }
        return res;
    }

    private void init_times(String[] lines) {
        for(String l : lines) {
            StringTokenizer st = new StringTokenizer(l);
            st.nextToken();
            int end_time = hms_to_s(st.nextToken());
            int start_time = end_time - convert_tt(st.nextToken()) + 1;
            start_times.add(start_time); end_times.add(end_time);
        }
        Collections.sort(start_times);
    }

    private int hms_to_s(String l) {
        StringTokenizer st = new StringTokenizer(l, ":");
        int h = Integer.parseInt(st.nextToken()) * 3600 * 1000;
        int m = Integer.parseInt(st.nextToken()) * 60 * 1000;
        int s = (int) (Double.parseDouble(st.nextToken()) * 1000);
        return h+m+s;
    }

    private int convert_tt(String t) {
        return (int) (Double.parseDouble(t.substring(0, t.length()-1)) * 1000);
    }
}
