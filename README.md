This educational project is using OpenAI API and Polygon API to generate information about the stock prices.
It uses [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview) and [Function Calling](https://platform.openai.com/docs/guides/function-calling) so that OpenAI can use the data from [Polygon API](https://polygon.io/) to produce the needed results.




Example of execution 1:

```
Hello, welcome to the Stock Analyzer Assistant!

Matching `stock_analyzer_assistant` assistant found, using the first matching assistant with ID:  asst_RUfI77g84JNHti6vsLwzYIIX

Thread created with ID:  thread_oWtbfn6K5pZzEwSYMqeEdLaW

Enter the prompt for the assistant: Retrieve and visualize the monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024. Visualize it in an image

Run initiated with ID:  run_Cc9vo0LtAtZ3f1RSYZBVXdGF

Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 2.75 seconds

Tool call with ID and name: call_POas2MjZ011TLlPWbtK4hMNv polygon_api

Done! Response received in 0.34 seconds.

Run initiated with ID:  run_Cc9vo0LtAtZ3f1RSYZBVXdGF

Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 18.82 seconds

user: Retrieve and visualize the monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024. Visualize it in an image

assistant: I have retrieved the monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024. Here are the results:

1. Month: April 2024
   - Open Price: $179.55
   - Close Price: $171.48
   - High Price: $180.53
   - Low Price: $168.49

2. Month: May 2024
   - Open Price: $171.19
   - Close Price: $170.33
   - High Price: $178.36
   - Low Price: $164.07

3. Month: June 2024
   - Open Price: $169.58
   - Close Price: $192.25
   - High Price: $193.00
   - Low Price: $169.11

I will now visualize this monthly time series data in an image. Let me generate the visualization.
assistant: file-VnGPasPccxAphBrZIQnVYp7D

```
![stock-image](https://github.com/user-attachments/assets/f64a2bdb-43d3-4d38-8819-2e62aa7770cb)

```
Step: step_h6JdfWokDJFLsxuw5aCB4EnA
Step: step_WBIcdOu6jVOg0134D5b6yKoz
Step: step_LvkrvvQKTBcOt3am72PNH2Bi
Step: step_nEurXmMODWNjUbWsKMihJ7nP
```

Example of execution 2:

```
Hello, welcome to the Stock Analyzer Assistant!
Matching `stock_analyzer_assistant` assistant found, using the first matching assistant with ID:  asst_RUfI77g84JNHti6vsLwzYIIX
Thread created with ID:  thread_JuImMJZuzLa56QlxCAgDfnXE
Enter the prompt for the assistant: Retrieve the weekly time series data for the stock symbol 'MSFT' for the 3 months before July 2024. Visualize it in an image
Run initiated with ID:  run_EeeTqpNGjYiv39vvSUX8T6Kb
Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 2.14 seconds
Tool call with ID and name: call_qXVcwgh5dlmWBKmiGyDlIJG5 polygon_api
Done! Response received in 0.57 seconds.
Run initiated with ID:  run_EeeTqpNGjYiv39vvSUX8T6Kb
Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 24.43 seconds
user: Retrieve the weekly time series data for the stock symbol 'MSFT' for the 3 months before July 2024. Visualize it in an image
assistant: I have retrieved the weekly time series data for the stock symbol 'MSFT' for the 3 months before July 2024. Here are the results:

- Week 1: 
  - Open: $171.19
  - Close: $169.58
  - High: $171.92
  - Low: $168.23

- Week 2: 
  - Open: $169.03
  - Close: $176.55
  - High: $178.36
  - Low: $167.11

- Week 3: 
  - Open: $175.36
  - Close: $165.00
  - High: $176.63
  - Low: $164.07

- Week 4: 
  - Open: $165.52
  - Close: $169.30
  - High: $171.34
  - Low: $164.77

- Week 5: 
  - Open: $173.37
  - Close: $183.38
  - High: $187.00
  - Low: $169.11

- Week 6: 
  - Open: $182.35
  - Close: $183.05
  - High: $185.09
  - Low: $180.42

- Week 7: 
  - Open: $185.44
  - Close: $189.87
  - High: $191.09
  - Low: $184.62

- Week 8: 
  - Open: $189.33
  - Close: $189.98
  - High: $192.82
  - Low: $186.62

- Week 9: 
  - Open: $191.51
  - Close: $192.25
  - High: $193.00
  - Low: $189.10

- Week 10: 
  - Open: $192.90
  - Close: $196.89
  - High: $196.94
  - Low: $192.52

- Week 11: 
  - Open: $196.90
  - Close: $212.49
  - High: $220.20
  - Low: $192.15

- Week 12: 
  - Open: $213.37
  - Close: $207.49
  - High: $218.95
  - Low: $207.11

- Week 13: 
  - Open: $207.72
  - Close: $210.62
  - High: $216.07
  - Low: $206.59

- Week 14: 
  - Open: $212.09
  - Close: $226.34
  - High: $226.45
  - Low: $211.92

I will now visualize this data in an image.
assistant: file-Dw2dBEetwPx2zkRXwfIld3U5
```
![stock-image](https://github.com/user-attachments/assets/2391000b-69b9-4bf7-848e-8b5c8217d31b)

```
Step: step_NTx40vILquDW8hBE9kamlXLY
Step: step_pXg0fGzvMSw0duxydUMzJrJS
Step: step_SEhUtEFlRZLPWcmAsoZDLiv6
Step: step_qhcl9N1GkytEu4Cd4uukjvOj
```

