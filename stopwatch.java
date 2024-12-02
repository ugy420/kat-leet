import java.util.Scanner;

class stopwatch{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] N1 = new int[N];

        for(int i=0;i<N;i++){
            N1[i] = sc.nextInt();
        }
        
        if(N%2==0){
            int sum = 0;
            for(int i=0;i<N;i+=2){
                sum = sum + (N1[i+1]-N1[i]);
            }
            System.out.println(sum);
        }
        else{
            System.out.println("still running");
        }
        sc.close();
    }
}