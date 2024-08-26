This educational project is using OpenAI API and Polygon API to generate information about the stock price for sumbol 'AAPL'.
It uses [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview) and [Function Calling](https://platform.openai.com/docs/guides/function-calling) so that OpenAI can use the data from Polygon API to produce the needed results.




Example of execution:

```
Hello, welcome to the Stock Analyzer Assistant!

Matching `stock_analyzer_assistant` assistant found, using the first matching assistant with ID:  asst_RUfI77g84JNHti6vsLwzYIIX

Thread created with ID:  thread_hxTPCIg5G6rrnHK8Fiv9Ltaq

Run initiated with ID:  run_imz8ulcGyhqzKAReUzGkM9Rj

Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 3.44 seconds

Tool call with ID and name: call_1f5ZzLGOPubSee8QDTBnDGP5 polygon_api

Done! Response received in 0.37 seconds.

Run initiated with ID:  run_imz8ulcGyhqzKAReUzGkM9Rj

Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 5.43 seconds

user: Retrieve and visualize the monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024. Visualize it in an image

assistant: The monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024 has been retrieved. Here are the details of the data:
- March 2024: Close price = $171.48
- April 2024: Close price = $170.33
- May 2024: Close price = $192.25
- June 2024: Close price = $210.62

Let's visualize this data in an image.
```
![image](https://github.com/user-attachments/assets/ba8835d1-3401-4449-bd6c-64aa81e210c0)
```
Step: step_TyxwxXukw7Dkfb3O4aHF63Gp
Step: step_01dXGxK9tjvhicOrIMC9UVzO
Step: step_onE7QOdiN7LlnoOiv7T3vfB1
```



