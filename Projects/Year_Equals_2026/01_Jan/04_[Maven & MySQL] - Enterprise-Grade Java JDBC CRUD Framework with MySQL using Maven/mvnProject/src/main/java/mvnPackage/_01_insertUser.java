package mvnPackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class _01_insertUser {
	public static void main(String[] args) throws Exception{
		String url = "jdbc:mysql://localhost:3306/MySQL_JDB";
		String user = "root", pwd = "ghat123@gmail.com";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection ctn = DriverManager.getConnection(url, user, pwd);
		String username = "FifthUserName", email = "FIUN123@gmail.com";
		float score = 543.21f;
		// PreparedStatement ps = ctn.prepareStatement("insert into User_Details values('FirstUserName', 2.32, 'FUN123@gmail.com')");
		// Alternative of Above
		// PreparedStatement ps = ctn.prepareStatement("insert into User_Details values('" + username + "', " + score + ", '" + email + "')");
		// Alternative of Above
		PreparedStatement ps = ctn.prepareStatement("insert into User_Details values(?, ?, ?)");
		// For first ? = username, next is score, then email, this is decided when table is created in MySQL DB
		ps.setString(1, username);
		ps.setFloat(2, score);
		ps.setString(3, email);
		// Return 0 for fail, number > 0 for pass
		int is_ps = ps.executeUpdate();
		if (is_ps > 0) {
			System.out.println("Successfully Added: " + username);
		}else System.out.println("Failed to Added: " + username);
		ctn.close();
	}
}
