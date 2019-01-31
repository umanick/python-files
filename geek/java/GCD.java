import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class GCD {
	
	public static void main(String args[]){
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		long t = System.currentTimeMillis();
		System.out.println("GCD1 = " + gcd(a, b));
		System.out.println("Duration : " + (System.currentTimeMillis()-t));
		t = System.currentTimeMillis();
		System.out.println("GCD2 = " + gcd2(a, b));
		System.out.println("Duration : " + (System.currentTimeMillis()-t));
		t = System.currentTimeMillis();
		System.out.println("GCD3 = " + gcd3(a, b));
		System.out.println("Duration : " + (System.currentTimeMillis()-t));
	}
	private static int gcd(int a, int b){
	    
	    if(a==0)
	        return b;
	    if(b==0 || a==b)
	        return a;
	    if(a>b)
	        return gcd(a-b, a);
	    return gcd(a, b-a);
	}
	private static int gcd2(int u, int b){
		int shift;

		/* GCD(0,b) == b; GCD(u,0) == u, GCD(0,0) == 0 */
		if (u == 0) return b;
		if (b == 0) return u;

		/* Let shift := lg K, where K is the greatest power of 2
		dividing both u and b. */
		for (shift = 0; ((u | b) & 1) == 0; ++shift) {
		 	u >>= 1;
		 	b >>= 1;
		}

		while ((u & 1) == 0)
		u >>= 1;

		/* From here on, u is always odd. */
		do {
		/* remove all factors of 2 in b -- they are not common */
		/*   note: b is not zero, so while will terminate */
		while ((b & 1) == 0)  /* Loop X */
		   b >>= 1;

		/* Now u and b are both odd. Swap if necessary so u <= b,
		  then set b = b - u (which is even). For bignums, the
		  swapping is just pointer movement, and the subtraction
		  can be done in-place. */
		if (u > b) {
			int t = b; b = u; u = t; // Swap u and b.
		}

		b = b - u; // Here b >= u.
		} while (b != 0);

		/* restore common factors of 2 */
		return u << shift;
	}

	private static int gcd3(int a, int b){
		int times2;

		if (a == 0) return b;
		if (b == 0) return a;

		for (times2 = 0; ((a | b) & 1) == 0; ++times2) {
		 	a >>= 1;
		 	b >>= 1;
		}

		while ((a & 1) == 0)
		a >>= 1;

		do {
			while ((b & 1) == 0) 
			   b >>= 1;

			if (a > b) {
				int t = b; b = a; a = t; 
			}

			b = b - a; 
		} while (b != 0);

		return a << times2;
	}
}