import java.util.*;
public class Bubble_Sort_Array
{
    public static void main(String []args)
    {
         int arr[] = new int[10];
        Scanner in = new Scanner(System.in);
        for(int a = 0; a<arr.length; a++)
         {
            arr[a] = in.nextInt();
        }
        
        for(int i = 0; i<arr.length-1; i++)
        {
            for(int j = 0; j<arr.length-i-1; j++)
            {
                if(arr[j]>arr[j+1])
                {
                    arr[j] = arr[j]+arr[j+1];
                    arr[j+1] = arr[j]-arr[j+1];
                    arr[j] = arr[j]-arr[j+1];
                }
            }
        }
        
         System.out.println("Sorted elements of the array in ascending order are :");
        
        for(int n = 0; n<arr.length; n++)
        {
            System.out.print(arr[n]+", ");
        }
    }
}
