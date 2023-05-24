package com.example.movierentalreviewsystemcs348;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import java.sql.*;

@SpringBootApplication
public class MovieRentalReviewSystemCs348Application {

    public static void main(String[] args) {
        SpringApplication.run(MovieRentalReviewSystemCs348Application.class, args);
        // Define the DB2 JDBC Driver class
        final String JDBC_DRIVER = "com.ibm.db2.jcc.DB2Driver";
        // JDBC database URL
        final String DB_URL = "jdbc:db2://localhost:50000/CS348";

        //  Database credentials
        final String USER = "cs348GroupUser";
        final String PASS = "cs348";

        Connection conn = null;
        Statement stmt = null;
        try {
            // Register JDBC driver
            Class.forName(JDBC_DRIVER);

            // Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // Create a table
            System.out.println("Creating table in given database...");
            stmt = conn.createStatement();
            String sql = "CREATE TABLE Employee " +
                    "(ID INTEGER not NULL, " +
                    " FirstName VARCHAR(255), " +
                    " LastName VARCHAR(255), " +
                    " Email VARCHAR(255), " +
                    " PRIMARY KEY ( ID ))";
            stmt.executeUpdate(sql);
            System.out.println("Created table in given database...");

            // Execute a query to select data
            System.out.println("Creating statement...");
            stmt = conn.createStatement();
            sql = "SELECT ID, FirstName, LastName, Email FROM Employee";
            ResultSet rs = stmt.executeQuery(sql);

            // Extract data from result set
            while (rs.next()) {
                // Retrieve by column name
                int id = rs.getInt("ID");
                String first = rs.getString("FirstName");
                String last = rs.getString("LastName");
                String email = rs.getString("Email");

                // Display values
                System.out.print("ID: " + id);
                System.out.print(", First: " + first);
                System.out.print(", Last: " + last);
                System.out.println(", Email: " + email);
            }
            // Clean-up environment
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            //finally block used to close resources
            try {
                if (stmt != null)
                    stmt.close();
            } catch (SQLException se2) {
            }// nothing we can do
            try {
                if (conn != null)
                    conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            }
        }
        System.out.println("Goodbye!");
    }
}

