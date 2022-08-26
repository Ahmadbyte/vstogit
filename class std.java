class Std
{
    int id;
    String name;
    int age;
    Std(int i,String n)
    {
        id=i;
        name=n;
    }
    Std(int i,String n, int a)
    {
        id=i;
        name=n;
        age=a;
    }
    void display()
    {
        System.out.println(id+" "+name+" "+age);
    }
public static void main(String[] args)
{
    Std s1=new Std(101,"Sharique");
    Std s2=new Std(102,"Ahmad",23);
    s1.display();
    s2.display();
}
}