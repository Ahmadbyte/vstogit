import java.io.*;
import java.util.Scanner;
  
class sss //reverse by using charArray
{
    public static void main(String[] arg) {

        // declaring variable
        
        String stringinput = "Independent";
        
                // convert String to character array
        
                // by using toCharArray
        
                char[] arr = stringinput.toCharArray();
        
                //iteration
        
                for (int i = arr.length - 1; i >= 0; i--)
        
                 // print reversed String
        
                    System.out.print(arr[i]);
        
        }

}

    
    