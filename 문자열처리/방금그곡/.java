import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(String m, String[] musicinfos) {
        final String _m = replace(m);
        String[][] result = Arrays.stream(musicinfos)
            .map(x -> x.split(","))
            .map(x -> new String[]{minutes(x[0], x[1]), x[2], x[3]})
            .map(x -> new String[]{x[0], replace(x[1]), replace(x[2])})
            .map(x -> new String[]{x[0], x[1], codes(x[0], x[2])})
            .filter(x -> x[2].contains(_m))
            .sorted(komparator()).toArray(String[][]::new);
        return result.length > 0 ? result[0][1] : "(None)";
    }
    
    private static String minutes(String start, String end) {
        String[] s = start.split(":"), e = end.split(":");
        int h = Integer.parseInt(e[0]) - Integer.parseInt(s[0]);
        int m = Integer.parseInt(e[1]) - Integer.parseInt(s[1]);
        return h * 60 + m + "";
    }
    
    private static String replace(String target) {
        return target.replace("C#", "c").replace("D#", "d")
            .replace("F#", "f").replace("G#", "g").replace("A#", "a");
    }
    
    private static String codes(String minutes, String code) {
        int _minutes = Integer.parseInt(minutes); 
        int len = code.length();
        int mock = _minutes / len, remain = _minutes % len;
        return code.repeat(mock) + code.substring(0, remain);
    }
    
    private static Comparator<String[]> komparator() {
        return new Comparator<String[]>() {
            @Override
            public int compare(String[] x, String[] y) {
                int x_min = Integer.parseInt(x[0]);
                int y_min = Integer.parseInt(y[0]);
                return (x_min != y_min) ? y_min - x_min : 1;
            }
        };
    }
}
