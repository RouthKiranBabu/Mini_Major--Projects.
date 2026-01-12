package mvnPackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class _03_Delete_CRUD_JDBC {

	public static void main(String[] args) throws Exception{
		String url = "jdbc:mysql://localhost:3306/MySQL_JDB";
		String user = "root", pwd = "ghat123@gmail.com";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection ctn = DriverManager.getConnection(url, user, pwd);
		
		// Deleting row based on email
		String email = "TUN123@gmail.com";
		PreparedStatement ps =  ctn.prepareStatement("delete from User_Details where Email=?");
		ps.setString(1, email);
		int eu = ps.executeUpdate();
		if (eu > 0) System.out.println("Deleted at email " + email);
		else System.out.println("Not Deleted at email " + email);
		ctn.close();

	}

}
