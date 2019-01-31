class LCM 
{ 
    // Recursive method to return gcd of a and b 
    private static int gcd(int a, int b){
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
      
    // method to return LCM of two numbers 
    static int lcm(int a, int b) 
    { 
        return (a*b)/gcd(a, b); 
    } 
      
    // Driver method 
    public static void main(String[] args)  
    { 
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        System.out.println("LCM of " + a +" and " + b + " is " + lcm(a, b)); 
    } 
} 