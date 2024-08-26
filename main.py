import json
from openai import OpenAI
import requests
import time


def polygon_api(multiplier, timespan, from_date, to_date):
    with open("/Users/Natali/Documents/work/PycharmProjects/pythonProject1/polygon-key.key", "r") as f:
        stock_api = f.readline()
        symbol='AAPL'
        api_url=f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={stock_api}"
        r = requests.get(api_url)
        return r.json()


class StockAnalyzer:
    def __init__(self):
        print("Hello, welcome to the Stock Analyzer Assistant!")
        with (open("/Users/Natali/Documents/work/PycharmProjects/pythonProject1/api.key", "r") as f):
            self.client = OpenAI(api_key=f.readline())
            self.assistant = None
            self.run = None
            self.thread = None

    def create_assistant(self):
        functions_list = [
            {
                "type": "function",
                "function": {
                    "name": "polygon_api",
                    "description": "Retrieve and show the time series data for the stock symbol 'AAPL'.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "multiplier": {
                                "type": "integer",
                                "description": "The size of the timespan multiplier (how many days/months/minutes/etc.)."
                            },
                            "timespan": {
                                "type": "string",
                                "description": "The size of the time window: can be day, month, second, minute, hour, week, month."
                            },
                            "from_date": {
                                "type": "string",
                                "description": "The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp."
                            },
                            "to_date": {
                                "type": "string",
                                "description": "The end of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp."
                            }
                        },
                        "required": ["multiplier", "timespan", "from_date", "to_date"],
                    },
                },
            },
            {
                "type": "code_interpreter",
            },
        ]
        c = self.client.beta.assistants.list()
        for i in c.data:
            if i.name == 'stock_analyzer_assistant':
                self.assistant = i
                print(
                    "Matching `stock_analyzer_assistant` assistant found, using the first matching assistant with ID: ",
                    self.assistant.id)
                break
        if self.assistant is None:
            self.assistant = self.client.beta.assistants.create(
                name="stock_analyzer_assistant",
                description="""You're an experienced stock analyzer assistant tasked with analyzing
        and visualizing stock market data.""",
                model="gpt-3.5-turbo",
                tools=functions_list
            )
            print("No matching `stock_analyzer_assistant` assistant found, creating a new assistant with ID: ",
                  self.assistant.id)

    def wait_on_run(self):
        while self.run.status == "queued" or self.run.status == "in_progress":
            self.run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=self.run.id,
            )
            time.sleep(0.5)
        print(f"Waiting for response from `{self.assistant.name}` Assistant. Elapsed time: {round(time.time() - self.run.started_at, 2)} seconds")

    def create_thread(self):
        self.thread = self.client.beta.threads.create()
        print("Thread created with ID: ", self.thread.id)

    def create_run(self):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content="Retrieve and visualize the monthly time series data for the stock symbol 'AAPL' for the 3 months before June 2024. Visualize it in an image"
        )

        self.run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id
        )
        print("Run initiated with ID: ", self.run.id)

    def function_calls(self):
        function_list = {
            "polygon_api": polygon_api
        }
        tool_calls = self.run.required_action.submit_tool_outputs.tool_calls
        function_outputs = []
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            print(f"Tool call with ID and name: {tool_call.id} {function_name}")
            function_args = json.loads(tool_call.function.arguments)
            function_to_call = function_list[function_name]
            t = time.time()
            function_outputs.append({"tool_call_id": tool_call.id,
                                     "output": str(function_to_call(multiplier=function_args.get("multiplier"),
                                                                    timespan=function_args.get("timespan"),
                                                                    from_date=function_args.get("from_date"),
                                                                    to_date=function_args.get("to_date")
                                                                    ))})
            print(f"Done! Response received in {round(time.time() - t, 2)} seconds.")
        self.run = self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=self.thread.id,
            run_id=self.run.id,
            tool_outputs=function_outputs
        )
        print("Run initiated with ID: ", self.run.id)

    def list_messages(self):
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id,
            order='asc'
        )

        for message in messages:
            if message.content[0].type == 'text':
                print(f"{message.role}: {message.content[0].text.value}")
            else:
                file_name = message.content[0].image_file.file_id

                print(f"{message.role}: {file_name}")
                image_data = self.client.files.content(message.content[0].image_file.file_id)
                image_data_bytes = image_data.read()
                with open("stock-image.png", "wb") as f1:
                    f1.write(image_data_bytes)

    def list_steps(self):
        run_steps = self.client.beta.threads.runs.steps.list(
            thread_id=self.thread.id,
            run_id=self.run.id
        )
        for step in run_steps:
            print(f"Step: {step.id}")


if __name__ == '__main__':
    s = StockAnalyzer()
    s.create_assistant()
    s.create_thread()
    s.create_run()
    s.wait_on_run()
    s.function_calls()
    s.wait_on_run()
    s.list_messages()
    s.list_steps()
