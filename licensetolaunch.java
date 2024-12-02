import java.util.Scanner;

class licensetolaunch{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for(int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }
        int lea = arr[0], dayz = 0;
        for(int i=0;i<N;i++){
            if(arr[i]<lea){
                lea = arr[i];
            }
        }
        for(int i=0;i<N;i++){
            if(lea<arr[i]){
                dayz++;
            }
            else if(lea==arr[i]){
                break;
            }
        }
        System.out.println(dayz);
        sc.close();
    }
}