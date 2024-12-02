import java.util.Scanner;

class filip{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int rn = reverse(n), rm = reverse(m);
        if(rn>rm){
            System.out.println(rn);
        }
        else{
            System.out.println(rm);
        }
        sc.close();

    }
    public static int reverse(int num){
        int rev = 0;
        while(num!=0){
            int rem = num%10;
            rev = rev*10 + rem;
            num = num / 10;
        }
        return rev;
    }
}
