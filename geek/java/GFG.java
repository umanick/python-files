import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCase = scan.nextInt();
        for(int i = 0; i < testCase; i++) {
            long no = scan.nextLong();
            ArrayList<Long> arrList = new ArrayList<Long>();
            jumpingNumbers(no, arrList);
            //Collections.sort(arrList);
            for(int j = 0; j < arrList.size(); j++) {
                System.out.print(arrList.get(j) +" ");
            }
            System.out.println();
        }
    }
    public static void jumpingNumbers(long no, ArrayList<Long> arrList) {
        arrList.add(0l);
        for(long i = 1; i < 10 && i <= no; i++) {
            System.out.println("-" + i);
            bfs(no, i, arrList);
        }
    }

    public static void bfs(long no, long i, ArrayList<Long> arrList) {
        LinkedList<Long> q = new LinkedList<Long>();
        q.add(i);
        while(!q.isEmpty()) {
            long curr = q.getFirst();
            q.remove();
            System.out.println("---" + curr);
            if(curr <= no) {
                arrList.add(curr);
                int last_dig = (int)curr%10;
                if(last_dig == 0)
                    q.add((curr*10 + last_dig + 1));
                else if(last_dig == 9)
                    q.add((curr*10 + last_dig - 1));
                else {
                    q.add((curr*10 + last_dig + 1));
                    q.add((curr*10 + last_dig - 1));
                 }
            }
        }
    }
}