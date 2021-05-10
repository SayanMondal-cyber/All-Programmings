import java.io.*;
public class Perfect_Square
{
    public static void main(String []args)throws IOException 
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter a number :");
        int num = Integer.parseInt(br.readLine());
        boolean flag = false;
        for(int i = 1; i <= num; i++)
        {
            if(num/i==i)
            {
                flag = true;
                break;
            }
        }
        
         if(flag)
        {
             System.out.println("The given number " + num + " is a perfect square number");
        }
        else
        {
            System.out.println("The given number " + num + " is not a perfect square number");
        }
    }
}