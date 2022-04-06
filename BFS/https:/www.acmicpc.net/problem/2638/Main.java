import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M;
    private static boolean[][] c, extennal, deleted;
    private static final int DN = 4;
    private static final int[] DI = {-1, 0, 1, 0}, DJ = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        input();
        calc_external();
        solution();
    }

    private static void calc_external() {
        Queue<Integer> iq = new LinkedList<>(), jq = new LinkedList<>();
        extennal[0][0] = true;
        iq.add(0); jq.add(0);

        while(!iq.isEmpty()) {
            int i=iq.poll(), j=jq.poll();

            for(int d = 0; d < DN; ++d) {
                int ni = i+DI[d], nj = j+DJ[d];
                if(ni == -1 || ni == N || nj == -1 || nj == M)
                    continue;
                if(c[ni][nj] || extennal[ni][nj]) continue;
                extennal[ni][nj] = true;
                iq.add(ni); jq.add(nj);
            }
        }
    }

    private static void solution() {
        int res = 0, removed_cheese = 0;
        boolean[][] external_adjust = new boolean[N][M];
        boolean[][] deleted = new boolean[N][M];

        while(true) {
            for(int i = 0; i < N; ++i) {
                for (int j = 0; j < M; ++j)
                    if(c[i][j] && is_extenral(i, j))
                        removed_cheese += can_remove(i, j, external_adjust, deleted);
            }
            if(removed_cheese == 0) break;
            removed_cheese = 0; res += 1;
            removed_cheese(deleted);
        }
        System.out.println(res);
    }

    private static void removed_cheese(boolean[][] deleted) {
        for(int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (deleted[i][j]) c[i][j] = false;
            }
        }
    }

    private static boolean is_extenral(int i, int j) {
        int air = 0;
        for(int d = 0; d < DN; ++d) {
            int ni = i+DI[d], nj = j+DJ[d];
            if(ni == -1 || ni == N || nj == -1 || nj == M)
                continue;
            if(!c[ni][nj]) air += 1;
        }
        return air >= 2;
    }

    private static int can_remove(int i, int j,
                                     boolean[][] external_adjust, boolean[][] deleted) {
        boolean[][] traced = new boolean[N][M];
        Queue<Integer> iq = new LinkedList<>(), jq = new LinkedList<>();
        iq.add(i); jq.add(j); traced[i][j] = true;
        boolean removable = false;

        while(!iq.isEmpty()) {
            int ti=iq.poll(), tj=jq.poll();

            for(int d = 0; d < DN; ++d) {
                int ni = ti+DI[d], nj = tj+DJ[d];
                if(ni == -1 || ni == N || nj == -1 || nj == M)
                    continue;
                if(c[ni][nj] || traced[ni][nj]) continue;
                if(extennal[ni][nj]) removable = true;

                traced[ni][nj] = true;
                iq.offer(ni); jq.offer(nj);
            }
        }

        if(removable) {
            deleted[i][j] = true;
            modify_external(traced, external_adjust);
            return 1;
        }
        return 0;
    }

    private static void modify_external(boolean[][] traced, boolean[][] external_adjust) {
        for(int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j)
                external_adjust[i][j] = traced[i][j] || external_adjust[i][j];
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken()); M=Integer.parseInt(st.nextToken());
        c=new boolean[N][M]; extennal=new boolean[N][M];
        deleted = new boolean[N][M];

        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; ++j) c[i][j] = st.nextToken().equals("1");
        }
        br.close();
    }
}
