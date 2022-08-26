interface Car
{
    void show();
}
interface Bike
{
    void print();
}
class vehical implements Car,Bike
{
    public void show()
    {
        System.out.println("Verna is best car");
    }
    public void print()
    {
        System.out.println("bullet");
    }
public static void main(String[] args)
{
    vehical obj=new vehical();
    obj.show();
    obj.print();
}
}