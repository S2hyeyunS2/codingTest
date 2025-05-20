import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);

        int N=sc.nextInt();
        int sum=0;

        for(int i=1; i<=N; i++){
            sum+=i;
        }
        System.out.println(sum);
    }
}