import java.util.Scanner;

class TestMath {
	public static void main (String[] args) {
		//code
		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
		int[] ops = new int[t];
		for(int i=0;i<t;i++){
		    int a = scanner.nextInt();
		    int b = scanner.nextInt();
		    int n = scanner.nextInt();
		    ops[i] = nthinseries(a, b, n);
		}
		for(int i=0;i<t;i++)
		    System.out.println(ops[i]);

	}
	
	private static int nthinseries(int a, int b, int n){
	    
	    double r = b*1.0d / a;
	    double nth = Math.floor(a * Math.pow(r, (n-1)));
	    return (int) nth;
	}
}