import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

class Solution {
    private static int ANSWER_MAX = 8;
    private static HashSet<Integer>[] db = new HashSet[ANSWER_MAX+1];

    public int solution(int N, int number) {
        StringBuilder base = new StringBuilder();

        // set[answer]에 있으면 바로 반환
        for(int answer = 1; answer <= ANSWER_MAX; answer++)
            if(make_db(base, answer, N).contains(number)) return answer;
        return -1;
    }

    private HashSet<Integer> make_db(StringBuilder base, int answer, int N) {
        db[answer] = new HashSet();
        db[answer].add(Integer.parseInt(base.append(N).toString()));

        for(int i = 1, j = answer - 1; i <= j; ++i, --j) {
            Iterator<Integer> db_i = db[i].iterator();
            while(db_i.hasNext()) {
                int i_value = db_i.next();
                Iterator<Integer> db_j = db[j].iterator();
                while (db_j.hasNext()) insert(db[answer], i_value, db_j.next());
            }
        }
        return db[answer];
    }

    private void insert(HashSet<Integer> db, int i, int j) {
        List<Integer> cases = Arrays.asList(i+j, i*j);
        db.addAll(cases);   if(i > j) db.add(i-j);  if(j > i) db.add(j-i);
        if(j != 0 && i/j != 0) db.add(i/j);
        if(i != 0 && j/i != 0) db.add(j/i);
    }
}