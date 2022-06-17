import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B17142 {
    private static final int MAX_VN = 10, CAN_VIRUS = 2, BLANK = 0, WALL = 1;
    private static final int MAX_ANSWER = 10000, DN = 4;
    private static final int[] DI = {-1, 0, 1, 0}, DJ = {0, 1, 0, -1};

    private static int N, M, VN, BLANK_N;
    private static int[][] G;
    private static int[] VX, VY;
    private static boolean[] VT;
    private static boolean[][] TRACED;
    private static int answer = MAX_ANSWER;

    public static void main(String[] args) throws IOException {
        input();
        virus_candid_init();
        blank_init();
        solution(0, 0);
        print();
    }

    private static void print() {
        System.out.println(answer == MAX_ANSWER ? -1 : answer);
    }


    private static void solution(int start, int c) {
        if (c == M) calculate();

        for(int i = start; i < VN; i++) {
            if (VT[i]) continue;
            VT[i] = true; solution(i+1, c+1); VT[i] = false;
        }
    }

    private static void calculate() {
        Queue<Integer> iQ=new LinkedList<>(), jQ=new LinkedList<>();
        int viruses = 0, res = 0;

        //queue init
        for (int i = 0; i < VN; ++i)
            if(VT[i]) {
                iQ.offer(VX[i]); jQ.offer(VY[i]);
                TRACED[VX[i]][VY[i]] = true;
            }

        while (!iQ.isEmpty() && viruses != BLANK_N) {
            int iteration = iQ.size();
            while(iteration-- > 0) {
                int i = iQ.poll(), j = jQ.poll();

                for (int d = 0; d < DN; ++d) {
                    int ni = i+DI[d], nj = j+DJ[d];
                    if(ni == -1 || ni == N || nj == -1 || nj == N) continue;
                    if(TRACED[ni][nj] || G[ni][nj] == WALL)
                        continue;
                    TRACED[ni][nj] = true;
                    if(G[ni][nj] == BLANK) viruses += 1;
                    iQ.add(ni); jQ.add(nj);
                }
            }
            res += 1;
        }
        if(viruses == BLANK_N) answer = Math.min(answer, res);

        //init traced
        for(int i = 0; i < N; ++i) Arrays.fill(TRACED[i], false);
    }

    private static void blank_init() {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                if(G[i][j] == BLANK) BLANK_N += 1;
        }
    }

    private static void virus_candid_init() {
        VX=new int[MAX_VN]; VY=new int[MAX_VN]; VT=new boolean[MAX_VN];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                if(G[i][j] == CAN_VIRUS) { VX[VN] = i; VY[VN++] = j; }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken()); M=Integer.parseInt(st.nextToken());
        G=new int[N][N]; TRACED=new boolean[N][N];

        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; ++j)
                G[i][j] = Integer.parseInt(st.nextToken());
        }
        br.close();
    }
}
