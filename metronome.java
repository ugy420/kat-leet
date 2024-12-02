import java.util.Scanner;

class metronome{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int in = sc.nextInt();
        float in1 = in;
        float rev = in1/4;
        System.out.println(rev);
        sc.close();
    }
}