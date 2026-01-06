package stepDefinitions;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import pageObjects.FormPage;

public class Steps {
	WebDriver driver;
	FormPage page;
	int delay = 250;
	boolean is_clear = false;
	
	@Given("Maximized Chrome Browser")
	public void maximized_chrome_browser() {
		driver = new ChromeDriver();
		page = new FormPage(driver, 10);
	}

	@Given("URL is {string}")
	public void url_is(String string)throws InterruptedException {
	    page.visitURL(string);
	    Thread.sleep(delay);
	}

	@Then("Check Title is {string}")
	public void check_title_is(String string) throws InterruptedException {
		page.checkTitle(string);
		Thread.sleep(delay);
	}

	@Then("Check URL is {string}")
	public void check_url_is(String string) throws InterruptedException {
		page.checkURL(string);
		Thread.sleep(delay);
	}

	@Then("Enter first name as {string}")
	public void enter_first_name_as(String string) throws InterruptedException{
		page.setFirstName(string);
		Thread.sleep(delay);
	}

	@Then("Enter last name as {string}")
	public void enter_last_name_as(String string)throws InterruptedException {
		page.setLastName(string);
		Thread.sleep(delay);
	}

	@Then("Enter email as {string}")
	public void enter_email_as(String string)throws InterruptedException {
		page.setEmail(string);
		Thread.sleep(delay);
	}

	@Then("Enter contact number as {string}")
	public void enter_contact_number_as(String string) throws InterruptedException {
		page.setPhoneNumber(string);
		Thread.sleep(delay);
	}

	@Then("Enter message as {string}")
	public void enter_message_as(String string) throws InterruptedException {
		page.setMessage(string);
		Thread.sleep(delay);
	}

	@Then("Click button named {string}")
	public void click_button_named(String string) throws InterruptedException{
		page.clickButton(string);
		Thread.sleep(delay);
	}

	@Then("Check alert text as {string}")
	public void check_alert_text_as(String string) throws InterruptedException{
		String response = page.checkAlertText(string);
		if (response.equals("Cleared")) {
			is_clear = true;
			return;
		}
		System.out.println(response);
		Thread.sleep(delay);
	}

	@Then("Click button named OK")
	public void click_button_named_ok() throws InterruptedException{
		if (is_clear) return;
		page.clickAlertOk();
		Thread.sleep(delay);
	}
	
	@Then("Wait {string} seconds then close browser")
	public void wait_seconds_then_close_browser(String string) throws InterruptedException {
	    int period = Integer.parseInt(string);
	    Thread.sleep(period);
	    page.closeDriver();
	}
}
