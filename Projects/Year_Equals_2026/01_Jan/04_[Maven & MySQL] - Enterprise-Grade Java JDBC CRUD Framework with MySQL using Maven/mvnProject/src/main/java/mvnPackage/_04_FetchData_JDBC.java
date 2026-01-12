package mvnPackage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class _04_FetchData_JDBC {

	public static void main(String[] args) throws Exception{
		String url = "jdbc:mysql://localhost:3306/MySQL_JDB";
		String user = "root", pwd = "ghat123@gmail.com";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection ctn = DriverManager.getConnection(url, user, pwd);
		
		PreparedStatement ps = ctn.prepareStatement("select * from User_Details");
		ResultSet rs = ps.executeQuery();
		while (rs.next()) {
			System.out.print("Name:" + rs.getString("UserName"));
			System.out.print("\tScore:" + rs.getString("Score"));
			System.out.println("\tEmail:" + rs.getString("Email"));
		}
		ctn.close();
	}

}
