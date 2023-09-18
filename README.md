
# RabbitMQ and MongoDB Project

This project demonstrates the use of RabbitMQ for simulating email delivery to contacts stored in a MongoDB database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3 installed on your system.
- RabbitMQ server accessible with the required credentials.
- MongoDB server accessible with the required connection URI.
- Python packages listed in `requirements.txt` installed.

## Getting Started

1. Clone the repository:

   - Clone this repository to your local machine.

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application by creating a `config.py` file with your RabbitMQ and MongoDB credentials. Use the provided template in the repository.

5. Define your Contact model in the `models.py` file as per your project requirements.

6. Write your `producer.py` script to generate contacts and send messages to RabbitMQ. Adjust the code according to your needs.

7. Write your `consumer.py` script to consume messages from RabbitMQ and process them. Customize the code as necessary.

8. Run the producer and consumer scripts in separate terminal windows:

   ```bash
   python producer.py
   ```

   ```bash
   python consumer.py
   ```

9. Observe the messages being processed and contacts updated in the MongoDB database.

## Contributing

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature/your-feature`.
5. Create a pull request.
