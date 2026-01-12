package mvnPackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class _02_Update_CRUD_JDBC {

	public static void main(String[] args) throws Exception{
		String url = "jdbc:mysql://localhost:3306/MySQL_JDB";
		String user = "root", pwd = "ghat123@gmail.com";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection ctn = DriverManager.getConnection(url, user, pwd);
		
		// Updating within table
		float score = 90f; String email = "TUN123@gmail.com";
		PreparedStatement ps = ctn.prepareStatement("update User_Details set Score=? where Email=?");
		ps.setFloat(1, score); ps.setString(2, email);
		int eu = ps.executeUpdate();
		if (eu > 0) System.out.println("Updated " + score + " at email " + email);
		else System.out.println("Update at email " + email + " got failed.");
		ctn.close();
	}

}
