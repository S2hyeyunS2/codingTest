import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1) BufferedReader로 빠른 입력 준비
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 2) 첫 줄: N
        int N = Integer.parseInt(br.readLine());
        
        // 3) 두 번째 줄: N개의 정수를 StringTokenizer로 토큰 분리
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        // 4) close는 선택사항이지만, 보통 닫아줍니다
        br.close();
        
        // 5) 정렬 뒤에 최소·최댓값 출력
        Arrays.sort(arr);
        System.out.println(arr[0] + " " + arr[N - 1]);
    }
}
