import java.util.Scanner;
//import java.util.scanner;
class xyz
{
    public static void main(String args[])
    {
        //String n,m;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first string: ");
        String str1=sc.next();
        char ch[]={};
        String s1=new String(ch);
        System.out.println(s1);
        System.out.println("Enter the second string: ");
        String str2=sc.next();
        if (str1!=str2){
            String result=str2.concat(str1);
            System.out.println(result);
        }
        else {
            System.out.println("not matching");
        }
    }
}

//         }

//         String result = str1.concat(str2);
//         System.out.println(result);
                
//     }

// }



