class Solution {


    final char DELIMITER = '#';
    public String encode(List<String> strs) {

        StringBuilder sb = new StringBuilder();

        for(var str : strs){
            sb.append(str.length());
            sb.append(DELIMITER);
            sb.append(str);
        }

        return sb.toString();
    

    }

    public List<String> decode(String str) {

        List<String> result = new ArrayList<>();

        int i = 0;

        while(i < str.length()){
           
           int pound = str.indexOf('#', i );
           int size = Integer.valueOf(str.substring(i, pound));
           i = pound + 1;
           result.add(str.substring(i, i + size));
           i = i + size;
        }

        return result;


    }
}
