//Using Clases , Objects & Constructors

class Account {
        String name;
        private int account_no;
        
         //constructor
         Account(String xname, int xaccount_no) { 
             this.name = xname;
             this.account_no = xaccount_no; 
         }
         
         void displayinfo() {
             System.out.println("Name : "+ name);
             System.out.println("Account Number : " + account_no);
         }
}

public class Main {
	public static void main(String[] args) {
		Account ac1 = new Account("Umesh Pal",12345678);
		ac1.displayinfo();
		System.out.println();
		Account ac2 = new Account("Himanshu Pal", 9876543);
		ac2.displayinfo();
		System.out.println();
		Account ac3 = new Account("Khushant Pal",4567890);
		ac3.displayinfo();
		System.out.println();
		System.out.println(ac1.name);
		//System.out.println(ac1.account_no);  [account_no has private access in Account]

		System.out.println(ac2.name);
		//System.out.println(ac2.account_no); [account_no has private access in Account]
		
		System.out.println(ac3.name);
		//System.out.println(ac3.account_no); [account_no has private access in Account]
    }
}