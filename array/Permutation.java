package array;
import java.util.HashSet;

public class Permutation {
    

    public static void printArray(int[] arr)
    {
        System.out.print("\n");
        for(int i=0; i<arr.length; i++)
            System.out.print(arr[i] + " ");
    }
    public static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public static void printPerm(int [] arr, int ci){
        if(ci == arr.length){
            printArray(arr);
            return;
        }
        HashSet<Integer> hash = new HashSet<Integer>();

        for(int i=ci; i<arr.length; i++)
        {
            if(!hash.contains(arr[i]))
            {
                hash.add(arr[i]);
                swap(arr, i, ci);
                printPerm(arr, ci+1);
                swap(arr, i, ci);
            }
        }
    }

    public static void main(String[] obj)
    {
        int[] a = {1,2,2};
        printPerm(a, 0);
    }
}

