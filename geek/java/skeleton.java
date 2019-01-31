	{
//Simple one

		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
		int[] ops = new int[t];
		for(int i=0;i<t;i++){
		    int a = scanner.nextInt();
		    int b = scanner.nextInt();
		    ops[i] = gcd2(a, b);
		}
		for(int i=0;i<t;i++)
		    System.out.println(ops[i]);


		///
		Scanner scanner = new Scanner(System.in);
		int t = 0;
		try{
	    	t = getInputs(scanner.nextLine())[0];
	    	if(t<=0 || t>30){
	    	    System.out.println("Number of test cases is not within 1-30");
		        System.exit(1);
	    	}
		} catch(Exception e){
		    System.out.println("Number of test cases is not a number");
		    System.exit(1);
		}
		int[] outputs = new int[t];
		for (int i=0;i<t;i++){
			int series[] = getInputs(scanner.nextLine());
		    
		    
		}
		for(int i=0;i<t;i++)
		    System.out.println(outputs[i]);
		
	} 
	private static int[] getInputs(String input) throws Exception {
	    if(null==input)
	        return null;
	    int[] ips = new int[2];
        String[] ipArr = input.split(" ");
        if(null!=ipArr)
            for(int i=0;i<ipArr.length;i++)
                ips[i] = Integer.parseInt(ipArr[i]);
        else 
            return null;
	    return ips;
	}

		/*
		 * Constraints:
			1 < T < 100
			1 <= Digits in Binary <= 16
		 */
		Scanner scanner = new Scanner(System.in);
		int maxT = 200;
		int maxN = 1000;
		int minN = 1;
		int t = 0;
		try{
	    	t = Integer.parseInt(scanner.nextLine());
	    	if(t<=0 || t>=maxT){
	    	    System.out.println("Number of test cases is not within range");
		        System.exit(1);
	    	}
		} catch(Exception e){
		    System.out.println("Number of test cases is not a number");
		    System.exit(1);
		}
		String[] outputs = new String[t];
		for (int i=0;i<t;i++){
			try {
			    int n = Integer.parseInt(scanner.nextLine());
		        if(n<minN || n>maxN){
		            System.out.println("N is not within range. Skipping test case.");
		        }
			} catch(Exception e){
			     System.out.println("Number of test cases is not a number. Skipping test case.");
			}
		    
		}
		for(int i=0;i<t;i++)
		    System.out.println(outputs[i]);