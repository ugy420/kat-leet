import java.util.*;

class cprnumber{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String cpr = sc.next();

        char[] num = cpr.toCharArray();

        int sum = 0;

        sum += 4*Character.getNumericValue(num[0]);
        sum += 3*Character.getNumericValue(num[1]);
        sum += 2*Character.getNumericValue(num[2]);
        sum += 7*Character.getNumericValue(num[3]);
        sum += 6*Character.getNumericValue(num[4]);
        sum += 5*Character.getNumericValue(num[5]);
        sum += 4*Character.getNumericValue(num[7]);
        sum += 3*Character.getNumericValue(num[8]);
        sum += 2*Character.getNumericValue(num[9]);
        sum += Character.getNumericValue(num[10]);

        String res = (sum%11==0) ? "1" : "0";
        System.out.println(res);
    }
}