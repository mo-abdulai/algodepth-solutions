class Solution {
    public boolean isValidSudoku(char[][] board) {

        int len = board.length;

        HashSet<String> seen = new HashSet<>();

        for(int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                char number = board[i][j];
                if(number != '.'){
                    if(!seen.add(number + " in row " + i) ||
                        !seen.add(number + " in column " + j) ||
                        !seen.add(number + " in block " + i/3 + "_" + j/3)) return false;
                    
                }
            }
        }
        return true;
        
    }
}
