package Medium.java;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class GroupByGroupSize {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        return groupByGroupSize(groupSizes);
    }






    HashMap<Integer, Integer> indexes = new HashMap<Integer, Integer>();

    /**
     * Solution 1
     * Runtime: Beats 59.52% of all users
     * Memory: Beats 48.48% of all users
     * 
     * Takes an array of people and groups them into lists based on their desired group size.
     * Groups the numbers within the array by their index within the array. The numbers in the array represent
     * the group size the index should belong in. This question assumes that each array given to it is solvable.
     * 
     * Uses a hashmap to determine the index for the groups that have been created and what size they want to be.
     * When these groups reach their desired size, the hashmap value (which represents the index the group has in the returned list)
     * will reset, and a new list/group will be created and its index will be stored as the hashmaps value for the group size key.
     * 
     * @param sizes An integer array filled with the group size of each person in it.
     * @return A list containing the lists of the created groups.
     */
    public List<List<Integer>> groupByGroupSize(int[] sizes) {
        int groupNumber = 0;
        List<List<Integer>> groups = new ArrayList<>();
        for (int i = 0; i < sizes.length; i++) {
            if (!indexes.containsKey(sizes[i])) {
                indexes.put(sizes[i], groupNumber);
                ArrayList<Integer> group = new ArrayList<>();
                group.add(i);
                groups.add(group);
                groupNumber++;
            }
            else if (groups.get(indexes.get(sizes[i])).size() >= sizes[i]) {
                indexes.put(sizes[i], groupNumber);
                ArrayList<Integer> group = new ArrayList<>();
                group.add(i);
                groups.add(group);
                groupNumber++;      
            }
            else {
                groups.get(indexes.get(sizes[i])).add(i);
            }
        }

        return groups;
    }

    public static void main(String[] args) {
        int[] groupSizes = new int[]{3,3,3,3,3,1,3};
        GroupByGroupSize grouping = new GroupByGroupSize();
        System.out.println(grouping.groupByGroupSize(groupSizes).toString());
    }
}
