
import java.util.HashMap;
import java.util.Map;




public class temp {


    public static int sumOfUnique(int[] nums) {
        Map<Integer, Integer> ctr = new HashMap<>();

        for(int i: nums){
            ctr.put(i, ctr.getOrDefault(i, 0) + 1);
        }

        
        int sum = 0;
        for (Map.Entry<Integer, Integer> en : ctr.entrySet()) {
            Integer key = en.getKey();
            Integer val = en.getValue();
            
            if(val == 1){
                sum += key; 
            }
        }

        return sum;
    }
    



    public static void main(String args[]){
        int[] nums  = {1,2,3,2};
        int x = sumOfUnique(nums);
        System.out.println(x);
    }
}
