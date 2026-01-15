/*{
    "id": "y6ka5OkBynzp3XQDhagkW",
    "bookId": 1,
    "customerName": "PostmanAPI",
    "quantity": 1,
    "timestamp": 1768398993734
}*/

let responseData = pm.response.json();

let jsonSchema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "bookId": {
            "type": "integer"
        },
        "customerName": {
            "type": "string"
        },
        "quantity": {
            "type": "integer"
        },
        "timestamp": {
            "type": "integer"
        }
    }
}

pm.test("JSON schema Validation using direct method", () => {
    pm.response.to.have.jsonSchema(jsonSchema);
})

pm.test("Json Schema Validation", () => {
    pm.expect(tv4.validate(responseData, jsonSchema)).to.be.true;
})