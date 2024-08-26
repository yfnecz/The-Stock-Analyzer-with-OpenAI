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
No matching `stock_analyzer_assistant` assistant found, creating a new assistant with ID:  asst_ExF53i9wQVoMCrFk8VuNZiP3
Thread created with ID:  thread_Wz5IcIqQ0rg69ejyagnyaBep
Enter the prompt for the assistant: Retrieve the weekly time series data for the stock symbol 'MSFT' for the month of July 2024. Visualize it in an image
Run initiated with ID:  run_Bn9uGrBwyuyzBAUuQ9K5XPo2
Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 8.92 seconds
Tool call with ID and name: call_gEwKb8yqKtA5wLPPbzupPN63 polygon_api
Done! Response received in 0.73 seconds.
Run initiated with ID:  run_Bn9uGrBwyuyzBAUuQ9K5XPo2
Waiting for response from `stock_analyzer_assistant` Assistant. Elapsed time: 16.46 seconds
user: Retrieve the weekly time series data for the stock symbol 'MSFT' for the month of July 2024. Visualize it in an image
assistant: I have retrieved the weekly time series data for the stock symbol 'MSFT' for the month of July 2024. Here are the details of the data:

1. Week of July 6, 2024:
   - Open: 448.66
   - Close: 467.56
   - High: 468.35
   - Low: 445.66

2. Week of July 13, 2024:
   - Open: 466.55
   - Close: 453.55
   - High: 467.7
   - Low: 450.645

3. Week of July 20, 2024:
   - Open: 453.3
   - Close: 437.11
   - High: 457.26
   - Low: 432

4. Week of July 27, 2024:
   - Open: 441.79
   - Close: 425.27
   - High: 448.39
   - Low: 417.27

5. Week of August 3, 2024:
   - Open: 431.58
   - Close: 408.49
   - High: 432.15
   - Low: 404.34

I will now visualize this data in an image.
assistant: file-D6igY093tt0A7kOZQCHWBvTt
```
![stock-image](https://github.com/user-attachments/assets/f32a4569-3d6b-4a4a-99fd-2b8bfd7de4aa)
```
Step: step_oulFZ3opLFUquZCKfCVfKKUP
Step: step_cKE1PFsgYFdhAJlLDDHlVKMR
Step: step_3vpLNs0VEO7N9WMCZCbOwFlK
Step: step_E16wUh3dhyjN4ZcwTIyOIaxg
```

