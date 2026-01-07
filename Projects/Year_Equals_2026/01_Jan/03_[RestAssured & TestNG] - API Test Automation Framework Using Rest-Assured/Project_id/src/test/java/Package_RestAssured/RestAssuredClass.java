package Package_RestAssured;

/*
Reference:
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Dependencies:
 * io.rest-assured, rest-assured
 * io.rest-assured, json-path
 * io.rest-assured, json-schema-validator
 * org.testng, testng
 * org.json, json
 * com.google.code.gson, gson
 * com.github.scribejava, scribejava-apis
 * 
Static Imports:
import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;*/

import static io.restassured.RestAssured.given;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

import org.testng.annotations.Test;
import io.restassured.RestAssured;

public class RestAssuredClass {
	@Test
	public void getBooks() {
//		Setting up baseURI
//		https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md#simple-books-api
		/*Protocol	=	https
		  Domain	=	simple-books-api.click*/
		RestAssured.baseURI = "https://simple-books-api.click";
		
		given()
		 .contentType("ContentType.JSON")
		
		.when()
//		Adding Path(/books) to the resource and Query parameters(type=fiction&limit=2)
//		For End Point Modification use the link below:
// 		https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md#endpoints
		
//		Optional query parameters:
//		type: fiction or non-fiction
//		limit: a number between 1 and 20.
		 .get("/books?type=fiction&limit=2")
		
		.then()
//			Validating Status code
			.statusCode(200)
//			Validating Status code
			.statusLine("HTTP/1.1 200 OK")
//			Validating ContentType
			.contentType("application/json")
			.time(lessThan(2000L))
			.header("Connection", equalTo("keep-alive"))
			.header("Content-length", equalTo("136"))
//			Assertions on Content
			.body("[0].id", equalTo(1))
			.body("[0].name", equalTo("The Russian"))
			.body("[0].type", equalTo("fiction"))
			.body("[0].available", equalTo(true))
			
			.body("[1].id", equalTo(3))
			.body("[1].name", equalTo("The Vanishing Half"))
			.body("[1].type", equalTo("fiction"))
			.body("[1].available", equalTo(true))
			
			.log().all();
	}
}
/*Right click on code -> Run As -> TestNG Test
 * 
Then Result:
[RemoteTestNG] detected TestNG version 7.11.0
SLF4J(W): No SLF4J providers were found.
SLF4J(W): Defaulting to no-operation (NOP) logger implementation
SLF4J(W): See https://www.slf4j.org/codes.html#noProviders for further details.
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 136
Connection: keep-alive
Date: Wed, 07 Jan 2026 10:03:01 GMT
X-Amzn-Trace-Id: Root=1-695e2f55-6c8f58e765be88756d7d9c63;Parent=15b4491cc02b80be;Sampled=0;Lineage=1:9ee0f5ed:0
x-amzn-RequestId: 0f850961-2cf9-4d64-a306-d8b503e4824a
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type, Authorization, X-Amz-Date, X-Api-Key, X-Amz-Security-Token
x-amz-apigw-id: WzxVdEhcIAMEOaQ=
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS, PATCH
X-Cache: Miss from cloudfront
Via: 1.1 a1b65f70ffc6e3717e17091dd53c6dda.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BLR50-P4
X-Amz-Cf-Id: BjykMS84LIOBAAIETWEcGZZLuaxHXZy0dqx6biaU7AnoXjZU1V_e8g==

[
    {
        "id": 1,
        "name": "The Russian",
        "type": "fiction",
        "available": true
    },
    {
        "id": 3,
        "name": "The Vanishing Half",
        "type": "fiction",
        "available": true
    }
]
PASSED: Package_RestAssured.RestAssuredClass.getBooks

===============================================
    Default test
    Tests run: 1, Failures: 0, Skips: 0
===============================================


===============================================
Default suite
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
===============================================
*/
