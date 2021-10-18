import java.util.Scanner;
public class Strong_Number
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num = in.nextInt();
        int count = 0;
        boolean flag = false;
        for(int i=2; i<=num; i++)
        {
            if(num%i==0)
            {
                for(int j=2; j<i; j++)
                {
                    if(i%j==0)
                    {
                        count++;
                    }
                }
                if(count==0)
                {
                    flag = true;
                }
                else
                {
                    flag = false;
                    break;
                }
            }
        }
        if(flag)
        {
            System.out.println("The given number " + num + " is a strong number");
        }
        else
        {
            System.out.println("The given number " + num + " is not a strong number");
        }
    }
}
