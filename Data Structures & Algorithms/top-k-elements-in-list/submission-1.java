class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> frequency = new HashMap<>();

        for(int num : nums){
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        List[] bucket = new List[nums.length + 1];

        for(int key : frequency.keySet()){
            int freq = frequency.get(key);
            if(bucket[freq] == null){
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(key);
        }


        List<Integer> result = new ArrayList<>();

        for(int i = bucket.length - 1; i >= 0 && result.size() < k; i--){
            if(bucket[i] != null && !bucket[i].isEmpty()){
                result.addAll(bucket[i]);
            }
        }

        
    return result.stream().mapToInt(i -> i).toArray();

        
    }
}
