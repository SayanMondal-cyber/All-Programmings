import java.util.Scanner;
public class Armstrong_Number
{
    public static void main(String []args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number to check whether it is armstrong number or not :");
        long num = in.nextInt();
        long temp = num;
        double count = 0;
        double digit = 0;
        long sum = 0;
        while(num>0)
        {
            digit = temp%10;
            count++;
            num/=10;
        }
      
        while(temp==0)
        {
            sum += Math.pow(digit, count);
            temp/=10;
        }
        
        if(sum == num)
        {
            System.out.println("The given number is an armstrong number");
        }
        else
        {
            System.out.println("The given number is not an armstrong number");
        }
    }
}
