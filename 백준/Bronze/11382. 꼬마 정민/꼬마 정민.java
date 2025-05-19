import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // 한 줄로 입력 받기
        long A = sc.nextLong();
        long B = sc.nextLong();
        long C = sc.nextLong();
        
        // A, B, C의 합 출력
        System.out.println(A + B + C);
    }
}