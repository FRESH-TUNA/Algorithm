import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[] in, post, pre;
    private static int idx;

    public static void main(String[] args) throws IOException {
        input();
        preorder(0, N-1, 0, N-1);
        print();
    }

    private static void print() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int n : pre) bw.write(n + " ");
        bw.flush();
    }

    private static void preorder(int inS, int inE, int postS, int postE) {
        if(inS > inE || postS > postE) return;

        System.out.println(inS + " " + inE + " " + postS + " " + postE);
        pre[idx++] = post[postE];

        int mid = -1;
        for(int i = inS; i <= inE; ++i)
            if(in[i] == post[postE]) { mid = i; break; }

        preorder(inS, mid-1, postS, postS+mid-inS-1);
        preorder(mid+1, inE, postS+mid-inS, postE-1);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        in=new int[N]; post=new int[N]; pre=new int[N];

        StringTokenizer inorder = new StringTokenizer(br.readLine());
        StringTokenizer postorder = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; ++i) {
            in[i] = Integer.parseInt(inorder.nextToken());
            post[i] = Integer.parseInt(postorder.nextToken());
        }
    }
}
