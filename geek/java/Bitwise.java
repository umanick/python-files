import java.util.Scanner;

class Bitwise {
	
	public static void main(String a[]){

     	Scanner scanner = new Scanner(System.in);
     	
     	
     	int num = (int) Math.pow(Integer.parseInt(a[0]),  Integer.parseInt(a[1]));
     	System.out.println("Sq : " + num);
     	

     	int d =  Integer.parseInt(a[2]);
     	System.out.println("k : " + d);
     	System.out.println(num/(int)Math.pow(10, d-1)%10);

     	char numstr[] = String.valueOf(num).toCharArray();
     	System.out.println("kth : " + numstr[numstr.length-d]);

     }
     	
}