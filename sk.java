import java.io.*;
import java.util.Scanner;

class srk
{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        StringBuilder input = new StringBuilder();
        String s=sc.nextLine();
        input.append(s);
        input.reverse();
        System.out.println(input);
    }
}