class sort //sorting
{
    public static void main(String[] args)
    {
        int arr[]={2,4,3,1,5,8,6};
        for(int i=0;i<arr.length;i++)
        {
            for(int j=i+1;j<arr.length;j++)
            {
                int temp=0;
                if(arr[j]<arr[i])
                {
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
            System.out.println(arr[i]);
        
                
        }
    }
}