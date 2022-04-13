import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class B17837 {
    final int WHITE = 0, BLUE = 2;
    final int[] DI={0, 0, 0, -1, 1}, DJ={0, 1, -1, 0, 0}, ND={0, 2, 1, 4, 3};
    final Deque<Integer> Q = new LinkedList<>();

    int N, K;
    int[][] BOARD;
    Stack<Integer>[][] STACK;
    int[] I, J, D;

    public static void main(String[] args) throws IOException {
        new B17837().call();
    }

    void call() throws IOException {
        init();
        solution();
    }

    private void solution() {
        for(int t = 1; t <= 1000; ++t) {
            if(moves()) {
                System.out.println(t);
                return;
            }
        }
        System.out.println(-1);
    }

    boolean moves() {
        for(int i = 0; i < K; ++i) if(move(i)) return true;
        return false;
    }
    boolean move(int i) {
        int oi = I[i], oj = J[i];
        int ni = oi+DI[D[i]], nj = oj+DJ[D[i]];
        if(ni == -1 || ni == N || nj == -1 || nj == N || BOARD[ni][nj] == BLUE) {
            D[i] = ND[D[i]]; ni = oi+DI[D[i]]; nj = oj+DJ[D[i]];
        }

        if(ni == -1 || ni == N || nj == -1 || nj == N || BOARD[ni][nj] == BLUE) return false;
        while(Q.isEmpty() || !(Q.peekLast() == i)) Q.addLast(STACK[oi][oj].pop());
        while(!Q.isEmpty()) {
            int node = BOARD[ni][nj] == WHITE ? Q.removeLast():Q.removeFirst();
            STACK[ni][nj].push(node);
            I[node] = ni; J[node] = nj;
        }
        I[i] = ni; J[i] = nj;
        return STACK[ni][nj].size() >= 4;
    }

    void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken()); K=Integer.parseInt(st.nextToken());
        BOARD = new int[N][N]; STACK = new Stack[N][N];
        I=new int[K]; J=new int[K]; D=new int[K];

        for(int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; ++j) {
                BOARD[i][j] = Integer.parseInt(st.nextToken());
                STACK[i][j] = new Stack<>();
            }
        }
        for (int i = 0; i < K; ++i) {
            st = new StringTokenizer(br.readLine());
            I[i]=Integer.parseInt(st.nextToken())-1;
            J[i]=Integer.parseInt(st.nextToken())-1;
            D[i]=Integer.parseInt(st.nextToken());
            STACK[I[i]][J[i]].push(i);
        }
        br.close();
    }
}
