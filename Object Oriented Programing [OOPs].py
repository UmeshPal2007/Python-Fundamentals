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


//Constructors and Shallow copy 

class Student {
    String name;
    double cgpa;

    // Standard Constructor
    Student(String name, double cgpa) { 
        this.name = name;
        this.cgpa = cgpa;
    }

    // Copy Constructor
    Student(Student other) {
        this.name = other.name;
        this.cgpa = other.cgpa;
    }

    void displayinfo() {
        System.out.println("Name : " + this.name);
        System.out.println("CGPA : " + this.cgpa);
    }
}

public class Main { // Changed to match filename Main.java
    public static void main(String args[]) {
        // 1. Create the original student object
        Student s1 = new Student("Umesh Pal", 9.8);

        // 2. Use the Copy Constructor to create a duplicate
        // This creates a NEW object in memory with the same values
        Student s2 = new Student(s1);

        // 3. Modify the copy (the "Task")
        // Notice that we only change s2
        s2.name = "Umesh Pal - Updated Profile";
        s2.cgpa = 9.9;

        // 4. Compare the outputs
        System.out.println("--- Original Student Data ---");
        s1.displayinfo(); 

        System.out.println("\n--- Modified Copy Data ---");
        s2.displayinfo();
    }
}
