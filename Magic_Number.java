import java.util.Scanner;
class Magic_Number
{
    public static void main(String []args)
    {
        Scanner sc = new Scanner(System.in);
        long l = sc.nextLong();
        long temp = l;
        long sum = 0;
        while(sum>=0 && sum<=9)
        {
            long digit = temp%10;
            sum += digit;
            temp/=10;
        }
        if(temp==1)
            System.out.println("The given number is a magic number");
        else
            System.out.println("The given number is not a magic number");
    }
}
