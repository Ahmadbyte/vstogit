import java.util.function.*;
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();//"Sharique ";
        String s2 = sc.nextLine();//"Ahmad"; 
        Consumer<String> c = (x) -> System.out.println(x);
        c.accept(s1+" "+s2);
    }
}