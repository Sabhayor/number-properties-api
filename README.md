# Number Properties API

This API provides interesting mathematical properties about a given number along with a fun fact.

## API Endpoint

**GET** `/api/classify-number?number=<number>`

## Example Request

```bash
curl -X GET "http://<your-url>/api/classify-number?number=371"
```

## Example Response

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Error Response

```json
{
    "number": "alphabet",
    "error": true
}
```

## Deployment

To deploy this API, follow these steps:

1. Clone the repository.
2. Set up a virtual environment and install dependencies.
3. Run the Flask application.
4. Deploy to a platform like Heroku.

## Dependencies

- Flask
- Flask-CORS

## License

MIT
```
