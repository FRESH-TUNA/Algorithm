class Solution {
    public int solution(int[][] sizes) {
        int w = 0, h = 0;
        for(int[] c : sizes) {
            int _w = Math.max(c[0], c[1]), _h = Math.min(c[0], c[1]);
            w = Math.max(w, _w); h =  Math.max(h, _h);
        }
        return w * h;
    }
}
