import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Main2 {
    private static LinkedList<String> data = new LinkedList<String>();

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    private static void solution() {
        LinkedList<String> new_data = new LinkedList<>();
        while (!data.isEmpty()) {
            String token = data.removeFirst();
            if(token.equals("+")) new_data.add(String.valueOf(
                    Integer.parseInt(new_data.removeLast())
                    + Integer.parseInt(data.removeFirst())));
            else new_data.add(token);
        }

        data = new_data;
        int res = Integer.parseInt(data.removeFirst());
        while (!data.isEmpty()) {
            data.removeFirst();
            res -= Integer.parseInt(data.removeFirst());
        }
        System.out.println(res);
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = br.readLine().split("((?=\\+|-)|(?<=\\+|-))");
        for(String token : tokens) data.add(token);
        br.close();
    }
}
