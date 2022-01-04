import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Collectors;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        HashSet<Character> set = new HashSet(
            skill.chars().mapToObj(c -> (char) c)
                 .collect(Collectors.toList())); 

        return (int) Arrays.stream(skill_trees).filter(
            (String tree) -> {
                if(tree.length() == 0) return false;
                for(int i = 0, s_idx = 0; i < tree.length(); ++i) {
                    if(!set.contains(tree.charAt(i))) continue;
                    if(tree.charAt(i) != skill.charAt(s_idx)) 
                        return false;
                    else s_idx += 1;
                }
                return true;
            }).count();
    }
}
