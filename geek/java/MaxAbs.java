class MaxAbs {
	public static void main(String args[]){

		int n = Integer.parseInt(args[0]);
        int m = Integer.parseInt(args[1]);
		int nn = Math.abs(n);
		int mm = Math.abs(m);
		boolean isNeg = n<0;
		int rem = nn%mm;
		int mid = mm/2;
		int ans = 0;
		//System.out.println("mid : " + mid);
		//System.out.println("rem : " + rem);
		if(mid>rem){
			ans = nn - rem;
		}
		else if (mid< rem){
			ans = nn + (mm - rem) ;
		} 
		else {
			if(mm%2==0)
				ans = nn  + (mm - rem) ;
			else 
				ans = nn - rem;
		}
		if(isNeg) ans = -ans;
		System.out.println("Closest1 : " + ans);
	}
	private static int maxAbs(int a, int b){
	    //if(a<0) a = -a;
	    //if(b<0) b = -b;
	    return (a<0?-a:a)>(b<0?-b:b)?a:b;
	}
}