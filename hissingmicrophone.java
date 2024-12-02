import java.util.Scanner;

class hissingmicrophone{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String let = sc.next();
        String prt = "no hiss";
        for(int i=0;i<let.length()-1;i++){
            if(let.charAt(i)=='s' && let.charAt(i+1)=='s'){
                prt = "hiss";
                break;
            }
        }
        System.out.println(prt);
        sc.close();
    }
}