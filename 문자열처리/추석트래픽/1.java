import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;
import java.util.Iterator;

class Solution {
    private ArrayList<int[]> timelines;
    
    public int solution(String[] lines) {
        timelines = new ArrayList();
        for(String line : lines) put_start_end(line);
        Collections.sort(timelines, new MyComp());
        return calculate();
    }

    private void put_start_end(String line) {
        String[] token = line.split(" "), hms = token[1].split(":");
        int time = (int) (Double.parseDouble(
            token[2].substring(0, token[2].length() - 1)) * 1000);
        
        int hour_sec = Integer.parseInt(hms[0]) * 3600 * 1000;
        int min_sec = Integer.parseInt(hms[1]) * 60 * 1000;
        int sec = (int)(Double.parseDouble(hms[2]) * 1000);
        
        int end = hour_sec + min_sec + sec;
        int start = end - time + 1;
        
        timelines.add(new int[] {start, 0});
        timelines.add(new int[] {end + 999, 1});
    }
    
    public int calculate() {
        int answer = 0, _answer = 0;
        Iterator<int[]> i = timelines.iterator();
        while (i.hasNext()) {
            int[] temp = i.next();
            System.out.println(temp[0] + " " + temp[1]);
            _answer += (temp[1] == 0 ? 1 : -1);
            answer = Math.max(answer, _answer);
        } 
        return answer;
    }
}

class MyComp implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
        if(a[0] != b[0]) return a[0] - b[0];
        else if(a[1] != b[1]) return a[1] - b[1];
        else return -1;
    }
}