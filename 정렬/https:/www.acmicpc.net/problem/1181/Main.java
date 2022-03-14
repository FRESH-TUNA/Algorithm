import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    private static final Set<String> words = new HashSet<>();

    public static void main(String[] args) throws IOException {
        input();
        List<String> sorted_words = sort();
        print(sorted_words);
    }

    private static void print(List<String> sorted_words) {
        for(String s : sorted_words) System.out.println(s);
    }

    private static List<String> sort() {
        return words.stream().sorted()
                .sorted(Comparator.comparing(x -> x.length()))
                .collect(Collectors.toList());
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        while (N-- > 0) words.add(br.readLine());
        br.close();
    }
}
