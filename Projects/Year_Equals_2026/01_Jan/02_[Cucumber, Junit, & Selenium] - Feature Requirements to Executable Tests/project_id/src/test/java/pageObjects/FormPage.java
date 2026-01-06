package pageObjects;

import java.time.Duration;

import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class FormPage {
	WebDriver driver;
	String fname, lname;
	boolean is_clear = false;
	
	public FormPage(WebDriver webDriver, int impWait) {
		driver = webDriver;
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(impWait));
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(id="firstName")
	@CacheLookup
	WebElement firstname;
	
	@FindBy(id="lastName")
	@CacheLookup
	WebElement lastname;
	
	@FindBy(xpath="//input[@type='email']")
	@CacheLookup
	WebElement email;
	
	@FindBy(id="number")
	@CacheLookup
	WebElement phone;
	
	@FindBy(xpath="//div[@class='field']//textarea")
	@CacheLookup
	WebElement message;
	
	@FindBy(xpath="//input[@type='submit']")
	@CacheLookup
	WebElement submit;
	
	@FindBy(xpath="//input[@type='reset']")
	@CacheLookup
	WebElement reset;
	
	public void visitURL(String url) {
		driver.get(url);
	}
	
	public boolean checkTitle(String tle) {
		String actual_title = driver.getTitle();
		if (actual_title.equals(tle)) return true;
		return false;
	}
	
	public boolean checkURL(String url) {
		String actual_url = driver.getCurrentUrl();
		if (actual_url.equals(url)) return true;
		return false;
	}
	
	public void setFirstName(String name) {
		firstname.sendKeys(name);
		fname = name;
	}
	
	public void setLastName(String name) {
		lastname.sendKeys(name);
		lname = name;
	}
	
	public void setEmail(String mail) {
		email.sendKeys(mail);
	}
	
	public void setPhoneNumber(String num) {
		phone.sendKeys(num);
	}
	
	public void setMessage(String msg) {
		message.sendKeys(msg);
	}
	
	public void clickButton(String btn) throws InterruptedException {
		String button = btn.trim();
		if (button.equalsIgnoreCase("submit")) {
			submit.click();
		}else if(button.equalsIgnoreCase("clear")) {
			reset.click();
			driver.close();
			is_clear = true;
		}
	}
	
	public String checkAlertText(String expectedText) {
		if (is_clear) return "Cleared";
		Alert alrt = driver.switchTo().alert();
		String actualText = alrt.getText();
		if (actualText.equals(expectedText)) return "As Expected: " + expectedText;
		return "Not as Expected: " + expectedText;
	}
	
	public void clickAlertOk() {
		Alert alrt = driver.switchTo().alert();
		alrt.accept();
	}
	
	public void closeDriver() {
		driver.quit();
	}
}
