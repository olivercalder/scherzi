public static int getMin(int[] arr) {
    return minHelper(arr, 0);
}
private static int minHelper(int[] arr, int start) {
    if (start == arr.length -1) {
        return arr[start];
    } else {
        int minOfRest = minHelper(arr, start + 1); //Find the min of the rest of the list
        if (arr[start] < minOfRest) { // if first element is actually the min
            return arr[start]; // return it
        } else{ // first 
            return minOfRest;
        }
    }
}
