import java.util.Scanner;

public class Scan {
	
	public static void main(String a[]){

		String input = "1 fish 2 fish red fish blue fish";
     	Scanner s = new Scanner(input);
     	while(s.hasNext()){
     		if(s.hasNextInt())
     			System.out.println(s.nextInt());
     	}
	}
}