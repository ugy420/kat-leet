import java.util.Scanner;

class pet{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[5][4];
        for(int i=0;i<5;i++){
            for(int j=0;j<4;j++){
                arr[i][j] = sc.nextInt();
            }
        }
        sumRow(arr);
    }
    public static void sumRow(int[][] ara){
        int[] sum = new int[5]; 
        for(int i=0;i<=4;i++){
            sum[i] = ara[i][0] + ara[i][1] + ara[i][2] + ara[i][3];
        }

        int greatest = sum[0];
        for(int i=0;i<sum.length;i++){
            if(greatest<=sum[i]){
                greatest = sum[i];
            }
        }
        
        int row=1;
        for(int i=0;i<5;i++){
            if(greatest==sum[i]){
                break;
            }
            row++;
        }
        System.out.println(row + " " + greatest);
    }
}