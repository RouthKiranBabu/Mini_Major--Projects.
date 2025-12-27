package _Package;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class _Java_Class {
	WebDriver driver;
	
	@BeforeMethod
	public void setup() {
//		Choosing a chrome browser to automate
		driver = new ChromeDriver();
//		Maximizing the browser
		driver.manage().window().maximize();
//		WebDriverWait wdw = new WebDriverWait(driver, Duration.ofSeconds(10));
//		Waits are used to avoid synchronization issues.
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
//		Visiting to OrangeHRM site using URL
		driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
	}
	
//	This method is called after each Test method
	@AfterMethod
	public void end_test() throws InterruptedException {// InterruptedException for Thread.sleep()
//		Wait for 4 seconds
		Thread.sleep(4000);
//		Closes the window
		driver.close();
	}
	
//	This Test runs first due to priority = 1 compared to other Test | This is the lower priority
	@Test(priority = 1)
	public void check_title() {
//		getTitle to get actual title from browser
		String actual_Title = driver.getTitle(), expected_Title = "OrangeHRM";
//		Show the actual title to see visually at console
		System.out.println("Title: " + actual_Title);
//		Assertions to for validation of Title
		Assert.assertEquals(actual_Title, expected_Title, "Title mismatch");
	}
	
//	This Test runs after the test priority = 1 as compared to other test
	@Test(priority = 2)
	public void check_url() {
//		.getCurrentUrl to get the actual URL from browser
		String actual_URL= driver.getCurrentUrl(), expected_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login";
//		Show casing the actual URL To see visually in Console
		System.out.println(actual_URL);
//		Assertions to for validation of URL
		Assert.assertEquals(actual_URL, expected_URL, "URL mismatch");
	}
	
//	This runs after all the test executes | Highest priority among others
	@Test(priority = 3)
	public void check_h5() {
//		Grabbing a element using xpath for testing
		WebElement head5 = driver.findElement(By.xpath("//h5"));
//		Getting a text of element
		String actual_text = head5.getText();
//		Check actual text is as expected using Assertions
		Assert.assertEquals(actual_text, "Login");
	}
}
