import java.io.*;
import java.util.Scanner;
  
class sss //reverse by using charArray with user input
{
    public static void main(String[] arg) {

        // declaring variable
        
        //String stringinput = "Independent";
        Scanner sc= new Scanner(System.in);
        String s=sc.nextLine();
        char[] arr = s.toCharArray();
        
        //iteration

        for (int i = arr.length - 1; i >= 0; i--)
        {
            System.out.print(arr[i]);

        }
    }
}